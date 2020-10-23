from subprocess import Popen, CREATE_NEW_CONSOLE
import os
prosess_list=[]

for i in range(16):
    prosess_list.append(Popen("python client.py", creationflags=CREATE_NEW_CONSOLE))

print("16 clients connected")
