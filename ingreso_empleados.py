from datetime import datetime 


def menu_principal():
    print("MENU")

    print("1 - Ingreso Empleado: \n")

    print("2 - Egreso de Empleado:\n")

    print("3 - Ver los ultimos 5 Registros:\n")

    print("4 - Salir del sistema \n")

def guardar_datos_ingreso(ingreso):
    try: 
        with open("personal.txt","a") as f:
            f.write(datetime.now().strftime("%d/%m/%y %H:%M:%S "))
            f.write( f" - {ingreso} - ingreso  \n")
            print("ingreso con exito")            
            f.close()
    except FileNotFoundError:
        print("no se ha podido grabar")

def guardar_datos_egreso(egreso):
    try: 
        with open("personal.txt","a") as f:
            f.write(datetime.now().strftime("%d/%m/%y %H:%M:%S")) 
            f.write(f" - {egreso} - egreso \n")
            print("Ingreso con exito")           
            f.close()
    except FileNotFoundError:
        print("no se ha podido grabar")       

def abrir_registros(registros):
    try:
        with open("personal.txt","r") as f:
            registros=f.readlines()
        for r in registros:
            lista_registros.append(r.strip()) 
            
                       
        return lista_registros    
    except FileNotFoundError:
        print("no se encontraron registros")

menu_principal()

ingreso=""
egreso=""
lista_registros=[]

intentos=0


while intentos<=5:
    menu_principal()
    opcion=int(input("=======>>>"))
    
    if opcion==1:
        ingreso=str(input("ingrese su nombre: "))
        intentos=intentos+1
        if ingreso.isalpha():
            guardar_datos_ingreso(ingreso)
            
            
        else:
            print("incorrecto, solo se permiten nombres")    
            
       
        
       
    elif opcion==2:
        egreso=str(input("ingrese su nombre: "))
        intentos=intentos+1
        if egreso.isalpha():
            guardar_datos_egreso(egreso) 
                        
        else:
            print("incorrecto, solo se permiten nombres")  
    
    elif opcion==3:
        registros=True
        intentos=intentos+1
        if registros:
            (abrir_registros(registros))
            if lista_registros==[]:
                print("no hay registros")  
            else:      
                for reg in lista_registros:
                    print(reg)       
                
                
                
    else:
        print("saliendo")
        break
    
 
                


 

