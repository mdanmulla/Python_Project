# hi sir mera game jaroor dekhna
# sir mene jitna functions ho sakta he utna use karne ke try kiya he
import random
over = 0
pc_wincount = 0
human_wincount = 0

print('''
Total chance is 10 you have to enter your choice 10 times than pc will decide who will win!
If match Your is draw than you don't lose any chance it is same as before

1 or s for Snake
2 or w for Water
3 or g for Gun

''')
def win():
    print('You win!\n')
    global human_wincount
    human_wincount = human_wincount + 1
    global over
    over = over + 1

def lose():
    print('You lose!\n')
    global pc_wincount
    pc_wincount = pc_wincount + 1
    global over
    over = over + 1

def Game_run():
    pc_list = ['Snake', 'Water', 'Gun']
    Pc_choice = random.choice(pc_list)

    Human_choice = input('Enter one of them:- ')
    if Human_choice =='s' or Human_choice== 'S' or  Human_choice== 'snake' or Human_choice == "1":
        Human_choice= Human_choice.replace(Human_choice,'Snake')
    elif Human_choice == 'w' or Human_choice == 'W' or Human_choice == 'water' or Human_choice == "2":
                Human_choice= Human_choice.replace(Human_choice,'Water')
    elif Human_choice == 'g' or Human_choice == 'G' or Human_choice == 'gun' or Human_choice == "3":
        Human_choice = Human_choice.replace(Human_choice,'Gun')
    elif Human_choice not in Pc_choice:
        print('Check your endered number or spelling')

    if Pc_choice == 'Snake' and Human_choice == 'Gun' :
        win()
    elif Pc_choice == 'Water' and Human_choice == 'Snake':
        win()
    elif Pc_choice == 'Gun' and Human_choice == 'Water':
        win()
    elif Pc_choice == 'Gun' and Human_choice == 'Snake':
        lose()
    elif Pc_choice == 'Snake' and Human_choice == 'Water':
        lose()
    elif Pc_choice == 'Water' and Human_choice == 'Gun':
        lose()
    elif Pc_choice == Human_choice:
        print('Match Draw Try again!\n')

while(True):
    if over<=10:Game_run()
    if over == 10:
        if pc_wincount > human_wincount:
            print('\nPc is defeated you!\n')

        elif pc_wincount < human_wincount:
            print('\nCongratulation you win!\n')
        else:
            print('\nGame over! both score is same\n')

        print("Pc Score"' =', pc_wincount)
        print("Your Score"' =', human_wincount)
        continuee = input('If you want to paly again hit y or yes other wise just hit enter:- ')
        continuee = continuee.lower()
        if continuee == 'y' or continuee =='yes':
            over = 0
            pc_wincount = 0
            human_wincount = 0
            continue
        else:break
