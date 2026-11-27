import time

def show_menu():
          print("---fantasy winkel---")
          print("1. Buy Sword (50 gold)")
          print("2. Buy Shield (40 gold)")
          print("3. Buy Potion (20 gold)")
          print("4. Buy Bow (60 gold)")
          print("5. View Inventory")
          print("6. Exit Shop")

def show_inventory(inventory):
            print("Your inventory:")
            for item in inventory:
                print(f"- {item}")

def can_buy(player_gold, price):
    if player_gold >= price:
          return True
    else: 
          return False

def buy_item(player_gold, inventory, item_name, price):
    if can_buy(player_gold, price):
        player_gold -= price
        inventory.append(item_name)
        print(f"You bought the {item_name} and now have {player_gold} gold.")
    return player_gold



    

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
    show_menu()

    antwoord = input("what would u like to do? ")

    if antwoord == "buy sword":
        if can_buy(player_gold, 50):
            player_gold = buy_item(player_gold, inventory, "sword", 50)
            time.sleep(2)
        else:
             print(f"je hebt niet genoeg geld")
    elif antwoord == "buy shield":
         if can_buy(player_gold, 40):
                    player_gold = buy_item(player_gold, inventory, "shield", 40)
                    time.sleep(2)
         else:
               print(f"je hebt niet genoeg geld")
    elif antwoord == "buy potion":
        if can_buy(player_gold, 20):
                player_gold = buy_item(player_gold, inventory, "potion", 20)
                time.sleep(2)
        else:
                 print(f"je hebt niet genoeg geld")
    elif antwoord == "buy bow":
        if can_buy(player_gold, 60):
                player_gold = buy_item(player_gold, inventory, "bow", 60)
                time.sleep(2)
        else:
                 print(f"je hebt niet genoeg geld")
    elif antwoord == "view inventory":
         show_inventory(inventory)   
         time.sleep(2)  

    elif antwoord == "exit shop":
        in_store = False
        print(f"have a nice day {player_name}, u heeft {player_gold} gold over")





