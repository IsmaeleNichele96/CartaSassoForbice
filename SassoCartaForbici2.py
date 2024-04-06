#altra implementazione 
# 0 sasso
# 1 carta
# 2 forbice
import random
r = random.randint(0,2)
human_score = 0
pc_score = 0

labels = ["Sasso", "Carta", "Forbice"]
game = True 

game_matrix = [
    #       C0  C1  C2
    # P0    p   c   g 
    # P1    g   p   c
    # P2    c   g   p
    ["pari", "computer", "player"],
    ["player", "pari", "computer"],
    ["computer", "player", "pari"]
]
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
        if game_matrix[user][computer] == "computer":
            pc_score += 1
            print(f"Vince -> {game_matrix[user][computer]}")
            print(f"Player = {human_score} \t Computer = {pc_score}")
        elif game_matrix[user][computer] == "player":
            human_score += 1
            print(f"Vince -> {game_matrix[user][computer]}")
            print(f"Player = {human_score} \t Computer = {pc_score}")
        else:
            print("Pareggio")
            print(f"Player = {human_score} \t Computer = {pc_score}")
            
    

    else:
        print("Input non valido")