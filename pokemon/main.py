from clases.pokemon import Pokemon

equipo = []
acciones = 0


def registrar_accion():
    """Usa 'global' para MODIFICAR una variable global."""
    global acciones
    acciones += 1


def pedir_entero(mensaje, defecto):
    """Variable local: 'valor' solo existe dentro de la función."""
    valor = input(mensaje).strip()
    return int(valor) if valor.isdigit() else defecto


def elegir_pokemon(mensaje="Elige un Pokémon"):
    """Muestra la lista y devuelve el Pokémon elegido (o None)."""
    if not equipo:
        print(" No tienes Pokémon todavía.")
        return None
    for i, p in enumerate(equipo, 1):
        print(f"  {i}. {p.nombre} (Nv {p.nivel})")
    opcion = input(f"{mensaje} (número): ").strip()
    if opcion.isdigit() and 1 <= int(opcion) <= len(equipo):
        return equipo[int(opcion) - 1]
    print("Opción inválida.")
    return None


def capturar():
    nombre = input("Nombre: ").strip().title()
    tipo = input("Tipo: ").strip().title()
    if not nombre or not tipo:
        print("Nombre y tipo son obligatorios.")
        return
    ataque = pedir_entero("Ataque inicial (Enter = 10): ", 10)
    defensa = pedir_entero("Defensa inicial (Enter = 10): ", 10)
    salud = pedir_entero("Salud inicial (Enter = 50): ", 50)
    equipo.append(Pokemon(nombre, tipo, ataque, defensa, salud))


def entrenar():
    p = elegir_pokemon("¿A quién entrenar?")
    if p:
        stats = input("Estadísticas (ataque, defensa, salud) separadas por coma "
                      "[Enter = todas]: ")
        lista = [s.strip() for s in stats.split(",") if s.strip()]
        p.entrenar(*lista)  # desempaquetado de lista -> *args


def ver_info():
    if not equipo:
        print("No tienes Pokémon todavía.")
        return
    for p in equipo:
        p.mostrar_info()


def atacar():
    if len(equipo) < 2:
        print("Necesitas al menos 2 Pokémon para combatir.")
        return
    print("Atacante:")
    atacante = elegir_pokemon()
    print("Objetivo:")
    objetivo = elegir_pokemon()
    if atacante and objetivo:
        if atacante is objetivo:
            print("Un Pokémon no puede atacarse a sí mismo.")
        else:
            atacante.atacar(objetivo)


def liberar():
    p = elegir_pokemon("¿A quién liberar?")
    if p:
        equipo.remove(p)
        del p  


def demo_parametros():
    """Paso por valor vs. por referencia."""
    def cambiar_nivel(nivel):      
        nivel += 10

    def cambiar_pokemon(poke):     
        poke.nivel += 10

    p = elegir_pokemon("Pokémon para la demo")
    if p:
        print(f"Nivel original: {p.nivel}")
        cambiar_nivel(p.nivel)
        print(f"Tras pasar el int:      {p.nivel}  (sin cambios)")
        cambiar_pokemon(p)
        print(f"Tras pasar el objeto:   {p.nivel}  (¡cambió!)")


def menu():
    print("1. Capturar Pokémon ")
    print("2. Entrenar Pokémon ")
    print("3. Ver información de todos ")
    print("4. Calcular cuántos existen ")
    print("5. Liberar Pokémon ")
    print("6. Combatir ")
    print("7. Demo paso de parámetros ")
    print("0. Salir")
    return input("Elige una opción: ").strip()


def main():
    acciones_menu = {
        "1": capturar, "2": entrenar, "3": ver_info,
        "4": Pokemon.total_pokemons, "5": liberar,
        "6": atacar, "7": demo_parametros,
    }
    while True:
        opcion = menu()
        if opcion == "0":
            print(f"¡Hasta pronto! Acciones realizadas: {acciones}")
            break
        accion = acciones_menu.get(opcion)
        if accion:
            accion()
            registrar_accion()
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
