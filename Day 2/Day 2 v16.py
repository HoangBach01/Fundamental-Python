# Viet chuong trinh choi keo bua bao
# Tao list Keo Bua Bao
print("Welcome to One - Two - Three Game!")
game = ['scissors', 'rock', 'paper']
game_index = [1,2,3]

# Tao nguoi choi 1,2
cont_game = '1'
while cont_game == '1' :
    n1 = 0
    while n1 not in game_index:
        n1 = eval(input("Person 1 decision (1: scissors or 2: rock or 3: paper):  "))

    n2 = 0
    while n2 not in game_index:
        n2 = eval(input("Person 2 decision (1: scissors or 2: rock or 3: paper):  "))


    # Tim nguoi thang
    if game[n1-1] == game[n2-1]:
        print("Person 1 = Person 2")
        cont_game = input("Do you want to continue other game (1: Yes or 0: No): ")
    elif (game[n1-1] == game[0] and game[n2-1] == game[2]) or (game[n1-1] == game[1] and game[n2-1] == game[0]) or (game[n1-1] == game[2] and game[n2-1] == game[1]):
        print("Person 1 win!")
        cont_game = input("Do you want to continue other game (1: Yes or 0: No): ")
    else:
        print("Person 2 win!")
        cont_game = input("Do you want to continue other game (1: Yes or 0: No): ")

print("Thank you, have a good day!")

