# In this project i used for and while both loops to drow a star pattern

print('printing pattern using for loop')
try:
    Input = int(input('Enter the number of columns and rows you want to drow\n'))
    Boolin = bool(int(input('Enter 0 for up to down columns and 1 for down to up column\n')))
    if Boolin==False:
        for i in range(Input):
            for j in range(i):
                print('*',end=' ')
            print()
    else:
        for i in range(Input,0,-1):
            for j in range(i):
                print('*',end=' ')
            print()
except Exception as Error:
    print(Error)



print('star patter using while loop\n')
try:
    Input = int(input('Enter the number of columns and rows you want to drow\n'))
    Boolin = bool(int(input('Enter 0 for up to down columns and 1 for down to up column\n')))
    if Boolin==True:
        Count = 1
        while(Count<=Input):
            print('* '*Count,end='\n')
            Count+=1
    else:
        Count = Input
        while(Count!=0):
            print('* '*Count,end='\n')
            Count-=1

except Exception as Error:
    print('Please enter only numbers')

