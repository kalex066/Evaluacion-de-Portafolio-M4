import sys
from persona import Person
from actividad import Activity
from funciones import *
from colorama import Fore

def main():
    try:
        shift = int(input("Turno semanal de Papá (1, 2 o 3): "))
        if shift not in [1, 2, 3]:
            print(f"{Fore.RED} Turno inválido. Elige 1, 2 o 3.")
            return

        amy = Person("Amy", 10)
        david = Person("David", 6)
        dad = Person("Papá")
        mom = Person("Mamá")

        # actividades con horario fijo
        for day in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]:
            amy.add_activity(Activity("Clase de ballet", "16:00", day))
            mom.add_activity(Activity("Llevar a Amy al ballet", "15:30", day))

        for day in ["Martes", "Jueves"]:
            amy.add_activity(Activity("Entrenamiento físico", "19:30", day))
            david.add_activity(Activity("Clase de fútbol", "19:00", day))

        amy.add_activity(Activity("Clase de inglés", "14:00", "Sábado"))
        mom.add_activity(Activity("Clase de inglés", "15:00", "Sábado"))
        david.add_activity(Activity("Clase de música", "11:00", "Sábado"))

        for day in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]:
            mom.add_activity(Activity("Gym", "08:00", day))

        for day in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]:
            mom.add_activity(Activity("Bootcamp", "18:00–21:00", day))
            
        assign_dad_shift(dad, mom, david, shift)
        people = [amy, david, dad, mom]

        while True:
            print(f"\n{Fore.BLUE} Selecciona la persona:")
            for i, p in enumerate(people):
                print(f"{i + 1}. {p.name}")
            print(f"{len(people) + 1}. Mostrar rutina diaria de todos")
            print(f"{len(people) + 2}. Salir")

            selection = input("Opción: ")
            
            if selection.isdigit():
                selection = int(selection)
                
                if 1 <= selection <= len(people):
                    chosen_person = people[selection - 1]
                    while True:
                        print(f"\n{Fore.GREEN}Opciones para {chosen_person.name}:")
                        print("1. Ver rutina diaria")
                        print("2. Ver resumen semanal")
                        print("3. Añadir una actividad")
                        print("4. Editar o eliminar actividad")
                        print("5. Exportar resumen de actividades en archivo txt")
                        print("6. Volver al menú principal")

                        sub_option = input("Opción: ")

                        if sub_option == "1":
                            chosen_day = input("¿Qué día de la semana quieres ver? (ej. Lunes): ")
                            chosen_person.show_daily_routine(chosen_day)
                        elif sub_option == "2":
                            show_weekly_summary(chosen_person)
                        elif sub_option == "3":
                            add_activity(chosen_person)
                        elif sub_option == "4":
                            edit_or_delete_activity(chosen_person)
                        elif sub_option == "5":
                            export_weekly_summary_to_txt(chosen_person)
                        elif sub_option == "6":
                            break
                        else:
                            print(f"{Fore.RED} Opción inválida.")
                
                elif selection == len(people) + 1:
                    # Show routine for all
                    chosen_day = input("¿Qué día de la semana quieres ver? (ej. Lunes): ")
                    for p in people:
                        p.show_daily_routine(chosen_day)
                
                elif selection == len(people) + 2:
                    print(f"{Fore.BLUE} ¡Bye Bye!")
                    sys.exit()
                
                else:
                    print(f"{Fore.RED} Opción inválida. Inténtalo de nuevo.")
            
            else:
                print(f"{Fore.RED} Por favor, ingresa un número válido.")
    
    except ValueError:
        print(f"{Fore.RED} Entrada inválida. Por favor, ingresa un número.")
    except Exception as e:
        print(f"{Fore.RED} Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()