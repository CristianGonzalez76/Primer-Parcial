clc;clear;

try
	fprintf('Determinar cuantas unidades, decenas y centenas tiene el numero \n');
	n1 = input('Ingrese un numero entre 0 y 999: ');
  
  
  pkg load database
  conn = pq_connect(setdbopts('dbname','Tarea_Preparatoria','host','localhost','port','5432','user','postgres','password','12345abc'))

	if (n1<=999)&&(n1>=0)
    c=fix(n1/100);
    d=fix((n1 -c*100)/10);
    u=fix(n1-c*100-d*10);

    printf('El numero %i tiene: \n', n1);
    printf('Centenas = %i \n ',c);
    printf('Decenas = %i \n' ,d);
    printf('unidades = %i \n', u);
		N = pq_exec_params(conn,"insert into ejer3(numero, centenas,decenas,unidades) values($1,$2,$3,$4);",{n1,c,d,u});
	else
		printf('Por favor ingrese un numero entre 0 y 999');
	endif
catch
	printf("Ha ocurrido un error \n");
end_try_catch
