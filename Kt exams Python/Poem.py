f=open("Poem.txt","w+")
s="johnny johnny \nyes papa \neating sugar \nno papa."
f.write(s)
f.seek(0)
print(f.read())
f.close
