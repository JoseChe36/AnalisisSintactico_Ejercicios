import socket
import re


socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip = "127.0.0.1"
port = 8001
socket_server.bind((ip,port))
socket_server.listen(5) 

print(f"\n\nServer Listening on {ip}:{port}")

salir = False
while salir == False:
    conexion, address = socket_server.accept()
    print ("La conexión ha sido establecida")
    archi1=open("DocApoyo.java","r")
    contenido=archi1.read()
    print(contenido)
    test_str = contenido
    archi1.close()            

    while True:
        message = conexion.recv(1024)
        message = message.decode()
        print(message)    

        if message == 'exit' or message == 'Exit' or message == 'EXIT':
            message = 'Adios...'
            conexion.send(message.encode())
            print("\n")
            salir = True
            break

        elif message == 'entrar' or message == 'Entrar' or message == 'ENTRAR':                                         
            message = ("Elija una opcion de la lista para validar las gramáticas del código fuente:\n\n1.- Sentencia de asignación."
                        "\n2.- Operaciones aritméticas básicas.\n3.- Expresiones booleanas básicas.\n4.- Formulas complejas.\n"
                        "5.- Estructura de control.\n\n")
            conexion.send(message.encode())
        
        elif message == '1':
            regex = r'(=)'                             
            matches = re.finditer(regex, test_str, re.MULTILINE)

            for matchNum, match in enumerate(matches, start=1):
                    
                    message = ("Se encontraron --> {matchNum} <-- coincidencias en el mensaje. ".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))                                           
            if message == '1':
                 message = ("Se encontraron --> 0 <-- coincidencias en el mensaje. ")                                                           
            conexion.send(message.encode())            

        elif message == '2':
            regex = r'([+]|[*]|-|/)'            
            matches = re.finditer(regex, test_str, re.MULTILINE)

            for matchNum, match in enumerate(matches, start=1):
                    
                    message = ("Se encontraron --> {matchNum} <-- coincidencias en el mensaje. ".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))                                                      
            if message == '1'  or message == '2':
                 message = ("Se encontraron --> 0 <-- coincidencias en el mensaje. ")                                                           
            conexion.send(message.encode())


        elif message == '3':
            regex = r'(!=|>=|<=|==|<|>|<)'                                   
            matches = re.finditer(regex, test_str, re.MULTILINE)

            for matchNum, match in enumerate(matches, start=1):
                    
                    message = ("Se encontraron --> {matchNum} <-- coincidencias en el mensaje. ".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))                                       
            if message == '1'  or message == '3':
                 message = ("Se encontraron --> 0 <-- coincidencias en el mensaje. ")                                                           
            conexion.send(message.encode()) 


        elif message == '4':
            regex = r'(//|%)'                                      
            matches = re.finditer(regex, test_str, re.MULTILINE)

            for matchNum, match in enumerate(matches, start=1):
                    
                    message = ("Se encontraron --> {matchNum} <-- coincidencias en el mensaje. ".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))                                                        
            if message == '1'  or message == '4':
                 message = ("Se encontraron --> 0 <-- coincidencias en el mensaje. ")                                                           
            conexion.send(message.encode())


        elif message == '5':
            regex = r'(?i)(\W|^)(if|while|for|or|and|xor|print|else|elif|is|in|not|break|pass|continue)(\W|$)'                                 
            matches = re.finditer(regex, test_str, re.MULTILINE)

            for matchNum, match in enumerate(matches, start=1):
                    
                    message = ("Se encontraron --> {matchNum} <-- coincidencias en el mensaje. ".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))                                        
            if message == '1' or message == '5':
                 message = ("Se encontraron --> 0 <-- coincidencias en el mensaje. ")                                                           
            conexion.send(message.encode())                            

        else:
            message = 'Favor de elegir una opción de la lista'            
            conexion.send(message.encode())

conexion.close()
print("Servidor Finalizado")