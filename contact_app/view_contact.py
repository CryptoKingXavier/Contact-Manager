from csv import reader

def show_contacts() -> None:
    # Info: To display all contacts
    contacts_list: list[list[str]] = list()

    with open('contacts.csv', 'r') as phonebook:
        csvreader = reader(phonebook)
        for row in csvreader:
            contacts_list.append(row)
        phonebook.close()
        contacts_list.sort()

        for contact in contacts_list:
            print(f"\tName: {contact[0]} - Phone Number: {contact[1]}", end="\n")

def show_contact() -> None:
    # Info: To display a single contact
    contacts_list: list[list[str]] = list()

    with open('contacts.csv', 'r') as phonebook:
        csvreader = reader(phonebook)
        for row in csvreader:
            contacts_list.append(row)
        phonebook.close()

        contact_name: str = input('Enter Contact Name: ').strip()

        for contact in contacts_list:
            if contact_name in contact:
                print(f"\tName: {contact[0]} - Phone Number: {contact[1]}", end="\n")
