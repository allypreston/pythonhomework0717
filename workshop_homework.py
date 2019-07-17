class Workshop:

    def __init__(self, obj_workshop_name, obj_teacher_name, obj_monster_attendees = [] ):
        self.workshop_name = obj_workshop_name
        self.teacher = obj_teacher_name
        self.list_of_attendees = obj_monster_attendees

    def teacher_set(self, obj_teacher_name):
        self.teacher = obj_teacher_name

    def add_attendee(self, obj_attendee):
        self.list_of_attendees.append(obj_attendee)

    def list_attendees(self):
        return self.list_of_attendees

