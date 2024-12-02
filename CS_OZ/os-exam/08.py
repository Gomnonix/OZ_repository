# 내 파이썬 프로그램의 이름을 알아보자.
import psutil, os

if __name__ == '__main__':
    name08 = os.getpid()
    print("08.py 프로세스 아이디 :", name08)

    for proc in psutil.process_iter():
    
        if proc.pid == name08:
            print(f'내 파이썬 프로그램 이름 : {proc.pid}')

        

