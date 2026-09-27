fighters = []

def create_fighter(fighters):
    name = input("\nFighter name: ")
    age = int(input("Age: "))
    weight = float(input("Weight(kg): "))
    
    fighter = {
        "name": name,
        "age": age,
        "weight": weight
    }
    
    fighters.append(fighter)        
    print("\nFighter created successfully!")
    print(f"\n{fighter['name']} \n{fighter['age']} years old \n{fighter['weight']} kg")

def list_fighters():
    if not fighters:
        print("\nNo fighter registered")
    else:
        for fighter in fighters:
            print(
                f"{fighter['name']} | "
                f"{fighter['age']} years old | "
                f"{fighter['weight']} kg"
            )

def search_fighters():
    search = input("Fighter's name: ").casefold()
    
    matches = []
    
    for fighter in fighters:
        if search in fighter["name"].casefold():
            matches.append(fighter)
    
    if not matches:
        print("Fighter not found")
    else:
        print("\nFighters found:")
        for fighter in matches:
            print(
                f"{fighter['name']} | "
                f"{fighter['age']} years old | "
                f"{fighter['weight']} kg"
            )    

def view_stats():
    print("View fighter stats")

def edit_fighter():
    search = input("Fighter's name: ").casefold()
               
    found = False
    
    for fighter in fighters:
        if fighter["name"].casefold() == search:
            print("\nFighter found!.\n")
    
            new_age = input(
                f"Age [{fighter['age']}] | New age: "
            )
    
            new_weight = input(
                f"Weight [{fighter['weight']}] | New weight: "
            )
    
            if new_age != "":
                fighter["age"] = int(new_age)
    
            if new_weight != "":
                fighter["weight"] = float(new_weight)
    
            print("\nFighter updated successfully!")
            found = True
            break
    
    if not found:
        print("\nFighter not found.")

while True:
    print("=" * 30 )
    print("      MMA FIGHTER MANAGER")
    print("=" * 30)
    print("\n1. Create fighter " \
    "\n2. List fighters " \
    "\n3. Search fighters " \
    "\n4. View fighter stats " \
    "\n5. Edit fighter " \
    "\n6. Exit")

    try:
        option = int(input("\nChoose an option: "))

        if option == 1:
           create_fighter(fighters)

        elif option == 2:
            list_fighters()

        elif option == 3:
            search_fighters()

        elif option == 4:
            view_stats()

        elif option == 5:
            edit_fighter()

        elif option == 6:
            break
        else: 
            print("Invalid option, choose one of the options")

    except ValueError:
        print("Invalid value")