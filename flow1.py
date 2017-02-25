def main():#good programming habits
    import random #import random module
    ran = random.randint(1, 10)#generation of random variable
    print(ran) #showing variable ran
    num = int(input("guess a number from 1-10  "))  # asking user to guess a number bet 1-10
    if ran == num:  # if user guess is equal to random variable
        print("congratz you won!")  # message for user who guessed correctly



    else: #if wrong guess
        turncounter=1
        while ran != num and turncounter <=2: #looping 2 times meeting the condition of ran
            if num == ran + 2:
                print("getting warm lucky buster")
                turncounter=turncounter+1
            elif num == ran + 1:
                print("HOT")
                turncounter = turncounter + 1
            elif num == ran - 1:
                print("HOT")
                turncounter = turncounter + 1
            elif num == ran - 2:
                print("getting warm lucky buster")
                turncounter = turncounter + 1
            elif ran==num:
                print("congratz u won sucker")  # display message you lose
                turncounter = turncounter + 1
            else:
                print("cold!")
            num = int(input("guess a number from 1-10  "))  # asking user to guess a number bet 1-10








main()