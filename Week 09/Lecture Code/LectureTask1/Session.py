class Session:
    def __init__(self, prop1, prop2):
        self.session_title = prop1
        self.max_capacity = prop2
        self.registered_attendees = []

    def add_attendee(self, attendee):
        if len(self.registered_attendees) < self.max_capacity:
            self.registered_attendees.append(attendee)
            attendee.register_for_session(self)
            print(self.registered_attendees)
        else:
            print("We have reached the capacity")

    def remove_attendee(self, attendee):
        if attendee in self.registered_attendees:
            self.registered_attendees.remove(attendee)
        else:
            print(f"{attendee.name} not in the Session")

    def list_attendees(self):
        for i in range(len(self.registered_attendees)):
            print(self.registered_attendees[i].name)
