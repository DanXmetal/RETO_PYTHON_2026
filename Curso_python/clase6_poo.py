class Nino:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad  # NOTA: Recibimos número entero (sin comillas)

    def presentarse(self):
        print(f"Soy {self.nombre} y tengo {self.edad} años.")

    # --- NUEVA FUNCIÓN MÁGICA ---
    def cumplir_anos(self):
        print(f"🎂 ¡Feliz cumpleaños {self.nombre}!")
        self.edad = self.edad + 1  # Modificamos SU propia variable

# --- PRUEBA ---

juan = Nino("Juan", 14)
maria = Nino("Maria", 10)

print("--- ANTES ---")
print(f"Edad de Juan: {juan.edad}")

# Juan cumple años (Ejecutamos la función SOLO en Juan)
juan.cumplir_anos()

print("\n--- DESPUÉS ---")
print(f"Edad de Juan: {juan.edad}")   # Debería ser 15
print(f"Edad de Maria: {maria.edad}") # Debería seguir en 10