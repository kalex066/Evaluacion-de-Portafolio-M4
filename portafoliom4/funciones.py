import sys
from actividad import Activity
from colorama import Fore
import unicodedata

def normalize_day(day_string):
    nfkd_form = unicodedata.normalize('NFKD', day_string)
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)]).lower()

def standardize_day(day_input):
    valid_days = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    normalized_input = normalize_day(day_input)
    for valid_day in valid_days:
        if normalize_day(valid_day) == normalized_input:
            return valid_day
    return day_input.capitalize()

def assign_dad_shift(dad_person, mom_person, david_person, shift):
    schedules = {
        1: ("07:00", "14:00"),
        2: ("14:00", "22:00"),
        3: ("22:00", "07:00")
    }
    start, end = schedules.get(shift, ("00:00", "00:00"))

    for day in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]:
        dad_person.add_activity(Activity(f"Trabajo (Turno {shift})", f"{start}-{end}", day))
        if shift in [1, 2]:
            mom_person.add_activity(Activity("Buscar a los niños", "13:00", day))
        else:
            dad_person.add_activity(Activity("Buscar a los niños", "13:00", day))

    for day in ["Martes", "Jueves"]:
        if shift in [1, 3]:
            dad_person.add_activity(Activity("Llevar a David al fútbol", "18:30", day))
        else:
            mom_person.add_activity(Activity("Llevar a David al fútbol", "18:30", day))

def add_activity(person):
    try:
        activity_name = input("Nombre de la nueva actividad: ")
        activity_time = input("Hora (ej. 17:00): ")
        activity_day = input("Día (ej. Lunes): ").strip()

        valid_days = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        if normalize_day(activity_day) not in [normalize_day(d) for d in valid_days]:
            print(f"{Fore.RED} Día inválido. Por favor, ingresa un día de la semana válido.")
            return

        if not activity_name or not activity_time or not activity_day:
            print(f"{Fore.RED} Todos los campos son obligatorios.")
            return

        standard_day = standardize_day(activity_day)
        activity = Activity(activity_name, activity_time, standard_day)
        person.add_activity(activity)
        print(f"{Fore.GREEN} Actividad '{activity_name}' agregada para {person.name} el día {standard_day}.")

    except Exception as e:
        print(f"{Fore.RED} Ocurrió un error al agregar la actividad: {e}")

def show_weekly_summary(person):
    days = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    print(f"\n{Fore.CYAN} Resumen semanal de {person.name}:")
    for day in days:
        normalized_day = normalize_day(day)
        activities = [a for a in person.activities if normalize_day(a.day) == normalized_day]
        print(f"{Fore.MAGENTA}{day}:")
        if activities:
            for act in sorted(activities, key=lambda x: x.time):
                print(f"  {Fore.YELLOW}- {act}")
        else:
            print(f"  {Fore.RED}No hay actividades.")

def export_weekly_summary_to_txt(person):
    days = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    file_name = f"Resumen_{person.name}.txt"

    with open(file_name, "w", encoding="utf-8") as file:
        file.write(f" Resumen semanal de {person.name}\n\n")
        for day in days:
            normalized_day = normalize_day(day)
            activities = [a for a in person.activities if normalize_day(a.day) == normalized_day]
            file.write(f"{day}:\n")
            if activities:
                for act in sorted(activities, key=lambda x: x.time):
                    file.write(f"  - {act.time} - {act.name}\n")
            else:
                file.write("  No hay actividades.\n")
            file.write("\n")

    print(f"{Fore.GREEN} El resumen ha sido exportado a '{file_name}'")

def edit_or_delete_activity(person):
    day = input("¿Qué día quieres revisar? (ej. Martes): ").strip()
    normalized_day = normalize_day(day)
    activities = [a for a in person.activities if normalize_day(a.day) == normalized_day]
    
    if not activities:
        print(f"{Fore.RED} No hay actividades ese día.")
        return

    print(f"\n Actividades de {person.name} el {standardize_day(day)}:")
    for i, act in enumerate(activities):
        print(f"{i + 1}. {act}")

    selection = input("Selecciona el número de la actividad a editar/eliminar: ")
    try:
        index = int(selection) - 1
        activity = activities[index]
    except (ValueError, IndexError):
        print(f"{Fore.RED} Selección inválida.")
        return

    print("\n¿Qué deseas hacer?")
    print("1. Editar actividad")
    print("2. Eliminar actividad")
    option = input("Opción: ")

    if option == "1":
        new_name = input("Nuevo nombre (presiona enter para mantener el nombre): ")
        new_time = input("Nueva hora (presiona enter para mantener la hora): ")
        new_day = input("Nuevo día (presiona enter para mantener el día): ")

        if new_name:
            activity.name = new_name
        if new_time:
            activity.time = new_time
        if new_day:
            activity.day = standardize_day(new_day)

        print(f"{Fore.GREEN} La actividad ha sido actualizada.")

    elif option == "2":
        person.activities.remove(activity)
        print(f"{Fore.GREEN} La actividad ha sido eliminada.")
    else:
        print(f"{Fore.RED} Opción inválida.")