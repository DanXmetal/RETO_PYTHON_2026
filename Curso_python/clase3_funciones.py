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



while True:
    print("\n=== AUTONOMOUS WINTER CONTROLLER ===")
    print("1. Monitor Temperature")
    print("2. Monitor Humidity")
    print("3. OFF THE SYSTEM")
    
    opcion = input("CHOSE (1-3): ")
    
    if opcion == "1":
        analyzetemperature()
         
    elif opcion == "2":
        analyzehumidity()
        
    elif opcion == "3":
        print("¡SEE YOU LATER!")
        break
    
    else:
        print("❌ ERROR IN THE COMAND")
        
        


