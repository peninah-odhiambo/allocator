#!/usr/bin/env python

""" DOJO

Usage:
create_room         LIVING|OFFICE	<room_name>
add_person          FELLOW |STAFF	<first_name> <last_name> [--wants_acommodation = N]
allocate_person				        <identifier> <new_room_name>
load_persons				        <filename>
print_allocations 			        [--o=filename]
print_unallocated			        [--o=filename]
print_room					        <room_name>
save_state					        [--db=sqlite_database]
load state 					        <sqlite_database>


Options:
-i | --interactive
-h | --help Show this screen
-v | --version

create_room			Creates a new room
add_person			Adds a new person
allocate_person		Allocates person to a new room
load_persons		Load persons from a created files
print_room			Prints rooms created	
save_state			Saves allocations of people and offices in the database		
loads state			Loads up the state of people and rooms from the sqlite_database

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
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

def start():
    # os.system('clear')
    print ("LOADING DOJO >>>>>>>>>>>>>>>>>>")

    intro = 'Welcome to the DOJO SPACE ALLOCATION APP'

    print ("Type help for a list of commands")

  

class Interactive (cmd.Cmd):

    dojo_prompt = 'DOJO'
    prompt = dojo_prompt

    @docopt_cmd
    def do_create_room (self,arg):

    @docopt_cmd
    def do_add_person (self,arg):

    @docopt_cmd
    def do_allocate_person (self,arg):

    @docopt_cmd
    def do_load_persons (self,arg):

    @docopt_cmd
    def do_print_rooms (self,arg):

    @docopt_cmd
    def do_save_state (self,arg):

    @docopt_cmd
    def do_load_state (self, arg):

  


    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Visit Soon!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    start()
    Interactive().cmdloop()

print(opt)