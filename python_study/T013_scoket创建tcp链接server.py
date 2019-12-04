'''
# https://www.cnblogs.com/dalaoban/p/9331113.html
sk = socket.socket()
sk.bind(('127.0.0.1', 8898))  #把地址绑定到套接字
sk.listen()          #监听链接
conn, addr = sk.accept() #接受客户端链接
ret = conn.recv(1024)  #接收客户端信息
print(ret)       #打印客户端信息
conn.send(b'hi')        #向客户端发送信息
conn.close()       #关闭客户端套接字
sk.close()        #关闭服务器套接字(可选)
'''

import socket
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('已经绑定服务端地址 127.0.0.1 端口是 9090')
sk.bind(('127.0.0.1', 9090))
print('创建listen，最大连接数为2')
sk.listen(2)
print('已经创建socket链接listen。。。')
while 1:
    print('等待客户端连接')
    conn, addr = sk.accept() #  等待连接 -- 阻塞

    while 1:
        msg_r = conn.recv(1024).decode('utf-8') # 阻塞等待接收客户端发来的消息
        print('接收到来自%s的一个消息:%s' % (addr, msg_r))
        if msg_r == 'q':
            break

        msg_s = input('>>>server收到连接请求，请输入返回信息：')
        conn.send(msg_s.encode('utf-8')) # 发送给客户端消息
        if msg_s == 'q':
            break

    conn.close() # 服务器和当前客户端断开连接,程序回到上一层死循环,重新等待客户端的连接
sk.close()
