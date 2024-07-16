import json
import random
class Cake:
    def __init__(self, base_layer_type, base_layer_flavor, middle_layer, middle_layer_flavor, top_layer, top_layer_flavor, toppings):
        self.base_layer_type = base_layer_type
        self.base_layer_flavor = base_layer_flavor
        self.middle_layer_type = middle_layer
        self.middle_layer_flavor = middle_layer_flavor
        self.top_layer_type = top_layer
        self.top_layer_flavor = top_layer_flavor
        self.toppings = toppings


def generate_a_cake():

    base_layer_types = ["Spongecake", "Choux pastry", "Cupcake", "Yeast cake", "Shortbread"]
    base_layer_flavors = ["Vanilla", "Cocoa", "Coffee"]
    middle_layer_types = ["Cold cheesecake", "Cheesecake", "Pudding", "Fruit pudding", "Whipped cream", "Jellied fruits"]
    middle_layer_flavors = ["Vanilla", "Strawberry", "Coconut", "Chocolate", "Coffee"]
    top_layer_types = ["Jello", "Icing"]
    top_layer_flavors = ["Fruit", "Chocolate", "Caramel"]
    topping_types = ["Fresh fruits", "Sprinkles", "Chocolate chips", "Crumble"]

    base_layer_type = random.choice(base_layer_types)
    base_layer_flavor = random.choice(base_layer_flavors)
    middle_layer_type = random.choice(middle_layer_types)
    middle_layer_flavor = random.choice(middle_layer_flavors)
    top_layer_type = random.choice(top_layer_types)
    top_layer_flavor = random.choice(top_layer_flavors)
    topping = random.choice(topping_types)
    cake = Cake(base_layer_type, base_layer_flavor, middle_layer_type, middle_layer_flavor, top_layer_type, top_layer_flavor, topping)

    return cake

cake = generate_a_cake()
print(f"""Here is your cake:

Base layer: {cake.base_layer_type}
Base layer flavor: {cake.base_layer_flavor}
Middle layer: {cake.middle_layer_type}
Middle layer flavor: {cake.middle_layer_flavor}
Top layer: {cake.top_layer_type}
Top layer flavor: {cake.top_layer_flavor}
Toppings: {cake.toppings}""")
