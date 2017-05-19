import unittest
from unittest import TestCase
from dojo_model import Dojo
from people_model import Fellow, Staff


class TestDojo (unittest.TestCase):

    def setUp (self): 
        self.dojo = Dojo()
        self.dojo.create_room ('NAI', 'OFFICE')
        self.dojo.create_room ('BLUE', 'LIVINGSPACE')
        self.dojo.add_person ("RUTH", "MASIKA", "FELLOW", "N")


    def test_add_person (self):
        """ Tests if person is added in the system """

        self.assertEqual (len(self.dojo.persons), 1)
        self.dojo.add_person ("NINAH", "ANYANGO", "FELLOW", "Y")
        self.assertEqual (len(self.dojo.persons), 2, "Person added succesfully!")

    def test_double_entries (self):
        """ Tests if a person is added more than once """
        self.assertEqual(len(self.dojo.persons), 1)
        self.dojo.add_person ("RUTH", "MASIKA", "FELLOW", "N")
        self.assertEqual(len(self.dojo.persons), 2, "Person exists! Modify name")


    def test_added_fellow_office (self):

        """ Tests if fellow is allocated an office successfully """

        self.dojo.create_room ("PEARL", "OFFICE")
        self.assertEqual (len(self.dojo.offices), 2)
        self.dojo.add_person ("REHEMA", "ROBI", "FELLOW", "Y" )
        self.assertEqual (len(self.dojo.rooms), 3, "Fellow Office allocation successful!")

    def test_added_fellow_living_space (self):

        """ Tests if fellow is allocated a Living space successfully """

        self.dojo.create_room ("MARS", "LIVINGSPACE")
        self.assertEqual (len(self.dojo.livingspaces), 2)
        self.dojo.add_person ("ROSE", "FELLOW", "Y")
        self.assertEqual (len(self.dojo.rooms), 3, "Fellow Living Space allocation Successful!")

    def test_added_staff_office (self):

        """ Tests if staff is added and allocated an office successfully """ 

        self.dojo.create_room ("RUBY", "OFFICE")
        self.assertEqual (len(self.dojo.offices), 2)
        self.dojo.add_person ("REMY", "STAFF", "FELLOW", "Y")
        self.assertEqual (len(self.dojo.offices), 2, "Staff added and Office allocated successfully")

    def test_no_living_space_staff (self):

        """ Tests thats staff is not allocated living space """

        self.dojo.create_room ("PLUTO", "LIVINGSPACE")
        self.assertEqual (len(self.dojo.livingspaces),2)
        self.dojo.add_person ("PAULA", "STAFF", "Y")
        self.assertEqual (len(self.dojo.rooms), 3, "Sorry, Living Space available for Fellows Only")


if __name__ == "__main__":
    unittest.main()

