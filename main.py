from random import randint
from sys import exit

possible_wall_colours = [
    "white", "light grey", "grey", "black",
    "brown", "red", "orange", "yellow",
    "lime", "green", "cyan", "light blue",
    "blue", "purple", "magenta", "pink"]

possible_nationalities = [
    "Afghan", "Algerian,", "Angolan", "Argentine",
    "Austrian,", "Australian", "Bangladeshi", "Belarusian",
    "Belgian", "Bolivian", "Bosnian", "Brazilian",
    "Bulgarian", "Cambodian", "Cameroonian", "Canadian",
    "Central African", "Chadian", "Chinese person", "Colombian",
    "Costa Rican", "Croat", "Czech person", "Congolese person",
    "Dane", "Ecuadorian", "Egyptian", "Salvadoran",
    "English person", "Estonian", "Ethiopian", "Finn",
    "French person", "German", "Ghanaian", "Greek",
    "Guatamalan", "Dutch person", "Honduran", "Hungarian",
    "Icelander", "Indian", "Indonesian", "Iranian",
    "Iraqi", "Irish person", "Israeli", "Italian",
    "Ivorian", "Jamacian", "Japanese person", "Jordinian",
    "Kazakhstani", "Kenyan", "Laotian", "Latvian",
    "Libyan", "Lithuanian", "Malagasy", "Malaysian",
    "Malian", "Mauritanian", "Mexican", "Moroccan",
    "Namibian", "New Zealander", "Nicaraguan", "Nigerian",
    "Norwegian", "Omani", "Pakistani", "Panamanian",
    "Paraguayan", "Peruvian", "Filipino", "Pole",
    "Portugese person", "Romanian", "Russian", "Saudi",
    "Scot", "Senegalese person", "Serbian", "Singaporean",
    "Slovak", "Somalian", "South African", "Spaniard",
    "Sudanese person", "Swede", "Swiss person", "Syrian",
    "Thai person", "Tunisian", "Turk", "Turkmen",
    "Ukranian", "Emirati", "American", "Uruguayan",
    "Vietnamese person", "Welsh person", "Zambian", "Zimbabwean"]

possible_foods = [
    "chicken", "cheese", "tomatoes", "rice",
    "eggs", "apples", "kiwis", "broccoli",
    "spinach", "nuts", "pork", "chocolate",
    "pasta", "bananas", "bread", "potatoes"]

possible_beverages = [
    "energy drinks", "wine", "sports drinks", "orange juice",
    "tea", "milk", "beer", "cider",
    "coffee", "water", "cola", "whiskey",
    "apple juice", "pineapple juice", "cranberry juice", "peach juice"]

possible_pets = [
    "fish", "cats", "dogs", "parrots",
    "budgies", "finches", "cockatiels", "horses",
    "snakes", "lizards", "rabits", "hamsters",
    "guinea pigs", "mice", "rats", "gerbils"]

def generate_random_index(end_index):
    return randint(0, end_index)

def pick_items(item_type):
    if item_type == "wall_colours":
        used_indeces = []
        wall_colours = []
        count = 0
        
        while count < 5:
            random_index = generate_random_index(len(possible_wall_colours) - 1)
            if random_index not in used_indeces:
                wall_colours.append(possible_wall_colours[random_index])
                used_indeces.append(random_index)
                count += 1
        
        return wall_colours
    
    if item_type == "nationalities":
        used_indeces = []
        nationalities = []
        count = 0
        
        while count < 5:
            random_index = generate_random_index(len(possible_nationalities) - 1)
            if random_index not in used_indeces:
                nationalities.append(possible_nationalities[random_index])
                used_indeces.append(random_index)
                count += 1
        
        return nationalities
    
    if item_type == "foods":
        used_indeces = []
        foods = []
        count = 0
        
        while count < 5:
            random_index = generate_random_index(len(possible_foods) - 1)
            if random_index not in used_indeces:
                foods.append(possible_foods[random_index])
                used_indeces.append(random_index)
                count += 1
        
        return foods
    
    if item_type == "beverages":
        used_indeces = []
        beverages = []
        count = 0
        
        while count < 5:
            random_index = generate_random_index(len(possible_beverages) - 1)
            if random_index not in used_indeces:
                beverages.append(possible_beverages[random_index])
                used_indeces.append(random_index)
                count += 1
        
        return beverages
    
    if item_type == "pets":
        used_indeces = []
        pets = []
        count = 0
        
        while count < 5:
            random_index = generate_random_index(len(possible_pets) - 1)
            if random_index not in used_indeces:
                pets.append(possible_pets[random_index])
                used_indeces.append(random_index)
                count += 1
        
        return pets
    

 
wall_colours = pick_items("wall_colours")
nationalities = pick_items("nationalities")
foods = pick_items("foods")
beverages = pick_items("beverages")
pets = pick_items("pets")


house1 = {
    "Wall Colour": wall_colours[0],
    "Nationality": nationalities[0],
    "Food": foods[0],
    "Beverage": beverages[0],
    "Pet": pets[0]}

house2 = {
    "Wall Colour": wall_colours[1],
    "Nationality": nationalities[1],
    "Food": foods[1],
    "Beverage": beverages[1],
    "Pet": pets[1]}

house3 = {
    "Wall Colour": wall_colours[2],
    "Nationality": nationalities[2],
    "Food": foods[2],
    "Beverage": beverages[2],
    "Pet": pets[2]}

house4 = {
    "Wall Colour": wall_colours[3],
    "Nationality": nationalities[3],
    "Food": foods[3],
    "Beverage": beverages[3],
    "Pet": pets[3]}

house5 = {
    "Wall Colour": wall_colours[4],
    "Nationality": nationalities[4],
    "Food": foods[4],
    "Beverage": beverages[4],
    "Pet": pets[4]}

print(f"Can you figure out who keeps {house4['Pet']}?\n\n")

print(f"""The {house3["Nationality"]} lives in the {house3["Wall Colour"]} house
The {house5["Nationality"]} keeps {house5["Pet"]} as pets
The {house2["Nationality"]} drinks {house5["Beverage"]}
The {house4["Wall Colour"]} house is on the left of the {house5["Wall Colour"]} house
The {house4["Wall Colour"]} house's owner drinks {house4["Beverage"]}
The person who doesn't eat {house3["Food"]} keeps {house3["Pet"]}
The owner of the {house1["Wall Colour"]} house doesn't eat {house1["Food"]}
The person living in the centre house drinks {house3["Beverage"]}
The {house1["Nationality"]} lives in the first house
The man who doensn't eat {house2["Food"]} lives next to the one who keeps {house1["Pet"]}
The man who keeps {house2["Pet"]} lives next to the man who doesn't eat {house1["Food"]}
The owner who doesn't eat {house5["Food"]} drinks {house5["Beverage"]}
The {house4["Nationality"]} doesn't eat {house4["Food"]}
The {house1["Nationality"]} lives next to the {house2["Wall Colour"]} house
The man who doesn't eat {house2["Food"]} has a neighbor who drinks {house1["Beverage"]}
""")

while True:
    command = input("Enter 's' for solution or 'q' for quit > ")

    if command.lower() == "s":
        print(f"""House 1:
> Wall Colour: {house1["Wall Colour"]}
> Nationality: {house1["Nationality"]}
> Food: {house1["Food"]}
> Beverage: {house1["Beverage"]}
> Pet: {house1["Pet"]}

House 2:
> Wall Colour: {house2["Wall Colour"]}
> Nationality: {house2["Nationality"]}
> Food: {house2["Food"]}
> Beverage: {house2["Beverage"]}
> Pet: {house2["Pet"]}

House 3:
> Wall Colour: {house3["Wall Colour"]}
> Nationality: {house3["Nationality"]}
> Food: {house3["Food"]}
> Beverage: {house3["Beverage"]}
> Pet: {house3["Pet"]}

House 4:
> Wall Colour: {house4["Wall Colour"]}
> Nationality: {house4["Nationality"]}
> Food: {house4["Food"]}
> Beverage: {house4["Beverage"]}
> Pet: {house4["Pet"]}

House 5:
> Wall Colour: {house5["Wall Colour"]}
> Nationality: {house5["Nationality"]}
> Food: {house5["Food"]}
> Beverage: {house5["Beverage"]}
> Pet: {house5["Pet"]}""")
        break

    if command.lower() == "q":
        exit()
