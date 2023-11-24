from csv import writer, reader
from typing import Mapping

def add_contact() -> None:
    contacts_list: list[list[str]] = list()
    contacts_dict: Mapping[str, str] | None = None

    with open('contacts.csv', 'r') as phonebook:
        csvreader = reader(phonebook)
        for row in csvreader:
            contacts_list.append(row)
        phonebook.close()
        contacts_list.sort()
        contacts_dict = dict(contacts_list)

    print("\nAdding Contact to Phonebook...")
    contact_name: str = input("\tAdd Contact Name: ").strip()

    if contact_name not in contacts_dict.keys():
        contact_number: str = input("\tAdd Contact Number: ").strip()
        contacts_list.append([contact_name, contact_number])
        contacts_list.sort()

    with open('contacts.csv', 'w', newline='') as phonebook:
        writer(phonebook).writerows(contacts_list)
        phonebook.close()
