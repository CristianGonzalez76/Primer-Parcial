clc;clear;

try
	fprintf('Determinar el angulo restante de un triangulo \n');
	a = input('Ingrese el primer angulo: ');
  b = input('Ingrese el segundo angulo: ');
  c = 180-a-b;
  pkg load database
  conn = pq_connect(setdbopts('dbname','Tarea_Preparatoria','host','localhost','port','5432','user','postgres','password','12345abc'));

    printf('El angulo es igual a %i \n', c);
		concat=strcat('El angulo flatante es c=', num2str(c));
		N = pq_exec_params(conn,"insert into ejer2(primer_angulo, segundo_angulo, angulo_resultante) values($1,$2,$3);",{a,b,c});
	
catch
	printf("Ha ocurrido un error \n");
end_try_catch
