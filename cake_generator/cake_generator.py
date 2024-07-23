import progressbar
import emoji
import time
import json
import random
from googlesearch import search

#####
class Cake:
    def __init__(self, base_layer_type, base_layer_flavor, middle_layer, middle_layer_flavor, top_layer, top_layer_flavor, topping):
        self.base_layer_type = base_layer_type
        self.base_layer_flavor = base_layer_flavor
        self.middle_layer_type = middle_layer
        self.middle_layer_flavor = middle_layer_flavor
        self.top_layer_type = top_layer
        self.top_layer_flavor = top_layer_flavor
        self.topping = topping
    
    def to_dict(self):
        return {
            "base_layer_type": self.base_layer_type,
            "base_layer_flavor": self.base_layer_flavor,
            "middle_layer_type": self.middle_layer_type,
            "middle_layer_flavor": self.middle_layer_flavor,
            "top_layer_type": self.top_layer_type,
            "top_layer_flavor": self.top_layer_flavor,
            "topping": self.topping
        }

    @staticmethod
    def from_dict(data):
        return Cake(
            data["base_layer_type"],
            data["base_layer_flavor"],
            data["middle_layer_type"],
            data["middle_layer_flavor"],
            data["top_layer_type"],
            data["top_layer_flavor"],
            data["topping"]
        )

# Show the dummy loading info
def animated_marker():
    widgets = ['Loading: ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()
        
    for i in range(20):
        time.sleep(0.1)
        bar.update(i)

# Generate a cake
def generate_a_cake():
    available_cake_parts = {
        "base_layer_types": ["Spongecake", "Choux pastry", "Cupcake", "Yeast cake", "Shortbread"],
        "base_layer_flavors": ["Vanilla", "Cocoa", "Coffee"],
        "middle_layer_types": ["Cold cheesecake", "Cheesecake", "Pudding", "Fruit pudding", "Whipped cream", "Jellied fruits"],
        "middle_layer_flavors": ["Vanilla", "Strawberry", "Coconut", "Chocolate", "Coffee"],
        "top_layer_types": ["Jello", "Icing"],
        "top_layer_flavors": ["Fruit", "Chocolate", "Caramel"],
        "topping_types":["Fresh fruits", "Sugar sprinkles", "Chocolate chips", "Crumble"]
    }

    base_layer_type = random.choice(available_cake_parts["base_layer_types"])
    base_layer_flavor = random.choice(available_cake_parts["base_layer_flavors"])
    middle_layer_type = random.choice(available_cake_parts["middle_layer_types"])
    middle_layer_flavor = random.choice(available_cake_parts["middle_layer_flavors"])
    top_layer_type = random.choice(available_cake_parts["top_layer_types"])
    top_layer_flavor = random.choice(available_cake_parts["top_layer_flavors"])
    topping = random.choice(available_cake_parts["topping_types"])

    cake = Cake(base_layer_type, base_layer_flavor, middle_layer_type, middle_layer_flavor, top_layer_type, top_layer_flavor, topping)
    return cake

# Print a nicely formatted cake idea
def describe_a_cake(cake):
    print(f"""\n
    Here's your cake:

    Base layer: {cake.base_layer_type} with the {cake.base_layer_flavor.lower()} flavor.
    Middle layer: {cake.middle_layer_type} with the {cake.middle_layer_flavor.lower()} flavor.
    Top layer: {cake.top_layer_type} with the {cake.top_layer_flavor.lower()} flavor.
    Finally, add {cake.topping.lower()} on the top of your cake.
    \n
    """)

# Print the main menu
def print_main_menu():
    main_options = ["[G]enerate a new cake", "[B]rowse previously generated cakes", "[A]dd new cake components", "[Q]uit"]
    print("\nWelcome to the \"Cake Generator\"! What would you like to do?\n")
    print(*main_options, sep="\n")

def save_cake(cake):
    with open("data/historic_cakes.json", "a") as database:
        json.dump(cake.to_dict(), database)
        database.write("\n")

shortcake_emoji = "\U0001F370"

while True:
    print_main_menu()
    option = input("Please enter your choice: \n").lower()
    if not option:
        print("Invalid option. Please try again.\n")
        continue
    elif option == "g":
        print(f"Be patient, your cake is being generated {shortcake_emoji}\n")
        animated_marker()
        cake = generate_a_cake()
        describe_a_cake(cake)
        save_cake(cake)
        print("""Do you need to look for a recipe for a component of the cake?\n
              [Y]es/[N]o\n""")
        answer = input().lower()
        if answer == "y":
            print("""Choose the component you want to look for:
                  [B]ase layer
                  [M]iddle layer
                  [T]op layer
                  T[o]pping\n""")
            answer = input().lower()
            if answer == "b":
                query = f"{cake.base_layer_flavor.lower() + ' ' + cake.base_layer_type.lower() + ' ' + 'recipe'}"
                print(f"Looking for the {query}s\n")
                animated_marker()
                for j in search(query, tld="co.in", num=3, start=0, stop=3, pause=2):
                    print(j)
            elif answer == "m":
                query = f"{cake.middle_layer_flavor.lower() + ' ' + cake.middle_layer_type.lower() + ' ' + 'recipe'}"
                print(f"Looking for the {query}s\n")
                animated_marker()
                for j in search(query, tld="co.in", num=3, start=0, stop=3, pause=2):
                    print(j)
            elif answer == "t":
                query = f"{cake.top_layer_flavor.lower() + ' ' + cake.top_layer_type.lower() + ' ' + 'recipe'}"
                print(f"Looking for the {query}s\n")
                animated_marker()
                for j in search(query, tld="co.in", num=3, start=0, stop=3, pause=2):
                    print(j)
            elif answer == "o":
                query = f"{cake.topping.lower() + ' ' + 'recipe'}"
                print(f"Looking for the {query}s\n")
                animated_marker()
                for j in search(query, tld="co.in", num=3, start=0, stop=3, pause=2):
                    print(j)
        elif answer == "n":
            print("Okey dokey, happy baking! See you next time!\n")
            continue
    elif option == "b":
        print("Not yet implemented")
    elif option == "a":
        print("Not yet implemented")
    elif option == "q":
        quit("See you next time!")
