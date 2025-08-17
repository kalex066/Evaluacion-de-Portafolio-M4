from actividad import Activity
from colorama import Fore
import unicodedata
def normalize_day(day_string):
    nfkd_form = unicodedata.normalize('NFKD', day_string)
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)]).lower()

class Person:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age
        self.activities = []

    def add_activity(self, activity):
        self.activities.append(activity)

    def show_daily_routine(self, day):
        print(f"\n{Fore.CYAN} Rutina de {self.name} para el día {day}:")
        normalized_day = normalize_day(day)
        daily_activities = [act for act in self.activities if normalize_day(act.day) == normalized_day]
        if daily_activities:
            for act in sorted(daily_activities, key=lambda x: x.time):
                print(f"  {Fore.YELLOW}- {act}")
        else:
            print(f"  {Fore.RED} No hay actividades registradas.")
