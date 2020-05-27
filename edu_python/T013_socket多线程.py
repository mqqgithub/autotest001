import socket
sk = socket.socket()
sk.bind(('127.0.0.1', 8007))
sk.listen()
conn,addr = sk.accept()
from_b_msg = conn.recv(1024)
str_msg = from_b_msg.decode('utf-8')
print('浏览器请求信息：', str_msg)

# conn.send(b'HTTP/1.1 200 ok \r\ncontent-type:text/html;charset=utf-8;\r\n')
conn.send(b'HTTP/1.1 200 ok \r\n\r\n')

with open(r'T013.html','rb') as f:
    f_data = f.read()
conn.send(f_data)
# conn.close()
