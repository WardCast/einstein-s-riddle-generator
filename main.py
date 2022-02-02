from random import randint

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
    
    

house1 = {
    "Wall Colour": pick_items("wall_colours")[0],
    "Nationality": pick_items("nationalities")[0],
    "Food": pick_items("foods")[0],
    "Beverage": pick_items("beverages")[0],
    "Pet": pick_items("pets")[0]}

house2 = {
    "Wall Colour": pick_items("wall_colours")[1],
    "Nationality": pick_items("nationalities")[1],
    "Food": pick_items("foods")[1],
    "Beverage": pick_items("beverages")[1],
    "Pet": pick_items("pets")[1]}

house3 = {
    "Wall Colour": pick_items("wall_colours")[2],
    "Nationality": pick_items("nationalities")[2],
    "Food": pick_items("foods")[2],
    "Beverage": pick_items("beverages")[2],
    "Pet": pick_items("pets")[2]}

house4 = {
    "Wall Colour": pick_items("wall_colours")[3],
    "Nationality": pick_items("nationalities")[3],
    "Food": pick_items("foods")[3],
    "Beverage": pick_items("beverages")[3],
    "Pet": pick_items("pets")[3]}

house5 = {
    "Wall Colour": pick_items("wall_colours")[4],
    "Nationality": pick_items("nationalities")[4],
    "Food": pick_items("foods")[4],
    "Beverage": pick_items("beverages")[4],
    "Pet": pick_items("pets")[4]}

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
The owner who smokes {house5["Food"]} drinks {house5["Beverage"]}
The {house4["Nationality"]} doesn't eat {house4["Food"]}
The {house1["Nationality"]} lives next to the {house2["Wall Colour"]} house
The man who doesn't eat {house2["Food"]} has a neighbor who drinks {house1["Beverage"]}
""")