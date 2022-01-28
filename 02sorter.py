#Adhikari, Reason
#This is a sorter

r = open("op.txt","r")  # open file, read-only
o = open("s.txt", "w") # open file, write
lines = r.readlines()
lines.sort()

for line in lines:
	o.write(line)
r.close()
o.close()