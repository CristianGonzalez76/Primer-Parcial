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
        1) Abrir programa
        2) Ver historial""")

        nn1 = int(input("Seleccione una opcion: "))

        if nn1==1:
            print("Introduzca su fecha de nacimiento")
            print("Ejemplo:   Dia: 5   Mes: 2  Año: 2000")


            dia1 = int(input("Dia: "))
            mes1 = int(input("Mes: "))
            year1 = int(input("Año: "))

            dia2 = 24  #coloque la fecha de hoy
            mes2 = 2   # pero se puede modificar para recibir la fecha de nacimiento y la fecha en la que se esta haciendo la consulta
            year2 = 2022

            Edad = year2-year1

            x1=0
            x2=0

            if mes1<mes2:
                print("Esta persona ya cumplio años")
                x1=Edad
                print("Esta persona tiene ", x1, " años")
                x2 = "Esta pesona ya cumplio años"

            elif (mes1==mes2) & (dia1<=dia2):
                print("Esta persona ya cumplio años")
                x1=Edad
                print("Esta persona tiene ", x1," años")
                x2 = "Esta persona ya cumplio años"
            
            elif (mes1>mes2):
                print("Esta persona aun no cumple años")
                x1=Edad-1
                print("Esta persona tiene ",x1, " años")
                x2 = "Esta persona aun no cumple años"
            elif (mes1==mes2)&(dia1>dia2):
                print("Esta persona aun no cumple años")
                x1=Edad-1
                print("Esta persona tiene ", x1," años")
                x2 = "Esta persona aun no cumple años"

            cursor = conexion.cursor()
            cursor.execute("INSERT INTO ejer1(dia,mes,ano,edad,celebro) VALUES(%s,%s,%s,%s,%s);",(dia1,mes1,year1,x1,x2))
            conexion.commit()
            cursor.close()
            conexion.close()


        elif nn1==2:
            cursor = conexion.cursor()
            SQL = "SELECT*FROM ejer1;"
            cursor.execute(SQL)
            valores = cursor.fetchall()
            print(valores)
            cursor.close()
            conexion.close()
    except:
        print("Error: Revise la informacion que ha proporcionado")


        
