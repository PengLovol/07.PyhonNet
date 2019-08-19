from socket import *
import sys

#从命令行输入IP，端口
HOST=sys.argv[1]
PORT=int(sys.argv[2])
ADDR=(HOST,PORT)
if len(sys.argv) < 3:
    print('''
        argv is error!
        run as 
        python3 udp_client.py 127.0.0.1 8888
        ''')
    raise
#创建数据报套接字
sockfd=socket(AF_INET,SOCK_DGRAM)


#消息收发
while True:
    data=input('消息：')
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)
    data,addr=sockfd.recvfrom(1024)
    print("从服务器收到：",data.decode())

sockfd.close()
