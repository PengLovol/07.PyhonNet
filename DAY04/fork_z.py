#僵尸进程
import os
from time import sleep 

pid = os.fork()

if pid < 0:
    print("create process failed")
elif pid == 0:
    print("Child Process:",os.getpid())
    print("Child process exit")
else:
    print("parent process") #父进程陷入死循环不退出,子进程先退出
    while True:
        pass 