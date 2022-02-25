#Realice un programa que ingrese Un número entre 1 y 999 e indique por cuantas unidades, 
# decenas y centenas está formado el número.


import psycopg2

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
        1) Ejecutar Programa
        2) Ver el historial""")

        nn1 = int(input("Seleccione un opcion: "))

        if nn1==1:
            numero = int(input ("Ingrese un valor entre 1 y 999   "))


            centenas=(numero%1000-numero%100)//100
            decenas=(numero%100-numero%10)//10
            unidades=numero%10
            print ("Valor de centenas: " , centenas)
            print ("Valor de decenas: " , decenas)
            print ("Valor de unidades: ", unidades)
            print ()

            cursor = conexion.cursor()
            cursor.execute("INSERT INTO ejer3(numero,centenas,decenas,unidades) VALUES(%s,%s,%s,%s);",(numero,centenas,decenas,unidades))
            conexion.commit()
            cursor.close()
            conexion.close()
        

        elif nn1==2:
            cursor = conexion.cursor()
            SQL = "SELECT*FROM ejer3;"
            cursor.execute(SQL)
            valores = cursor.fetchall()
            print(valores)
            cursor.close()
            conexion.close()
    except:
        print("Error: Posiblemete introdujo un caracter no numerico")