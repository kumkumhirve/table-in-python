'''Q12: Write a program to print table of any number .'''

num = int (input ("enter the number:"))
i = 1

for i in range(1,11):
    table = num*i
    i+=1
    print(table)
