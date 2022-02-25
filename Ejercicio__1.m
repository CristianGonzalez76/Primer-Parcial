clc;clear;

try
  pkg load database
  conn = pq_connect(setdbopts('dbname','Tarea_Preparatoria','host','localhost','port','5432','user','postgres','password','12345abc'));
	
  fprintf('Introduzca su edad \n');
  fprintf('Ejmplo : Dia: 15  Mes: 14 Año: 1998 \n ')
	dia1 = input('Ingrese el dia de su cumpleaños: ');
  mes1 = input('Ingrese el numero de su mes de nacimiento: ');
  year1 = input('Ingrese el año en que nacio: ');
  printf('Usted nacio el dia %i del mes %i y año %i \n', dia1, mes1, year1);
  edad=2022-year1;
  
  if (mes1<2)
    printf('Usted ya cumplio %i años ', edad);
    concat=strcat(' Usted nacio el dia ', num2str(dia1), ' del mes ', num2str(mes1),' y año ',num2str(year1));
	  concat1=strcat(' Ya cumplio ', num2str(edad), ' años');
    N = pq_exec_params(conn,"insert into ejer1(dia, mes,ano,edad,celebro) values($1,$2,$3,$4,$5);",{dia1,mes1,year1,edad,'Ya cumplio'});
  elseif (mes1==2)&(dia<=24)
    printf('Usted ya cumplio %i años ', edad);
    concat=strcat(' Usted nacio el dia ', num2str(dia1), ' del mes ', num2str(mes1),' y año ',num2str(year1));
	  concat1=strcat(' Ya cumplio ', num2str(edad), ' años');
    N = pq_exec_params(conn,"insert into ejer1(dia, mes,ano,edad,celebro) values($1,$2,$3,$4,$5);",{dia1,mes1,year1,edad,'Ya cumplio'});
  
  elseif (mes1>2)
    printf('Usted ya no ha cumplido %i años', edad);
    concat=strcat(' Usted nacio el dia ', num2str(dia1), ' del mes ', num2str(mes1),' y año ',num2str(year1));
	  concat1=strcat(' Ya cumplio ', num2str(edad), ' años');
    N = pq_exec_params(conn,"insert into ejer1(dia, mes,ano,edad,celebro) values($1,$2,$3,$4,$5);",{dia1,mes1,year1,edad,'Ya no ha cumplido'});
  
  elseif (mes1==24)&(dia1>24)
    printf('Usted ya no ha cumplido %i años', edad);
    concat=strcat(' Usted nacio el dia ', num2str(dia1), ' del mes ', num2str(mes1),' y año ',num2str(year1));
	  concat1=strcat(' Ya cumplio ', num2str(edad), ' años');
    N = pq_exec_params(conn,"insert into ejer1(dia, mes,ano,edad,celebro) values($1,$2,$3,$4,$5);",{dia1,mes1,year1,edad,'Ya no ha cumplido'});

  endif


catch
	printf("Ha ocurrido un error")
end_try_catch
