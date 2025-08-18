from colorama import init, Fore, Style
init(autoreset=True)

class Activity:
   
    def __init__(self, name, time, day):
        self.name = name
        self.time = time
        self.day = day

    def __str__(self):
        return f"{self.time} - {self.name}"
    