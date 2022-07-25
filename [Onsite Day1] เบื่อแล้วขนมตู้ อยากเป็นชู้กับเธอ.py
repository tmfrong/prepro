"""[Onsite Day1] เบื่อแล้วขนมตู้ อยากเป็นชู้กับเธอ"""
def main():
    """print [Onsite Day1] เบื่อแล้วขนมตู้ อยากเป็นชู้กับเธอ"""
    money = int(input())
    water = int(input())
    num_snack1 = int(input())
    num_snack2 = int(input())
    num_snack3 = int(input())
    moneyforsnack1 = money - water
    modmoneyforsnack = (money - water)%3
    if modmoneyforsnack == 0 and moneyforsnack1 >= 10:
        snack1 = num_snack1*10
        print("Snack number 1:%d" %snack1) 
    elif modmoneyforsnack == 1 and moneyforsnack1 >= 15:
        snack1 = num_snack1*15
        print("Snack number 1:%d" %snack1) 
    elif modmoneyforsnack == 2 and moneyforsnack1 >= 20:
        snack1 = num_snack1*20
        print("Snack number 1:%d" %snack1) 
    else:
        print("You don’t have enough money!")
        
    moneyforsnack2 = moneyforsnack1 - snack1
    modmoneyforsnack2 = moneyforsnack2%3
    if modmoneyforsnack2 == 0 and moneyforsnack2 >= 12:
        snack2 = num_snack2*12
        print("Snack number 2:%d" %snack2) 
    elif modmoneyforsnack2 == 1 and moneyforsnack2 >= 15:
        snack2 = num_snack2*15
        print("Snack number 2:%d" %snack2) 
    elif modmoneyforsnack2 == 2 and moneyforsnack2 >= 18:
        snack2 = num_snack2*18
        print("Snack number 2:%d" %snack2) 
    else:
        print("You don’t have enough money!")
        
    moneyforsnack3 = moneyforsnack2 - snack2 - snack1
    modmoneyforsnack3 = moneyforsnack3%3
    if modmoneyforsnack3 == 0 and moneyforsnack3 >= 5:
        snack3 = num_snack3*5
        print("Snack number 3:%d" %snack3) 
    elif modmoneyforsnack3 == 1 and moneyforsnack3 >= 7:
        snack3 = num_snack3*7
        print("Snack number 3:%d" %snack3) 
    elif modmoneyforsnack3 == 2 and moneyforsnack3 >= 9:
        snack3 = num_snack3*9
        print("Snack number 3:%d" %snack3) 
    else:
        print("You don’t have enough money!")
main()
