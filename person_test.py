import unittest
import sys
from unittest import TestCase
from dojo_model import Dojo
from people_model import Fellow, Staff
# from main import dojo.Dojo
# from main import room.Room

# AssertIn = Test that first is in second.  If not, the test will fail.
# AssertEqual = Test that first and second are equal. If the values do not compare equal, the test will fail.

class TestDojo (unittest.TestCase):

    def setUp (self):
        self.dojo = Dojo()
        self.dojo.offices = []
        self.dojo.livingspaces = []
        self.dojo.vacant_rooms = []
        self.dojo.vacant_offices = []
        self.dojo.vacant_livingspaces = []
        self.dojo.rooms = []
        self.dojo.persons = []



    def test_add_person (self):
        """ Tests if person is added in the system """

        self.assertEqual (len(self.dojo.persons, 0))
        self.dojo.add_person ("NINAH", "ANYANGO", "FELLOW", "Y")
        self.assertEqual (len(self.dojo.persons), 1, "Person added succesfully!")

    def test_double_entries (self):
        """ Tests if a person is added more than once """

        self.dojo.add_person ("NINAH", "ANYANGO", "FELLOW", "Y")
        person_names = [person.person_name for person in self.dojo.persons]
        self.assertIn ("NINAH", "ANYANGO", self.first_name, self.last_name)
        entry = self.dojo.add_perpson ("NINAH", "ANYANGO", "FELLOW", "Y")
        self.assertEqual (entry, "Sorry, Person already exists.  Kindly choose/modify another name")


    def test_added_fellow_office (self):

        """ Tests if fellow is allocated an office succesfully """

        self.dojo.create_room ("PEARL", "OFFICE")
        self.assertEqual (len(self.dojo.test_added_fellow_office), 0)
        self.dojo.add_person ("REHEMA", "FELLOW")
        self.assertEqual (len(self.dojo.rooms), 1, "Fellow Office allocation succesful!")

    def test_added_fellow_living_space (self):

        """ Tests if fellow is allocated a Living space succesfully """

        self.dojo.create_room ("MARS", "LIVING")
        self.assertEqual (len(self.dojo.test_added_fellow_livingspace), 0)
        self.dojo.add_person ("ROSE", "FELLOW", "Y")
        self.assertEqual (len(self.dojo.rooms), 1, "Fellow Living Space allocation Succesful!")

    def test_added_staff_office (self):

        """ Tests if staff is added and allocated an office succesfully """ 

        self.dojo.create_room ("RUBY", "OFFICE")
        self.assertEqual (len(self.dojo.test_added_staff_office), 0)
        self.dojo.add_person ("REMY", "STAFF")
        self.assertEqual (len(self.dojo.rooms), 1, "Staff added and Office allocated succesfully")

    def test_no_living_space_staff (self):

        """ Tests thats staff is not alllocated living space """
        self.dojo.create_room ("PLUTO", "LIVING")
        se;f.assertEqual (len(self.dojo.test_no_living_space_staff),0)
        self.dojo.add_person ("PAULA", "STAFF", "Y")
        self.assertEqual (len(self.dojo.rooms), 0, "Sorry, Living Space available for Fellows Only")


if __name__ == "__main__":
    unittest.main()











