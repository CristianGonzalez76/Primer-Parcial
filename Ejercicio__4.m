clc;clear;

try
  pkg load database
  conn = pq_connect(setdbopts('dbname','Tarea_Preparatoria','host','localhost','port','5432','user','postgres','password','12345abc'));
  
  x1 = randperm(6)
  x2 = randperm(6)
  
  x3 = x1+x2
  
  if x3==8
    print('Ha ganado el juego')
    
   elseif x3==7
    print('Ha perdido el juego')
    
   else
    print('Vuealva a jugar otra vez')
    
  endif
  N = pq_exec_params(conn,"insert into ejer4(dado1, dado2,resultado) values($1,$2,$3);",{x1,x2,x3,edad});
  
  
  N=pq_exec_params(conn,'select * from ejer4;')
  
  
catch
  print('Ocurrio un error, reinicie el juego')
 end_try_catch
