import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)  # Return the loaded data
    except FileNotFoundError:  # Handle empty or malformed files
        return []  # Return an empty list in case of an error


# helper method.
def save_data_helper(viedos):
    with open('youtube.txt', 'w') as file:
        json.dump(viedos, file) # dump me write data it in 2 thing 1- what to write 2- where to write.

def list_all_viedos(viedos):
    print("\n")
    print("-" * 70)
    for index, viedo in enumerate(viedos, start=1):
        print(f"{index}.{viedo['name']}, Duration {viedo['time']}")
    print("\n")
    print("-" * 70)

def add_viedo(viedos):
    name = input("Enter viedo name: ")
    time = input("Enter viedo duration: ")

    viedos.append({"name": name, "time": time})
    save_data_helper(viedos)


def update_viedo(viedos):
    list_all_viedos(viedos)
    index = int(input("Enter viedo Number to update: "))

    if 1 <= index <= len(viedos):
        name = input("Enter new viedo name: ")
        time = input("Enter new viedo time: ")

        # user started with index 1 but the actual index started at 0.
        viedos[index-1] = {"name": name, "time": time}
        save_data_helper(viedos)
    else:
        print("Invalid index selected")

def delete_viedo(viedos):
    list_all_viedos(viedos)

    index = int(input('Enter the viedo number to be deleted: '))

    if 1 <= index <= len(viedos):
        del  viedos[index-1]
        save_data_helper(viedos)
    else:
        print("Invalid index selected")

def main ():
    viedos = load_data()
    while True:
        print("\n Youtube Manager | choose an option")
        print("1. List all youtube viedos ")
        print("2. Add a youtube viedo ")
        print("3. Update a youtube viedo ")
        print("4. Delete a youtube viedo ")
        print("5. Exit the app")
        choice = input("Enter your choice: ")
        

        match choice:
            case "1":
                list_all_viedos(viedos)
            case "2":
                add_viedo(viedos)
            case "3":
                update_viedo(viedos)
            case "4":
                delete_viedo(viedos)
            case "5":
                break
            case _:
                print("Invalid Choice")

        

if __name__ == "__main__":
    main()