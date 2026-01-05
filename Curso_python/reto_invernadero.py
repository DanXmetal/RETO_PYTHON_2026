
while True:
    print("\n=== CONTROLADOR DE INVIERNO AUTONOMO ===")
    print("1. Monitorear Temperatura")
    print("2. Controlar Riego")
    print("3. Apagar Sistema")
    
    opcion = input("Elige (1-3): ")
    
    if opcion == "1":
        temperatura=float(input("INGRESE LA TEMPERATURA: "))
        print(f"Temperatura guardada: {temperatura}°C")
        
        if temperatura > 35:
            print("Activando Ventiladores y Nebulizadores")
        
        elif temperatura < 10:
            print("ADVERTENCIA: Activando Calefacción")
        
        else:
         print("SISTEMA ESTABLE")
         
         
    elif opcion == "2":
        while True:
            try:
                humedad = int(input("HUMEDAD DEL SUELO (0-100): "))
                if 0 <= humedad <= 100:
                    print(f"HUMEDAD guardada: {humedad}%")
                    break
                else:
                    print("❌ SOLO VALORES ENTRE 0% Y 100%")  # ✅ Mensaje para rango
            except ValueError:
                print("❌ SOLO UN VALOR DE 0% A 100%")
     
        if humedad < 30:
            print("INICIANDO RIEGO ")
        
        elif humedad >= 30:
            print("HUMEDAD OPTIMA")
        
        
        
    elif opcion == "3":
        print("¡Adiós!")
        break
    
    
    else:
        print("❌ ERROR DE COMANDO")