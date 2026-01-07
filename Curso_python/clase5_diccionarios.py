def login():
    """
    Simula un sistema de ingreso con reintentos infinitos
    usando un bucle while hasta que las credenciales sean correctas.
    
    """
    
    # 1. Base de Datos
    database = {
        "daniel": "code2026",
    }

    print("--- SECURITY SYSTEM ---")

    # 2. Bucle infinito para persistencia
    while True:
        # Solicitamos usuario
        usuario_input = input("\n INPUT THE USERNAME: ")

        # Verificamos existencia del usuario (Búsqueda en claves del hash map)
        if usuario_input in database:
            
            password_input = input("INPUT THE PASSWORD: ")
            
            # Verificamos credenciales
            if password_input == database[usuario_input]:
                print(f"¡WELCOME, {usuario_input}! ACCESS GRANTED.")
                # 'return' finaliza la ejecución de TODA la función, rompiendo el bucle.
                return True 
            else:
                print("Error: PASSWORD INCORRECT")
                # No hay 'return' ni 'break', por lo que el bucle while se repite
                
        else:
            print("Error: THE USERNAME DOES NOT EXIST IN THE DATABASE, REPEAT THE PROCESS")
            # El bucle while se repite nuevamente
            
            
def analyzetemperature():
        temperature=float(input("Enter Temperature: "))
        print(f"Saved Temperature: {temperature}°C")
        
        if temperature > 35:
            #Activando Ventiladores y Nebulizadores
            print("Activating Fans And Nebulizers")
        
        elif temperature < 10:
            #Activando calefaccion 
            print("Activating Heating")
        
        else:
            #Sistema estable
            print("Stable system")

def analyzehumidity():
        while True:
            try:
                # ingrese la humedad del suelo
                humidity = int(input("Enter the humidity:"))
                if 0 <= humidity <= 100:
                    print(f" Saved humidity {humidity}%")
                    break
                else:
                    print("❌ enter the values from 0 to 100 ")  # ✅ Mensaje para rango
                    
            except ValueError:
                print("❌enter the values from 0 to 100")
     
        if humidity < 30:
            print("Starting irrigation ")
        
        elif humidity >= 30:
            print("Optimal Humidity")
            
def start_data_logging():
    print("--- Start data logging---")
    
    # PASO 1: ¿Cuántos datos?
    amount = int(input("Amount of data to take:  "))
    
    # PASO 2: Lista vacía
    buffer_temperature = []
    
    # PASO 3: Bucle for
    for i in range(amount):
        # La variable 'i' va contando (0, 1, 2...)
        reading = float(input(f"Enter the temperature sample #{i+1}: "))
        
        # Agregamos a la lista
        buffer_temperature.append(reading)
        print("   >> Date saved in the RAM.")

    # PASO 4: Cálculos (Ya fuera del bucle)
    average = sum(buffer_temperature) / len(buffer_temperature)
    maximum = max(buffer_temperature)
    minimum = min(buffer_temperature)

    # PASO 5: Mostrar resultados
    print("\n--- REPORTE FINAL ---")
    print(f"Total Samples: {len(buffer_temperature)}")
    print(f"Average: {average}°C")
    print(f"Maximum: {maximum}°C")
    print(f"Minimum: {minimum}°C")
    
    
    


login()
    
    
    
while True:
    print("\n=== AUTONOMOUS WINTER CONTROLLER ===")
    print("1. Monitor Temperature")
    print("2. Monitor Humidity")
    print("3. Start Data Logging")
    print("4. OFF THE SYSTEM")
    
    opcion = input("CHOSE (1-4): ")
    
    if opcion == "1":
        analyzetemperature()
         
    elif opcion == "2":
        analyzehumidity()
        
    elif opcion == "3":
        start_data_logging()
        
    elif opcion == "4":
        print("¡SEE YOU LATER!")
        break
    
    else:
        print("❌ ERROR IN THE COMAND")
        
        


