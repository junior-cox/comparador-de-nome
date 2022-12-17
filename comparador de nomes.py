# esse codigo compara os nomes#
while(True):
   nomepri=input('nome primario //')
   b=bool(True)
   while(b):
      nomesec=input('digite o nome secundario //')
      if(len(nomepri)==len(nomesec)):
          print('os nomes tem o mesno tamanho')
      if(len(nomepri)>len(nomesec)):
          print('o nome primario e maior ')
      if(len(nomepri)<len(nomesec)):
          print('o mone segundario e maior ')
      print('o primario tem {} e o secudario tem {}'.format(len(nomepri),len(nomesec)))
      a=input('voce que troca o primario')
      if(a=='sim'):
         b=False
#altor junior h o #