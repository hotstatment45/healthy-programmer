#Programmer care
import time
import datetime

def getdate():
    return datetime.datetime.now()

player_name = input("Enter your name: ")

#Story data -  user
def create_data():
    coin1 = 0
    coin2 = 0
    coin3 = 0

    def countdown():
            for i in range(1,4):
                time.sleep(i)
                print(i)
    while True:
            print("choose an option:\n 1.Strain\n2.Tired\n3.Headache\n4.Quit\n")
            user_enter = int(input("Enter any one(1,2, 3 or 4) \n"))
            if user_enter == 4:
                print("Goodbye!")
                break
            else:
                if user_enter == 1:
                    print("Take some rest and close you eyes as count down.")
                    countdown()
                    coin1 += 5
                elif user_enter == 2:
                    print("Stand up!, stretch your body.")
                    countdown()
                    coin2 += 5
                else:
                    print("Turn off screen and meditate")
                    countdown()
                    coin3 += 5
    total_coin = coin3 + coin2 + coin1
    with open(f"user_{player_name}.txt","w") as f:
        f.write(f"Date: {getdate()}\n Name: {player_name}\n Your coin---->\n1.Eye exercise - {coin1}\n2.Physical exercise - {coin2}\n3.Mind relax - {coin3}\n Great! you earn total {total_coin} coin!!")
        print("Great!! you file is created.")

def view_data():
    try:
        with open(f"user_{player_name}.txt", "r") as f:
            print("Here's your record!---->")
            print(f.readlines())
    except FileNotFoundError:
        print("Sorry!, File isn't created yet.")



try:
    while True:
        print("===Hurry up ,-> Exercise!===")
        print("Choose an option:\n1.create data\n2.view data\n3.None")
        choose = int(input("Enter in num: "))
        if choose == 1:
            create_data()
        elif choose == 2:
            view_data()
        elif choose == 3:
            print("Goodbye!")
            break
except ValueError:
    print(f"Enter a valid value.")

except KeyboardInterrupt:
    print(f"Enter a value without combination of “CTRL + C” or “CTRL + Z”.")


