from socket import  *
from select import  select

#创建套接字作为我们关注的IO
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)

rlist=[s]
wlist=[]
xlist=[]

while True:

#提交检测我们关注的IO等待IO发生
    rs,ws,xs=select(rlist,wlist,xlist)
    for r in rs:
        if r is s:
            c,addr=r.accept()
            print("Connect from",addr)
            rlist.append(c) #添加到关注列表
        else:
            data=r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
            print(data.decode())
            r.send(b'Receive your message')
    for w in ws:
        pass
    for x in xs:
        pass