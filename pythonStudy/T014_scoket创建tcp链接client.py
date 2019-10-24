import socket
'''
sk = socket.socket()           # 创建客户套接字
sk.connect(('127.0.0.1', 8898))    # 尝试连接服务器
sk.send(b'hello!')
ret = sk.recv(1024)         # 对话(发送/接收)
print(ret)
sk.close()            # 关闭客户套接字
'''
from socket import socket
sk = socket()
sk.connect(('127.0.0.1', 9090))
print('客户段已经连接服务端')
while 1:
    msg_s = input('>>>请输入客户端向server发送的信息：')
    sk.send(msg_s.encode('utf-8'))
    if msg_s == 'q':
        break
    msg_r = sk.recv(1024).decode('utf-8')
    print('server端返回信息：'+msg_r)
    if msg_r == 'q':
        break

sk.close()