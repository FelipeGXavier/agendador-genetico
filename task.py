class Task:

    def __init__(self, id, preference = 0):
        self.preference = preference
        self.week = 0
        self.schedule = 0
        self.id = id

    def set_week(self, week):
        self.week = week
        return self
    
    def set_schedule(self, schedule):
        self.schedule = schedule
        return self

    def gene(self):
        return str(self.week)  + str(self.schedule) + str(self.preference) + str(self.id)

    def __str__(self):
        return "id=" + str(self.id) + ", week=" + str(self.week) + ", preference=" + str(self.preference) + ", schedule=" + str(self.schedule)

    




    