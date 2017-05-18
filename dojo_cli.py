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

    print("=" * 30 + "\nWELCOME\n" + "=" * 30)
    print (spacer)
    print (spacer)
    intro = "ALLOCATION MADE EASIER AND FASTER"
    prompt = "> "
    print (spacer)
    print (spacer)
    print("=" * 60)
    print (spacer)
    print (spacer)
    


    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>..."""

        room_name = arg["<room_name>"]
        room_type = arg["<room_type>"]

        if room_name and room_type:
            dojo.create_room (room_name, room_type)


    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <first_name> <last_name> <title> [<wants_acommodation>]"""
        first_name = arg["<first_name>"]
        last_name = arg["<last_name>"]
        title = arg["<title>"]
        wants_accomodation = arg["<wants_acommodation>"]

        dojo.add_person(first_name, last_name, title, wants_accomodation)

    
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