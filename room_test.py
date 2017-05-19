import unittest
from unittest import TestCase
from dojo_model import Dojo
from room_model import Room, Office, Livingspace


class TestDojo (unittest.TestCase):
    
    def setUp (self): 
        self.dojo = Dojo()

    def test_create_room (self):

        """ Tests if room is created """
        self.assertEqual (len(self.dojo.rooms), 0)
        self.dojo.create_room ("GOLD", "OFFICE")
        self.assertEqual (len(self.dojo.rooms), 1, "Room created Succesfully!")

    def test_room_is_office_or_livingspace (self):
        """Tests if room created ins OFFICE or LIVINGSPACE"""
        self.assertEqual (len(self.dojo.rooms), 0)
        self.dojo.create_room ('GOLD', 'HOME')
        self.assertEqual (len(self.dojo.rooms), 0, "Sorry! Choose OFFICE or LIVINGSPACE")

    def test_created_office (self):

        """Tests if office is created and if more than one office can be created """

        self.assertEqual(len(self.dojo.offices), 0)
        self.dojo.create_room ("DIAMOND", "OFFICE")
        self.assertEqual(len(self.dojo.offices), 1)

    def test_created_livingspace (self):

        """ Tests if office is created and if more than one living space can be created """

        self.assertEqual (len(self.dojo.livingspaces), 0)
        self.dojo.create_room ("MERCURY", "LIVINGSPACE")
        self.dojo.create_room ("VENUS", "LIVINGSPACE")
        self.assertEqual(len(self.dojo.livingspaces), 2)


    def test_room_name_repeated (self):

        """ Tests if room created already exists """

        self.dojo.create_room ("MARS", "OFFICE")
        self.dojo.create_room ("MARS", "OFFICE")
        self.assertEqual(len(self.dojo.rooms), 1)

if __name__ == "__main__":
    unittest.main()




