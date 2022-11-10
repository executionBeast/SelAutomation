#19073500000


baseRoll = "20073502090"


i = 1
rollno = []
print(rollno)
print(rollno)
incr = ""

while i <=6:
    if i<10:
        roll=baseRoll+"0"+str(i)
        rollno.append(roll)
        #print(rollno)
        i =i+1
    else:
        roll=baseRoll+str(i)
        rollno.append(roll)
        #print(rollno)
        i = i+1

print(rollno)
