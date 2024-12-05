import json


def add_contact():
    name = input("Name: ")
    age = input("Age: ")
    email = input("Mail: ")

    human = {"name": name, "age": age, "email": email}
    return human

def display_contact(population):
    for i, human in enumerate(population):
        print(i +1, "-", human["name"], "|", human["age"], "|", human["email"])


def delete_contact(population):
    display_contact(population)

    while True:
        contact = input("Delete Contact: ")
        try:
            contact = int(contact)
            if contact <=0 or contact > len(population):
                print("Invalid Contact Number")
            else:
                break
        except ValueError:
            print("Invalid input")
    population.pop(contact - 1)
    print("Contact Deleted")

def search_contact(population):
    search_name = input("Search Name: ").lower()
    result = []
    for human in population:
        name = human["name"]
        if search_name in name.lower():
            result.append(human)
    display_contact(result)

print("Contact Management")
print()

with open("contacts.json", "r") as f:
    population = json.load(f)["contacts"]

while True:
    print("Contact List Size:", len(population))
    crud = input("'Add', 'Delete', or 'Search', 'Exit': ")
    if crud == "Add":
        human = add_contact()
        population.append(human)
        print("Contact Added to the List")
    elif crud == "Delete":
        delete_contact(population)
    elif crud == "Search":
        search_contact(population)
    elif crud == "Exit":
        break
    else:
        print("Please provide a valid choice.")

with open("contacts.json", "w") as f:
    json.dump({"contacts": population}, f)