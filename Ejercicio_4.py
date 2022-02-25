# La Reglas del juego. Debes lanzar un par de dados. Si la suma de las 
# caras es un 8, ganas. Si sale 7, pierdes. Si no hasalido, 
# ni 8, ni 7, puedes seguir lanzando. Si sale 8 ganas, pero 
# si en algún otro lanzamiento sale 7, pierdes.


import psycopg2
import random

while True:
    try:
        conexion = psycopg2.connect(
            host = "localhost",
            port = "5432",
            user = "postgres",
            password = "12345abc",
            dbname = "Tarea_Preparatoria"
        )


        print("""
        1) Jugar
        2) Ver historial""")

        nn1 =int(input("Selecione un opcion: "))

        if nn1==1:
            x = random.randrange(6)
            y = random.randrange(6)

            z = x+y
            w=0
            pulsador = input("Presione la letra j y luego enter para tira los dados: ")
            if pulsador=="j":
                if z==8:
                    print("Dado 1: ",x)
                    print("Dado 2: ",y)
                    print("Felicidades a gando el juego obtuvo un: ",z)

                elif z==7:
                    print("Dado 1: ",x )
                    print("Dado 2: ",y)
                    print("Has perdido el juego")
                else:
                    print("Dado 1: ",x)
                    print("Dado 2: ",y)
                    print("Vuelva a jugar")


                cursor = conexion.cursor()
                cursor.execute("INSERT INTO ejer4(dado1,dado2,resultado) VALUES(%s,%s,%s);",(x,y,z))
                conexion.commit()
                cursor.close()
                conexion.close()

        if nn1==2:
            cursor = conexion.cursor()
            SQL = "SELECT*FROM ejer4;"
            cursor.execute(SQL)
            valores = cursor.fetchall()
            print(valores)
            cursor.close()
            conexion.close()
    except:
        print("Se produjo un error, se recomienda reiniciar el juego")
                    
