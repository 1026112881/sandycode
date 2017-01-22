import io
import random

file=open("MockData.txt","w")

for i in range(1000000):
		file.write(str(i)+" |x "+str(random.randint(0,500000-1))+":1 |y "+str(random.randint(0,19))+":1\r\n")
		file.write(str(i)+" |x "+str(random.randint(0,500000-1))+":1\r\n")
		file.write(str(i)+" |x "+str(random.randint(0,500000-1))+":1\r\n")
		file.write(str(i)+" |x "+str(random.randint(0,500000-1))+":1\r\n")
		file.write(str(i)+" |x "+str(random.randint(0,500000-1))+":1\r\n")
		file.write(str(i)+" |x "+str(random.randint(0,500000-1))+":1\r\n")
		file.write(str(i)+" |x "+str(random.randint(0,500000-1))+":1\r\n")
		file.write(str(i)+" |x "+str(random.randint(0,500000-1))+":1\r\n")
		file.write(str(i)+" |x "+str(random.randint(0,500000-1))+":1\r\n")
		file.write(str(i)+" |x "+str(random.randint(0,500000-1))+":1\r\n")
		file.write(str(i)+" |x "+str(random.randint(0,500000-1))+":1\r\n")
		file.write(str(i)+" |x "+str(random.randint(0,500000-1))+":1\r\n")
		file.write(str(i)+" |x "+str(random.randint(0,500000-1))+":1\r\n")
		file.write(str(i)+" |x "+str(random.randint(0,500000-1))+":1\r\n")
		file.write(str(i)+" |x "+str(random.randint(0,500000-1))+":1\r\n")

file.close()
