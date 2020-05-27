
client_data='''GET /favicon.ico HTTP/1.1
Host: 127.0.0.1:8002
Connection: keep-alive'''
request_path = client_data.split('\r\n')[0].split()[1]
print(request_path)