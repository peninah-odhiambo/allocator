class Room(object): 

    """ Office and Living space inherits from the Class Room """
    
    def __init__(self, room_name, room_type):
        self.occupants = []
        self.room_name = room_name
        self.room_type = room_type

    def __repr__(self):
        return "<Room %s %s>" % self.room_name, self.room_type


class Office(Room):
    
    capacity = 6

    def __init__(self, room_name, room_type):
        super(Office, self).__init__(room_name, room_type)

    def __repr__(self):
        return "<Office %s %s>" % (self.room_name, self.room_type)


class Livingspace(Room):

    capacity = 4

    def __init__(self, room_name, room_type):
        super(Livingspace, self).__init__(room_name, room_type)

    def __repr__(self):
        return "<Living space %s %s>" % (self.room_name, self.room_type)


