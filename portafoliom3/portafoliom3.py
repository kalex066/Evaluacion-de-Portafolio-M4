import random
from colorama import init, Fore, Style

init(autoreset=True)

ejercicios = {
    "Bíceps-Tríceps": {
        "Flexiones diamante": {"tipo": "repeticiones", "calorias": 7},
        "Fondos de tríceps": {"tipo": "repeticiones", "calorias": 6},
        "Curl bíceps con botellas": {"tipo": "reps", "calorias": 5},
        "Extensión de tríceps sobre cabeza": {"tipo": "repeticiones", "calorias": 6},
        "Curl martillo con mochila": {"tipo": "repeticiones", "calorias": 5}
    },
    "Abdomen-Espalda": {
        "Plancha": {"tipo": "tiempo", "calorias": 5},
        "Superman": {"tipo": "repeticiones", "calorias": 6},
        "Abdominales": {"tipo": "repeticiones", "calorias": 6},
        "Crunch bicicleta": {"tipo": "repeticiones", "calorias": 7},
        "Elevación de piernas": {"tipo": "repeticiones", "calorias": 6}
    },
    "Hombro-Pecho": {
        "Flexiones clásicas": {"tipo": "repeticiones", "calorias": 7},
        "Flexiones abiertas": {"tipo": "repeticiones", "calorias": 8},
        "Pike push ups": {"tipo": "repeticiones", "calorias": 8},
        "Flexiones con palmada": {"tipo": "repeticiones", "calorias": 9},
        "Elevaciones frontales con botellas": {"tipo": "repeticiones", "calorias": 6}
    },
    "Glúteos": {
        "Puente de glúteos": {"tipo": "repeticiones", "calorias": 6},
        "Patada trasera": {"tipo": "repeticiones", "calorias": 6},
        "Elevaciones laterales": {"tipo": "repeticiones", "calorias": 6},
        "Sentadilla sumo": {"tipo": "repeticiones", "calorias": 7},
        "Abducción de cadera acostada": {"tipo": "repeticiones", "calorias": 6}
    },
    "Cuádriceps-Pantorrillas": {
        "Sentadillas": {"tipo": "repeticiones", "calorias": 8},
        "Zancadas": {"tipo": "repeeticiones", "calorias": 7},
        "Elevación de talones": {"tipo": "repeticiones", "calorias": 5},
        "Sentadilla con salto": {"tipo": "repeticiones", "calorias": 9},
        "Paso al frente con mochila": {"tipo": "repeticiones", "calorias": 7}
    }
}

def generar_rutina(grupo, nivel):
    rutina = []
    
    if nivel == "facil":
        repeticiones = [6, 8]
        tiempos = [20, 30] 
        descansos = [20, 30]
        series_rango = [2, 3]
        duracion_por_repeticiones = 2
    elif nivel == "medio":
        repeticiones = [10, 12]
        tiempos = [30, 40]
        descansos = [30, 40]
        series_rango = [3, 4]
        duracion_por_repeticiones = 2.5
    elif nivel == "dificil":
        repeticiones = [15, 20]
        tiempos = [40, 60]
        descansos = [40, 60]
        series_rango = [4, 5]
        duracion_por_repeticiones = 3
    else:
        return [], 0, 0

    seleccionados = random.sample(list(ejercicios[grupo].keys()), k=4)
    total_calorias = 0
    tiempo_total = 0

    for ejercicio in seleccionados:
        datos = ejercicios[grupo][ejercicio]
        tipo = datos["tipo"]
        calorias_minuto = datos["calorias"]

        series = random.randint(series_rango[0], series_rango[1])

        if tipo == "reps" or tipo == "repeticiones":
            reps = random.randint(repeticiones[0], repeticiones[1])
            duracion_por_serie = reps * duracion_por_repeticiones
            valor = f"{series} series de {reps} repeticiones"
        else:
            tiempo = random.randint(tiempos[0], tiempos[1])
            duracion_por_serie = tiempo
            valor = f"{series} series de {tiempo} segundos"

        calorias = (duracion_por_serie / 60) * calorias_minuto * series
        total_calorias += calorias

        descanso = random.randint(descansos[0], descansos[1])
        tiempo_total += (duracion_por_serie * series) + (descanso * (series - 1))

        rutina.append((ejercicio, valor, descanso, calorias, duracion_por_serie * series))
    
    return rutina, total_calorias, tiempo_total

def menu():
    while True:
        print(Fore.BLUE + "\n===  RUTINAS DE EJERCICIOS POR GRUPO MUSCULAR ===")
        print(Fore.CYAN + "1. Bíceps - Tríceps")
        print("2. Abdomen - Espalda")
        print("3. Hombro - Pecho")
        print("4. Glúteos")
        print("5. Cuádriceps - Pantorrillas")
        print("6. Salir")
        
        opcion = input(Fore.YELLOW + "¿Cuál grupo muscular quieres entrenar hoy? Elige una opción (1-6): ")
        
        grupos = {
            "1": "Bíceps-Tríceps",
            "2": "Abdomen-Espalda",
            "3": "Hombro-Pecho",
            "4": "Glúteos",
            "5": "Cuádriceps-Pantorrillas"
        }
        
        if opcion in grupos:
            nivel = input(Fore.MAGENTA + "Elige el nivel de dificultad (facil, medio, dificil): ").lower()
            rutina, total_calorias, tiempo_total = generar_rutina(grupos[opcion], nivel)

            if not rutina:
                print(Fore.RED + "Nivel inválido.")
                continue

            print(Fore.BLUE + f"\n=== Rutina para {grupos[opcion]} ===\n")
            for ejercicio, valor, descanso, calorias, duracion in rutina:
                print(Fore.GREEN + f"- {ejercicio}: " + Fore.WHITE + f"{valor} " +
                      Fore.YELLOW + f"(descanso {descanso} seg entre series) | ~{calorias:.1f} cal")

            print(Fore.CYAN + f"\nCalorías quemadas con la rutina: {total_calorias:.1f} cal")
            print(Fore.CYAN + f"Tiempo total estimado: {tiempo_total // 60} min {tiempo_total % 60} seg\n")
        
        elif opcion == "6":
            print(Fore.MAGENTA + "\n¡Gracias por entrenar conmigo! ¡Nos vemos mañana para seguir progresando!")
            break
        else:
            print(Fore.RED + "Opción inválida, intenta otra vez.\n")

menu()