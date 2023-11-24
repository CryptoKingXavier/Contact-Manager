# Contact Manager Python Project

## Importing Required Libraries
    - from time import (
        sleep   # Delay execution for a given number of seconds
    )
    
    - from os import (
        system as sys   # Using command prompt command to clear terminal screen
    )

    - from typing import (
        Any,   # Any is compatible with every data type
        Mapping,   # Dictionary representation
        Generator,   # Generator[YieldType, SendType, ReturnType]
        Literal
    )

## ContactManager
    - object: The base class of the class hierarchy.

    - __init__ -> None:
        - contacts: Mapping[str, str]
            This is the dictionary representation of a phonebook
        - contact_keys: list[str]
            This holds all the names in the phonebook
        - contact_values: list[str]
            This holds all the numbers in the phonebook
        - contact_items: list[tuple[str, str]]
            This holds all info in a (name, number) format
        
## CRUD Functionality of ContactManager Project

### Create Functionality
    - add_contact -> None:
        This function is responsible for prompting users for a contact info to add to the phonebook

### Read Functionality

#### For all contacts
    - read_contacts -> Generator[tuple[str, str], Any, Literal['None'] | None]:
        This checks if the contacts is empty and utilizes the yield `generator` object to partially return each contact when needed while keeping track of the previous contact generated. This function should never be invoked.

    - show_contacts -> None:
        This works hand-in-hand with `read_contacts` to display the generated contact using the `iter-next` iterator object

#### For a single contact
    - read_contact -> Generator[tuple[str, str], Any, Literal['None'] | None]:
        This checks if the contacts is empty and queries the contacts dictionary to make a search based on either the name or number and then utilizes the yield `generator` object to partially return the contact when found. This function should never be invoked.

    - show_contact -> None:
        This works hand-in-hand with `read_contact` to display the generated contact using the `iter-next` iterator object

### Update Functionality

#### Updating Number
    - update_contact -> None:
        This queries the contacts dictionary to find a number match based on the given name and when found, changes the number with the newly given one.

#### Updating Name
    - update_contact -> None:
        This utilizes a reverse dictionary searching algorithm I developed to change the name based on finding a name match first and then chnaging it to a new name while maintaining the integrity of the number assigned to it.

### Delete Functionality
    - delete_contact -> None:
        This queries the contacts dictionary to find a name match and when found, deletes it from the dictionary memory.

##### Bonus Tip
    - sys('cls')   # On Windows, this clears the terminal screen
