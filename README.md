# SPACE ALLOCATOR
The Space allocator is a python based Command Line Interface that can be used to allocate Office space and Living Space to Fellows and Staff that join Andela.  

## Problem Description

When a new Fellow joins Andela they are assigned an office space and an optional living space if they choose to opt in. When a new Staff joins they are assigned an office space only. This SPACE ALLOCATOR APP digitizes and randomizes a room allocation system for one of the Andela Keya' facilities called the Dojo. It enables the creation of rooms, adding people to the systems and alllocating them to random rooms where need be.

## Requirements

Python version 3.5
Python virtualenv
SQLite3
Setup

## Installation
1. Clone this repository 
> $ git clone https://github.com/peninah-anyango/allocator.git
2. Navigate to the ** allocator directory **
> $ cd allocator
3. Create virtual environment
4. Install the required packages
> $ pip install -r requirements.txt
5. Run the app in interactive mode
> $ python dojo_cli.py --i

## Usage
* create_room <room_type> <room_name> : Creates a new room.
* add_person <first_name> <last_name> <title> [<needs_accomodation>] : Adds a new person and allocates a random room.
* print_room <room_name>: Prints occupants in a specified name.
* reallocate_person <name> <new_room>: Moves a person from one room to another.
* load_people <filename>: Does batch addition of people using data from a filename.txt
* print_allocations [<filename>]: Prints all rooms and the people in them and optionally writes the data to filename.txt.
* print_unallocated [<filename>]: Prints all the people that haven't been allocated and optionally writes the data to filename.txt.
* load_state [<filename>]: Loads data from the specified SQLite db into the app
* save_state [<db_name>]: Persists data stored in the app to a SQLite DB

## Task list
- [x] create_room
- [x] add_person
- [ ] print_room
- [ ] reallocate_person
- [ ] load_people
- [ ] print_allocations
- [ ] print_unallocated
- [ ] load_state
- [ ] save_state

## Tests

Run nosetests 

## License
The MIT 

