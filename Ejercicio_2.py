import psycopg2

while True:

    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "12345abc",
        dbname = "Tarea_Preparatoria"
    )

    print("""
    1) Abrir programa
    2) Ver el historial""")

    nn1 = int(input("Seleccione una opcion: "))

    if nn1==1:

        a = int(input("Primer angulo: "))
        b = int(input("Segundo angulo: "))

        c = 180-a-b
        print("El angulo es: ",c)

        cursor = conexion.cursor()
        cursor.execute("INSERT INTO ejer2(primer_angulo,segundo_angulo,angulo_resultante) VALUES(%s,%s,%s);",(a,b,c))
        conexion.commit()
        cursor.close()
        conexion.close()

    elif nn1==2:
        cursor = conexion.cursor()
        SQL = "SELECT*FROM ejer2;"
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
        cursor.close()
        conexion.close()