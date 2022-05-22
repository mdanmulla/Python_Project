import datetime


def getdate():
    import datetime
    return datetime.datetime.now()
print("Anmulla for 1 , Rohan for 2, Hammad for 3")
clint_name = int(input('Enter the name for clint: '))
read_add = int(input('Enter 1 for add and 2 for read dite or workout list: '))
exercise_dite = int(input('Enter exercise for 1 dite for 2: '))
year = str(datetime.datetime.now().year)
month = str(datetime.datetime.now().month)
day = str(datetime.datetime.now().day)
hour = str(datetime.datetime.now().hour)
minutes = str(datetime.datetime.now().minute)

if clint_name==1 and read_add==1 and exercise_dite==1:
    print("you have selected Anmulla's file for adding Exercise")
    done_Exe = input('Enter the name of exercise you have done: ')
    with open('anmulla_exercise.txt', 'a') as op:
        op.write(done_Exe)
        op.write(' '+year+'\\'+month+'\\'+day+'\\'+ hour + ':' + minutes + '\n')


elif clint_name == 1 and read_add == 1 and exercise_dite == 2:
    print("you have selected Anmulla's file for adding dite")
    what_dite = input('Enter the name of food you have consumed: ')
    with open('anmulla_dite.txt', 'a') as op:
        op.write(what_dite)
        op.write(' '+year+'\\'+month+'\\'+day+'\\'+ hour + ':' + minutes + '\n')


elif clint_name == 1 and read_add == 2 and exercise_dite == 1:
    print("you have selected Anmulla's file for reading Exercise")
    with open('anmulla_exercise.txt') as read1:
        for i in read1:
            print(i,end='')

elif clint_name == 1 and read_add == 2 and exercise_dite == 2:
    print("you have selected Anmulla's file for reading dite")
    with open('anmulla_dite.txt') as read1:
        for i in read1:
            print(i,end='')


if clint_name==2 and read_add==1 and exercise_dite==1:
    print("you have selected Rohan's file for adding Exercise")
    done_Exe = input('Enter the name of exercise you have done: ')
    with open('rohan_exercise.txt', 'a' + "\n") as op:
        op.write(done_Exe)
        op.write(' '+year+'\\'+month+'\\'+day+'\\'+ hour + ':' + minutes + '\n')

elif clint_name == 2 and read_add == 1 and exercise_dite == 2:
    print("you have selected Rohan's file for adding dite")
    what_dite = input('Enter the name of food you have consumed: ')
    with open('rohan_dite.txt', 'a') as op:
        op.write(what_dite)
        op.write(' '+year+'\\'+month+'\\'+day+'\\'+ hour + ':' + minutes + '\n')

elif clint_name == 2 and read_add == 2 and exercise_dite == 1:
    print("you have selected Rohan's file for reading Exercise")
    with open('rohan_exercise.txt') as read1:
        for i in read1:
            print(i,end='')

elif clint_name == 2 and read_add == 2 and exercise_dite == 2:
    print("you have selected Rohan's file for reading dite")
    with open('rohan_dite.txt') as read1:
        for i in read1:
            print(i,end='')

if clint_name==3 and read_add==1 and exercise_dite==1:
    print("you have selected hammed's file for adding Exercise")
    done_Exe = input('Enter the name of exercise you have done: ')
    with open('hammed_exercise.txt', 'a') as op:
        op.write(done_Exe)
        op.write(' '+year+'\\'+month+'\\'+day+'\\'+ hour + ':' + minutes + '\n')


elif clint_name == 3 and read_add == 1 and exercise_dite == 2:
    print("you have selected hammed's file for adding dite")
    what_dite = input('Enter the name of food you have consumed: ')
    with open('hammad_dite.txt','a') as op:
        op.write(what_dite)
        op.write(' '+year+'\\'+month+'\\'+day+'\\'+ hour + ':' + minutes + '\n')

elif clint_name == 3 and read_add == 2 and exercise_dite == 1:
    print("you have selected hammed's file for reading Exercise")
    with open('hammed_exercise.txt') as read1:
        for i in read1:
            print(i,end='')

elif clint_name == 3 and read_add == 2 and exercise_dite == 2:
    print("you have selected hammed's file for reading dite")
    with open('hammad_dite.txt') as read1:
        for i in read1:
            print(i,end='')