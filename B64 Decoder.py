import base64
count = 0
f = open(r"C:\Users\opc\Desktop\new\newfile.txt")
f1 = open("new.txt","w")
Lines = f.readlines()
for line in Lines:
        try:
                content = line.split(':')
                temp1 = content[0]
                temp2 = content[1].replace('\n','')
                data = base64.b64decode(temp2)
                string = temp1+":"+str(data)+"\n"
        except:
                count += 1
                print(count)
        finally:
                f1.write(string)
f.close()
f1.close()
