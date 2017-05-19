#!/usr/bin/env python

""" 
DOJO

Usage:
    dojo create_room <room_type> <room_name>...
    dojo add_person <first_name> <last_name> <title>  [--wants_acommodation == 'N']
    dojo print_room <room_name>
    dojo print_allocations [--o = FILENAME]
    dojo (-i | --interactive)
    dojo (-h | --help | --version)

Options:
    -i, --interactive      Interactive Mode
    -h, --help             Show this screen
    -v, --version

"""


import sys
import cmd
from docopt import docopt, DocoptExit
from dojo_model import Dojo
from people_model import Fellow, Staff
from room_model import Livingspace, Office

dojo = Dojo()
spacer = " "

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:

            print('Invalid Command!, Type help')
            print(e)
            return

        except SystemExit:

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

class Interactive (cmd.Cmd):

    print("                 x----------------------------------------------x                  ")
    print("                 x----------------------------------------------x                  ")
    print(spacer)
    print("                     ALLOCATIONS MADE EASIER AND FASTER!!!                         ")
    print(spacer)
    print("                 x----------------------------------------------x                  ")
    print("                 x----------------------------------------------x                  ")
    print(spacer)
    intro = "                         >>> LETS ROOM UP!!! <<<                     "
    print (spacer)
    prompt = "DOJO >> "
    print (spacer)

    
    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>..."""
        try:
            for room_name in arg["<room_name>"]:
                room_type = arg["<room_type>"]
                dojo.create_room (room_name, room_type)
                print (spacer)
        except:
            print ("Create room")


    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <first_name> <last_name> <title> [<wants_acommodation>]"""
        try:
            first_name = arg["<first_name>"]
            last_name = arg["<last_name>"]
            title = arg["<title>"]
            wants_accomodation = arg["<wants_acommodation>"]

            dojo.add_person(first_name, last_name, title, wants_accomodation)
        except:
            print ("No Rooms Available cannot add person")
    
    def do_quit(self,arg):
        """Quits out of Interactive Mode."""

        print('Visit Soon!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt["--interactive"]:
    try:
        print (__doc__)
        Interactive().cmdloop()
    except KeyboardInterrupt:
        print ("Exiting")

print(opt)