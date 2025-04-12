
contacts={}

def add_contact():
    name=input("enter name: ")
    phone=input("enter your number: ")
    email=input("enter your email: ")
    if name in contacts:
        print("This contact already exists.")
    else:
        contacts[name]=phone
        contacts[name]=email
        print("contact added successfully")
def delete_contact():
    name =input("enter name: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfuly")
    else:
        print("This contact does not exist")
def update_contact():
    name=input("enter name: ")
    for contact in contacts:
        if(contact==name):
            phone= input("enter the new phone number: ")
            contacts[name]=phone
            email=input("enter the email: ")
            contacts[name]=email
            print("contact updated successfully")
            break
        else:
            print("This contact does not exist")
def search_contact():
    name=input("enter name: ")
    for contact in contacts:
        if contact.lower()==name.lower():
            print("contact found")
            print(contact,contacts[contact])
            break
        else:
            print("contact not found")
def display_contact():
    if contacts=={}:
        print("There are no contacts")
    else:
        print("Contact list: ")
        for name,phone,email in contacts.items():
            print(name,phone,email)
while True:
    print("\nContact Book Menu: ")
    print("1. Add contact")
    print("2. Delete Contact")
    print("3. Update Contact")
    print("4. Search Contact")
    print("5. Display Contact")
    print("6. Exit")

choice=int(input("enter your choice(1-6): "))
if choice=='1':
    add-contact()
elif choice=='2':
    delete_contact()
elif choice=='3':
    update_contact()
elif choice=='4':
    search_contact()
elif choice=='5':
    display_contact()
elif choice=='6':
    print("Exiting Contact Book. Bye Bye!")
    break
else:
    print("INVALID CHOICE")