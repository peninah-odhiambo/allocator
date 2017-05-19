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
            if room_type.upper() == 'OFFICE':
                new_office = Office(room_name, room_type)
                self.rooms.append(new_office)
                self.unallocated_offices.append (new_office)
                self.offices.append(new_office)
                msg = "Office called %s has been created succesfully!" %room_name
                print("*******created room(s)*********")
                print(spacer)
                print (msg)
            
            elif room_type.upper() == 'LIVINGSPACE':
                new_livingspace = Livingspace(room_name, room_type)
                self.rooms.append(new_livingspace)
                self.unallocated_livingspaces.append(new_livingspace)
                self.livingspaces.append (new_livingspace)
                msg = "Living Space called %s has been created succesfully!" %room_name
                print("*******created room(s)*********")
                print(spacer)
                print (msg)

            elif room_type.upper() != 'OFFICE' or room_type.upper() != 'LIVINGSPACE':
                msg = 'Sorry, Choose room type OFFICE or LIVINGSPACE'
                print (msg)

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
                if len(random_office.occupants) < random_office.capacity:
                    random_office.occupants.append(new_person)
                    print("*******added person(s)*********")
                    msg = "Staff called %s has been added successfully and allocated  Office %s!"\
                    %(person_name, random_office.room_name)
                    print (msg)
                else:
                    print ("Room capacity full!")
                
                if wants_accomodation == "Y":
                    if len(random_livingspace.occupants) < random_livingspace.capacity:
                        random_livingspace.occupants.append(new_person)
                        msg = "Staff called %s has been added successfully and allocated Livingspace %s!"\
                        %(person_name, random_livingspace.room_name)
                        print (msg)
                    else:
                        print ("Room capacity full!")    

            elif title == "STAFF":
                new_person = Person(person_name, title, wants_accomodation)
                self.persons.append(new_person)
                self.staff.append (new_person)
                self.unallocated_persons.append (new_person)
                if len(random_office.occupants) < random_office.capacity:
                    random_office.occupants.append(new_person)
                    print("*******added person(s)*********")
                    msg = "Staff called %s has been added successfully and allocated  Office %s!"\
                    %(person_name, random_office.room_name)
                    print (msg)
                else:
                    print ("Room capacity full!")

                if wants_accomodation == 'Y':
                    msg_error = "Sorry! Living Space for FELLOWS only"
                    print(msg_error)

            else:
                print ("Title can only be FELLOW or STAFF")

    def print_room (self, room_name):
        self.room_name = room_name

        room_names = [room.room_name for room in self.rooms]
        if room_name not in room_names:
            msg = "Sorry! Room does not exist. Check spelling"
            print (msg)

        else:
            if room_name in room_names:
                f
























