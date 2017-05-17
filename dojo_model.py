import random
from room_model import Room, Office, Living
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

        if room_type == 'OFFICE':
            new_office = Office(room_name, room_type)
            self.rooms.append(new_office)
            self.unallocated_offices.append (new_office)
            self.offices.append(new_office)
            msg = "Office called %s has been created succesfully!" %room_name
            return msg
            print ("Name: " + new_office.room_name + "  |  Type: " + new_office.room_type)

        elif room_type == 'LIVING':
            new_livingspace = Living(room_name, room_type)
            self.rooms.append(new_livingspace)
            self.unallocated_livingspaces.append(new_livingspace)
            self.livingspaces.append (new_livingspace)
            msg = "Living Space called %s has been created succesfully!" %room_name
            return msg
            print ("Name: " + new_livingspace.room_name + "  |  Type: " + new_livingspace.room_type)

        else:
            room_names = [room.room_name for room in self.rooms]
            if room.room_name == room_name:
                msg = "Sorry! %s exists.  Please choose another one" %room_name
                return msg

    def unallocated_rooms (self, room_name, room_type):
        if room_type == 'OFFICE':
            capacity = 6
            for office in self.offices:
                if len (office.members) < capacity:
                    self.unallocated_offices.append (office)
                elif len (office.members) >= office.capacity:
                    self.unallocated_offices.remove(office)

        elif room_type == 'LIVING':
            capacity = 4
            for livingspace in self.livingspace:
                if len (livingspace.members) < capacity:
                    self.unallocated_livingspaces.append (livingspace)
                elif len (livingspace.members) >= capacity:
                    self.unallocated_livingspace.remove (livingspace)

        else:
            pass



    def add_person (self, first_name, last_name, person_title, wants_accomodation ="N"):
        person_name = first_name + spacer + last_name
        self.person_title = person_title
        random_livingspace = random.choice(self.unallocated_livingspaces)
        random_office = random.choice(self.unallocated_offices)

        "Adds person and Allocates to room """

        # self.allocated_offices = random_office
        person_names = [person.person_name for person in self.persons]

        if person_name in person_names:
            return "Sorry! Name exists, please modify name"

        else:
            if person_title == "FELLOW":
                new_person = Person(person_name, person_title, wants_accomodation)
                self.persons.append(new_person)
                self.fellows.append (new_person)
                self.unallocated_persons.append (new_person)
                random_office.occupants.append(Person(first_name, last_name, person_title, wants_accomodation))
                if wants_accomodation == "Y":
                    random_livingspace.occupants.append(Person(first_name, last_name, person_title, wants_accomodation = 'Y'))
                else:
                    pass
        

            elif person_title == "STAFF":
                new_person = Person(person_name, person_title, wants_accomodation)
                self.persons.append(new_person)
                self.staff.append (new_person)
                self.unallocated_persons.append (new_person)
                random_office.occupants.append(Person(first_name, last_name, person_title, wants_accomodation))
                if wants_accomodation == 'Y':
                    msg = "Sorry! Living Space for FELLOWS only"
                    return msg
                else:
                    pass

        


dojo = Dojo()
dojo.create_room ('MAMA', 'OFFICE')
dojo.create_room ('WEWE', 'LIVING')
print (len(dojo.offices))
dojo.add_person ('NELLY', 'OUMA', 'FELLOW', "Y")
dojo.add_person ('ANINI', 'HELIDA', 'STAFF', "Y")
print (len(dojo.fellows))








