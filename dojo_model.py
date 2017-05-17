import random
from room import Room, Office, Living
from people import Person, Staff, Fellow

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
            print "Name: " + new_office.room_name + "  |  Type: " + new_office.room_type

        elif room_type == 'LIVING':
            new_livingspace = Living(room_name, room_type)
            self.rooms.append(new_livingspace)
            self.unallocated_livingspaces.append(new_livingspace)
            self.livingspaces.append (new_livingspace)
            msg = "Living Space called %s has been created succesfully!" %room_name
            return msg
            print "Name: " + new_livingspace.room_name + "  |  Type: " + new_livingspace.room_type

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
                    self.unallocated_livngspace.remove (livingspace)

        else:
            pass


    def add_person (self, first_name, last_name, person_title, wants_accomodation ="N"):
        person_name = first_name + spacer + last_name
        self.person_title = person_title

        "Adds person and Allocates to room """

        # new_persons = []
        person_name = [person.person_name for person in self.persons]

        for person in person.person_name:
            if person.person_name in person_name:
                return "Sorry! Name exists, please modify name"

            else:
                if person_title == "FELLOW":
                    new_person = person_name
                    self.persons.append(new_person)
                    self.fellows.append (new_person)
                    self.unallocated_persons (new_person)

                elif person_title == "STAFF":
                    new_person = person_name
                    self.persons.append(new_person)
                    self.staff.append (new_person)
                    self.unallocated_persons (new_person)

dojo = Dojo()
dojo.create_room ('MAMA', 'OFFICE')
dojo.create_room ('WEWE', 'LIVING')
print (len(dojo.offices))

dojo = Dojo()
dojo.add_person ('NELLY', 'OUMA', 'FELLOW', "Y")
print (len(dojo.persons))







