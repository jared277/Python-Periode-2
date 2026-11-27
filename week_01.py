import time


print("Hello Periode 2!")


player_name = input("enter your name: ")
print(f"hello {player_name}")

player_gold = 100
inventory = []

print(f"welkom {player_name} u have {player_gold} gold.")

winkel_voorraad = [
    {"id": 1, "naam":"sword", "price": 50},
    {"id": 2, "naam":"shield", "price": 40},
    {"id": 3, "naam":"potion", "price": 20},
    {"id": 4, "naam":"bow", "price": 60},
]



in_store = True

while in_store:
    print("---fantasy winkel---")
    print("1. Buy Sword (50 gold)")
    print("2. Buy Shield (40 gold)")
    print("3. Buy Potion (20 gold)")
    print("4. Buy Bow (60 gold)")
    print("5. View Inventory")
    print("6. Exit Shop")

    antwoord = input("what would u like to do? ")

    if antwoord == "buy sword":
        if player_gold >= 50:
            player_gold -= 50
            print(f"jij hebt een zwaard gekocht en hebt nu {player_gold} gold")
            inventory.append("sword")
            time.sleep(2)
        else:
             print(f"je hebt niet genoeg geld")
    elif antwoord == "buy shield":
        if player_gold >= 40:
            player_gold -= 40
            print(f"jij hebt een shield gekocht en hebt nu {player_gold} gold")
            inventory.append("shield")
            time.sleep(2)
        else:
               print(f"je hebt niet genoeg geld")
    elif antwoord == "buy potion":
        if player_gold >= 20:
                player_gold -= 20
                print(f"jij hebt een potion gekocht en hebt nu {player_gold} gold")
                inventory.append("potion")
                time.sleep(2) 
        else:
                 print(f"je hebt niet genoeg geld")
    elif antwoord == "buy bow":
        if player_gold >= 60:
                player_gold -= 60
                print(f"jij hebt een bow gekocht en hebt nu {player_gold} gold") 
                inventory.append("bow")
                time.sleep(2)
        else:
                 print(f"je hebt niet genoeg geld")
    elif antwoord == "view inventory":
         print(f"{inventory}")   
         time.sleep(2)  

    elif antwoord == "exit shop":
        in_store = False
        print(f"have a nice day {player_name}, u heeft {player_gold} gold over")





