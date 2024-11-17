class Attendee:
    def __init__(self, name, id):
        self.name = name
        self.attendee_id = id
        self.registered_sessions = []

    def register_for_session(self, session):
        if session in self.registered_sessions:
            print("You are already registered there!")
        else:
            self.registered_sessions.append(session)
            print("You have been added to the session")

    def cancel_registration(self, session):
        if session in self.registered_sessions:
            self.registered_sessions.remove(session)
        else:
            print(f"You haven't registered")

    def list_registered_sessions(self):
        print("You have registered: ")
        for i in range(len(self.registered_sessions)):
            print(self.registered_sessions[i].session_title)

