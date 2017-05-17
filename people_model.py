spacer = " "


class Person(object):

    """ Fellow and Staff inherit from the Class Person"""

    def __init__(self, first_name, last_name, title, wants_accomodation = "N"):

        self.name = first_name + spacer + last_name
        self.title = title  

    def __repr__(self):
        return "<Person %s>" % self.name


class Staff(Person):

    job_type = "STAFF"

    def __init__(self,first_name, last_name, title, wants_accomodation = "N"):

        super(Staff, self).__init__(self.name)
        self.title = title

    def __repr__(self):
        return "<Staff %s>" % self.name


class Fellow(Person):

    job_type = "FELLOW"

    def __init__(self, first_name, last_name, title, wants_accomodation = "N"):
        super(Fellow, self).__init__(self.name)
        self.id = person_id

    def __repr__(self):
        return "<Fellow %s>" % self.name