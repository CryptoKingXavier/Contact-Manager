from csv import reader, writer
from typing import Mapping

def update_contact() -> None:
    # Info: To update a contact
    contacts_list: list[list[str]] = list()
    contacts_dict: Mapping[str, str] | None = None

    with open('contacts.csv', 'r') as phonebook:
        csvreader = reader(phonebook)
        for row in csvreader:
            contacts_list.append(row)
        phonebook.close()
        contacts_list.sort()
        contacts_dict = dict(contacts_list)

    state: str = input("1. Update Name - 2. Update Number: ")
    contact_name: str = input("\tContact Name: ").strip()
    if contact_name not in contacts_dict.keys():
        print("Contact Doesn't Exist!")
        return

    if state == '1':
        print("\nUpdating Contact Name in Phonebook...")
        for contact in contacts_list:
            if contact_name in contact:
                contact[0] = input(f"\t{contact_name}'s New Name: ").strip()
    if state == '2':
        print("\nUpdating Contact Number in Phonebook...")
        for contact in contacts_list:
            if contact_name in contact:
                contact[1] = input(f"\t{contact_name}'s New Number: ").strip()

    contacts_list.sort()

    with open('contacts.csv', 'w', newline='') as phonebook: 
        writer(phonebook).writerows(contacts_list)
        phonebook.close()
