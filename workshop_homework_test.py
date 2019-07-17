from workshop_homework import *

workshop1 = Workshop("scare_tactics", "mr waternoose")
workshop2 = Workshop("python for monsters", "Filipe Paiva", "Ally Preston")

workshop1.teacher_set("Adam Simone")

print(workshop1.teacher)

print(workshop1.list_of_attendees)

workshop1.add_attendee("James P. Sullivan")

print(workshop1.list_of_attendees)

print(workshop1.workshop_name, ', ', workshop1.teacher, ', ', workshop1.list_of_attendees)
print(workshop2.workshop_name, ', ', workshop2.teacher, ', ', workshop2.list_of_attendees)