from Attendee import Attendee
from Session import Session

session1 = Session("Python", 2)
session2 = Session("Java", 4)

attendee1 = Attendee("Nikita", 1)
attendee2 = Attendee("Muath", 2)
attendee3 = Attendee("Haritha", 3)
attendee4 = Attendee("Gaurav", 4)

session1.add_attendee(attendee1)
session1.add_attendee(attendee2)
session1.add_attendee(attendee3)

attendee1.list_registered_sessions()
