class Pokemon:
    """Representa a un Pokémon con estadísticas básicas de combate."""

   
    _creados = 0   
    _vivos = 0     

    ESTADISTICAS = ("ataque", "defensa", "salud")

    def __init__(self, nombre, tipo, ataque=10, defensa=10, salud=50):
    
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = 1
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud

        Pokemon._creados += 1
        Pokemon._vivos += 1
        print(f"¡Un {self.nombre} salvaje de tipo {self.tipo} ha sido capturado! ")

    def __del__(self):
        Pokemon._vivos -= 1
        print(f"{self.nombre} ha sido liberado ")

    # Métodos de instancia
    def entrenar(self, *args):
        """Sube de nivel y mejora estadísticas.

        Sobrecarga con *args:
            entrenar()                      -> mejora ataque, defensa y salud
            entrenar("ataque")              -> mejora solo ataque
            entrenar("ataque", "salud")     -> mejora ataque y salud
        """
        a_mejorar = args if args else self.ESTADISTICAS
        mejoras = {"ataque": 3, "defensa": 2, "salud": 10}

        self.nivel += 1
        for stat in a_mejorar:
            stat = stat.lower()
            if stat in mejoras:
                setattr(self, stat, getattr(self, stat) + mejoras[stat])
            else:
                print(f"Estadística desconocida: '{stat}' (se ignora)")

        print(f"{self.nombre} subió al nivel {self.nivel} "
              f"(mejoró: {', '.join(a_mejorar)})")

    def mostrar_info(self):
        print(f" {self.nombre:<12} | Tipo: {self.tipo:<10} | Nv: {self.nivel:<3} | "
              f"ATQ: {self.ataque:<4} | DEF: {self.defensa:<4} | HP: {self.salud}")

    def atacar(self, objetivo):
        """Ataca a otro Pokémon.

        'objetivo' es un objeto (mutable): se pasa por referencia, así que
        al modificar objetivo.salud el cambio se ve fuera del método.
        """
        if self.salud <= 0:
            print(f"{self.nombre} está debilitado y no puede atacar.")
            return
        if objetivo.salud <= 0:
            print(f"{objetivo.nombre} ya está debilitado.")
            return

        dano = max(1, self.ataque + self.nivel - objetivo.defensa // 2)  # variable local
        objetivo.salud = max(0, objetivo.salud - dano)

        print(f"{self.nombre} ataca a {objetivo.nombre} y causa {dano} de daño. "
              f"(HP restante: {objetivo.salud})")
        if objetivo.salud == 0:
            print(f"¡{objetivo.nombre} se ha debilitado!")

    # Método de clase
    
    @classmethod
    def total_pokemons(cls):
        """Muestra cuántos Pokémon han sido creados."""
        print(f"Pokémon creados en total: {cls._creados} | "
              f"Actualmente en tu equipo: {cls._vivos}")
        return cls._creados
