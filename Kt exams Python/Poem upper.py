f=open("Ok.txt","r")
data=f.readlines()
for line in data:
    print(line.strip().upper())
f.close()
