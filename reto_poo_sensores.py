import random

# 1. LA CLASE (El diseño del componente)
class Sensor:
    def __init__(self, tipo, ubicacion):
        self.tipo = tipo
        self.ubicacion = ubicacion
        self.valor = 0.0

    def medir(self):
        print(f"📡 Sensor de {self.tipo} ({self.ubicacion}) activado...")
        # Simulamos lectura aleatoria
        self.valor = random.uniform(10.0, 40.0)
    
    def obtener_reporte(self):
        print(f"   >> Lectura Final: {self.valor:.2f}")

# --- ZONA DE INSTALACIÓN (Creación de Objetos) ---

print("--- INICIANDO SISTEMA DE SENSORES ---")

# Creamos los 5 objetos físicos en memoria RAM
s_techo = Sensor("Temperatura", "Techo")
s_suelo = Sensor("Humedad", "Suelo")
s_entrada = Sensor("Luminosidad", "Puerta Principal")
s_piscina = Sensor("Ph", "Piscina")
s_jardin = Sensor("Luminosidad", "Jardin")

# --- ZONA DE AUTOMATIZACIÓN (La Optimización) ---

# 1. Agrupamos todos los objetos en una LISTA
# Ahora 'lista_sensores' contiene las referencias a los 5 objetos.
lista_sensores = [s_techo, s_suelo, s_entrada, s_piscina, s_jardin]

print(f"\n⚡ Procesando {len(lista_sensores)} dispositivos en tiempo real...\n")

# 2. Bucle de Control Masivo
# La variable 'sensor_x' va tomando la forma de cada objeto en la lista, uno por uno.
for sensor_x in lista_sensores:
    sensor_x.medir()           # Orden genérica (polimorfismo básico)
    sensor_x.obtener_reporte() # Reporte genérico
    print("-" * 30)            # Separador visual

print("✅ Ciclo de lectura finalizado.")