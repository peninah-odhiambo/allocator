import unittest
import sys
from unittest import TestCase
from dojo import Dojo
from room import Room, Office, Living
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


    def test_create_room (self):

        """ Tests if room is created """
        self.assertEqual (len(self.dojo.rooms), 0)
        self.dojo.create_room ("GOLD", "OFFICE")
        self.assertEqual (len(self.dojo.rooms), 1, "Room created Succesfully!")

    def test_created_office (self):

        """Tests if office is created and if more than one office can be created """

        self.assertEqual(len(self.dojo.offices), 0)
        # self.dojo.create_room ("GOLD", "OFFICE")
        self.dojo.create_room ("DIAMOND", "OFFICE")
        self.assertEqual(len(self.dojo.offices), 1)

    def test_created_livingspace (self):

        """ Tests if office is created and if more than one living space can be created """

        self.assertEqual (len(self.dojo.livingspaces), 0)
        self.dojo.create_room ("MERCURY", "LIVING")
        self.dojo.create_room ("VENUS", "LIVINGSPACE")
        self.assertEqual(len(self.dojo.livingspaces), 1)


    def test_room_name_repeated (self):

        """ Tests if room created already exists """

        self.dojo.create_room ("MARS", "OFFICE")
        room_names = [room.room_name for room in self.dojo.rooms]
        self.assertIn ("MARS", self.room_name)
        entry = self.dojo.create_room ("MARS", "OFFICE")
        self.assertEqual(entry, "Sorry, Room Name already exists.  Kindly Choose another name")




