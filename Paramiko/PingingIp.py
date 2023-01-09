import paramiko
import pandas as pd
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="10.0.2.15",username="siri",password="1356")
ip=input("Enter ip address")
number=int(input("Enter Number of packets:"))
command=f'ping -c {number} {ip}'
stdin,stdout,stderr,=ssh.exec_command(command)
# df=pd.DataFrame(stdout)
# print
flag=False
for i in stdout.readlines():
    if "ttl" not in i:
        print(i)
        flag=True
    else:
        flag=False
if flag==True:
    print("host reached")
else:
    print("host unreachable")
# print(df.columns)
# df.to_excel('df.xlsx')