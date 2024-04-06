# 0 sasso
# 1 carta
# 2 forbice
import random
r = random.randint(0,2)
human_score = 0
pc_score = 0

labels = ["Sasso", "Carta", "Forbice"]
game = True
while game:
    print("0 - Sasso")
    print("1 - Carta")
    print("2 - Forbice")
    print("3 - Resetta i punteggi")
    print("4 - Termina il gioco")

    user_input = input("\nCosa vuoi fare?\n")
    
    if user_input == "4":
        print("Gioco terminato")
        print(f"Umano: {human_score} \t Computer: {pc_score}")
        game = False
    elif user_input == "3":
        human_score = 0
        pc_score = 0
        print("Punteggio resettato")
        print(f"Umano: {human_score} \t Computer: {pc_score}")
    elif int(user_input) in range(0, 3):
        print("HERE GAME")
        computer = random.randint(0, 2)
        user = int(user_input)
        print(f"{labels[user]} vs. {labels[computer]}")
        if computer == user:
            print("Pareggio")
            print(f"Umano: {human_score} \t Computer: {pc_score}")
            #specifico i casi in cui vince il pc
        elif computer == 0 and user == 2 or computer ==1 and user == 0 or computer ==2 and user == 1:
            print("Computer vince")
            pc_score += 1
            print(f"Umano: {human_score} \t Computer: {pc_score}")
        else:
            print("Umano vince")
            human_score += 1
            print(f"Umano: {human_score} \t Computer: {pc_score}")
    else:
        print("Input non valido")