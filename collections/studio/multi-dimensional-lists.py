food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.
food_cabinet = (sorted(food.split(','))) 
equipment_cabinet = sorted(equipment.split(','))
pets_cabinet = sorted(pets.split(','))
sleep_cabinet = sorted(sleep_aids.split(','))


# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.
#cargo_hold = []
#cargo_hold += food_cabinet, equipment_cabinet, pets_cabinet, sleep_cabinet
cargo_hold = [food_cabinet,equipment_cabinet,pets_cabinet,sleep_cabinet]
print(cargo_hold)


# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.
cabinet_index  = int(input('Select a cabinet 0-3:'))
print(f'Selected cabinet: {cargo_hold[cabinet_index ]}')


# d) Use bracket notation and format to display the contents of the selected cabinet. If the user entered an invalid number, print an error message.
if 0 <= cabinet_index < len(cargo_hold):
    print(f"Cabinet {cabinet_index} contains: {cargo_hold[cabinet_index]}")
else:
    print("Invalid cabinet number.")


# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. Use the in method to check if the cabinet contains the selected item, then print “Cabinet ____ DOES/DOES NOT contain ____.”
item = input("Enter an item: ")
if 0 <= cabinet_index < len(cargo_hold):
    if item in cargo_hold[cabinet_index]:
        print(f"Cabinet {cabinet_index} DOES contain {item}.")
    else:
        print(f"Cabinet {cabinet_index} DOES NOT contain {item}.")

    