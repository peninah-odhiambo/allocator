#!/usr/bin/env python

""" DOJO

Usage:
dojo create_room                 <room_name> <room_type>
dojo add_person                  <first_name> <last_name> <title>  [--wants_acommodation = 'N']


Options:
-i | --interactive
-h | --help Show this screen
-v | --version



"""

import sys
import cmd
from docopt import docopt, DocoptExit
from dojo_model import Dojo
from people_model import Fellow, Staff

dojo = Dojo()

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:


            print('Invalid Command!')
            print(e)
            return

        except SystemExit:


            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

def start():

    print ("LOADING DOJO >>>>>>>>>>>>>>>>>>")

    intro = 'Welcome to the DOJO SPACE ALLOCATION APP'

    print ("Type help for a list of commands")

  

class Interactive(cmd.Cmd):

    dojo_prompt = 'DOJO'
    prompt = dojo_prompt

    @docopt_cmd
    def do_create_room (self,arg):
        
        """ Usage: create_room <room_name> <room_type> """

        room_name = arg["<room_name>"]
        room_type = arg["<room_type>"]

        if room_name and room_type:
            result = dojo.create_room (room_name, room_type)

    @docopt_cmd
    def do_add_person (self,arg):

        """ Usage: add_person <first_name> <last_name> <title> [--wants_accomodation = 'N'] """

        first_name = arg["<first_name>"]
        last_name = arg["<last_name>"]
        title = arg["<title>"]
        wants_accomodation = arg["<wants_accomodation>"]

        title == "FELLOW" or "STAFF"

        if wants_accomodation is None:
            wants_accomodation == "N"

            print (self.dojo.add_person (first_name, last_name, title))

        else:
            print (self.dojo.add_person (first_name, last_name, title, wants_acommodation))

    @docopt_cmd
    def do_clear(self, arg):
        """Clears screen"""
        os.system("clear")


    @docopt_cmd
    def do_quit(self,arg):
        """Quits out of Interactive Mode."""

        print('Visit Soon!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    os.system("clear")
    start()
    interactive().cmdloop()

print(opt)