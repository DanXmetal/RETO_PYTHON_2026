
while True:
    print("\n=== CONTROLADOR DE INVIERNO AUTONOMO ===")
    print("1. Monitorear Temperatura")
    print("2. Controlar Riego")
    print("3. Apagar Sistema")
    
    opcion = input("Elige (1-3): ")
    
    if opcion == "1":
        TEMP=float(input("INGRESE LA TEMPERATURA: "))
        print(f"Temperatura guardada: {TEMP}°C")
        
        if TEMP > 35:
            print("Activando Ventiladores y Nebulizadores")
        
        elif TEMP < 10:
            print("ADVERTENCIA: Activando Calefacción")
        
        else:
         print("SISTEMA ESTABLE")
         
         
    elif opcion == "2":
        while True:
            try:
                HUM = int(input("HUMEDAD DEL SUELO (0-100): "))
                if 0 <= HUM <= 100:
                    print(f"HUMEDAD guardada: {HUM}%")
                    break
                else:
                    print("❌ SOLO VALORES ENTRE 0% Y 100%")  # ✅ Mensaje para rango
            except ValueError:
                print("❌ SOLO UN VALOR DE 0% A 100%")
     
        if HUM < 30:
            print("INICIANDO RIEGO ")
        
        elif HUM >= 30:
            print("HUMEDAD OPTIMA")
        
        
        
    elif opcion == "3":
        print("¡Adiós!")
        break
    
    
    else:
        print("❌ ERROR DE COMANDO")