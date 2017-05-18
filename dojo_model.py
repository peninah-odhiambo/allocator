import random
from room_model import Room, Office, Livingspace
from people_model import Person, Staff, Fellow

spacer = " "


class Dojo (object):

    """ The Class Dojo is the main class that hold subclasses like Office, Living Space, Fellow, Staff """

    def __init__(self):
        self.rooms = []
        self.allocated_rooms = []
        self.unallocated_rooms = []
        self.offices = []
        self.allocated_offices = []
        self.unallocated_offices = []
        self.livingspaces = []
        self.allocated_livingspace = []
        self.unallocated_livingspaces = []
        self.persons = []
        self.allocated_persons = []
        self.unallocated_persons = []
        self.fellows = []
        self.staff = []

    def create_room (self, room_name, room_type):
        room_names = [room.room_name for room in self.rooms]
        if room_name in room_names:
            msg = "Sorry! %s exists.  Please choose another one" %room_name
            print (msg)
        else:
            if room_type == 'OFFICE':
                new_office = Office(room_name, room_type)
                self.rooms.append(new_office)
                self.unallocated_offices.append (new_office)
                self.offices.append(new_office)
                msg = "Office called %s has been created succesfully!" %room_name
                print (msg)
            
            elif room_type == 'LIVINGSPACE':
                new_livingspace = Livingspace(room_name, room_type)
                self.rooms.append(new_livingspace)
                self.unallocated_livingspaces.append(new_livingspace)
                self.livingspaces.append (new_livingspace)
                msg = "Living Space called %s has been created succesfully!" %room_name
                print (msg)
            else:
                pass


    def unallocated_rooms (self, room_name, room_type):
        if room_type == 'OFFICE':
            capacity = 6
            for office in self.offices:
                if len (office.members) < capacity:
                    self.unallocated_offices.append (office)
                elif len (office.members) >= office.capacity:
                    self.unallocated_offices.remove(office)

        elif room_type == 'LIVINGSPACE':
            capacity = 4
            for livingspace in self.livingspace:
                if len (livingspace.members) < capacity:
                    self.unallocated_livingspaces.append (livingspace)
                elif len (livingspace.members) >= capacity:
                    self.unallocated_livingspace.remove (livingspace)


    def add_person (self, first_name, last_name, title, wants_accomodation ="N"):
        """Adds person and Allocates to room """
        person_name = first_name + spacer + last_name
        self.title = title
        random_livingspace = random.choice(self.unallocated_livingspaces)
        random_office = random.choice(self.unallocated_offices)


        person_names = [person.person_name for person in self.persons]

        if person_name in person_names:
            print ("Sorry! Name exists, please modify name")

        else:
            if title == "FELLOW":
                new_person = Person(person_name, title, wants_accomodation)
                self.persons.append(new_person)
                self.fellows.append (new_person)
                self.unallocated_persons.append (new_person)
                random_office.occupants.append(new_person)
                msg = "Fellow called %s has been added successfully and allocated %s!"\
                %(person_name, random_office.room_name)
                print (msg)
                
                if wants_accomodation == "Y":
                    random_livingspace.occupants.append(Person(first_name, last_name, title, wants_accomodation = 'Y'))
                    msg = "Fellow called %s has been allocated %s!" %(person_name, random_livingspace.room_name)
                    print (msg)     

            elif title == "STAFF":
                new_person = Person(person_name, title, wants_accomodation)
                self.persons.append(new_person)
                self.staff.append (new_person)
                self.unallocated_persons.append (new_person)
                random_office.occupants.append(new_person)
                msg = "Staff called %s has been added successfully and allocated %s!"\
                %(person_name, random_office.room_name)
                if wants_accomodation == 'Y':
                    msg = "Sorry! Living Space for FELLOWS only"
                    print (msg)

    def print_room (self, room_name):
        self.room_name = room_name

        room_names = [room.room_name for room in self.rooms]
        if room_name not in room_names:
            msg = "Sorry! Room does not exist. Check spelling"
            print (msg)

        else:
            if room_name in room_names:
                f























