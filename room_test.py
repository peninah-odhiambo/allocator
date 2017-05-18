import unittest
import sys
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

    def test_created_office (self):

        """Tests if office is created and if more than one office can be created """

        self.assertEqual(len(self.dojo.offices), 0)
        self.dojo.create_room ("DIAMOND", "OFFICE")
        self.assertEqual(len(self.dojo.offices), 1)

    def test_created_livingspace (self):

        """ Tests if living is created and if more than one living space can be created """

        self.assertEqual (len(self.dojo.livingspaces), 0)
        self.dojo.create_room ("MERCURY", "LIVING")
        self.dojo.create_room ("VENUS", "LIVING")
        self.assertEqual(len(self.dojo.livingspaces), 2)


    def test_room_name_repeated (self):

        """ Tests if room created already exists """

        self.dojo.create_room ("MARS", "OFFICE")
        self.dojo.create_room ("MARS", "OFFICE")
        self.assertEqual(len(self.dojo.rooms), 1)

    def test_print_room (self):
        """ Prints  the names of all the people in room_name on the screen"""



if __name__ == "__main__":
    unittest.main()




