import random #---------------------------------------------------------------# Preparação
C = []
erro = []
#--------------------------------------------------------------------Crianco matriz---------------------------------------------------------------#
def matriz_borda(nlinhas: int, ncolunas: int) -> list:
  M = []
  for i in range(nlinhas):
    linha = []
    for j in range(ncolunas):
      if i==0 or j==0 or i==nlinhas-1 or j==ncolunas-1: # borda
        linha.append("⬛")
      else:
        linha.append("⬜")
    M.append(linha)
  return M
x, y = int(input("Número de y? ")), int(input("Número de x? "))
x1 = x
y1 = y
M = matriz_borda(x, y)
#-------------------------------------------------------------------Uma saida aleatoria----------------------------------------------------------#
r = random.randrange(1, 5) #Escolhendo saida no lado
def criando_saida(M, r, x, y):
  while True: #---------------------------------------------------------------------#Verificando se frente de * é vazio
    try:
      if r == 1: #lado superior
        r = random.randrange(2, x-1)
        if M[0][r-1] == '⬛' and M[0][r+1] == '⬛' and M[1][r] == '⬜':
          M[0][r] = '🚪'
          break
      if r == 3: #lado inferior
        r = random.randrange(2, x-1)
        if M[-1][r-1] == '⬛' and M[0][r+2] == '⬛' and M[-2][r] == '⬜':
          M[-1][r] = '🚪'
          break
      if r == 2: #Direita de lado
        r = random.randrange(2, y-1)
        if M[r-1][-1] == '⬛' and M[r+2][-1] == '⬛' and M[r][-2] == '⬜':
          M[r][-1] = '🚪'
          break
      if r == 4: #Esquerda de lado
        r = random.randrange(2, y-1)
        if M[r-1][0] == '⬛' and M[r+2][0] == '⬛' and M[r][1] == '⬜':
          M[r][0] = '🚪'
          break
    except:
      pass
    return M
    
criando_saida(M, r, x, y)
#-------------------------------------------------------------------------------Construindo parede "L"-------------------------------------------------------#
def construindo(M, x, y, r, rl):
  if rl == 0:
    for ii in range(y-4):
      M[ii][r] = '⬛'
      if ii+3 == y:
        for ix in range(1):
          M[ii][r+ix] = '⬛'
  if rl == 1:
    ii = y-1
    while ii != 2:
      M[ii][r] = '⬛'
      ii -= 1
      if ii+3 == y:
        for ix in range(1):
          M[ii][r+ix] = '⬛'
  return M
if x >= 5 and y >= 5:       #-----------------------------------------------------------------# Aleatorio para colocar parede no dentro de borda
  rl = random.randrange(0,1)
  r = random.randrange(2, y-2)
  construindo(M, x, y, r, rl)
S = M
#-----------------------------------------------------------------------------------------------#Preparação com mapa de padrão
Ca = []
#---------------------------------------------------------------# Escolhendo uma posição aleatoria para @
while True:
  try:
    x = random.randint(1, x1-1)
    y = random.randint(1, y1-1)
    if S[y][x] == '⬜':
      S[y][x] = '🤖'
      break
  except IndexError:
    pass
#---------------------------------------------------------------#Visualizando matriz original
for item in S:
  print(''.join(item))
print(" ")
#---------------------------------------------------------------#Função de procurar coordenadas de x e y de @ e colocar na lista
def find(element, M):
  result = []
  for i in range(len(M)):
      for j in range(len(M[i])):
          if M[i][j] == element:
              result.append(i)
              result.append(j)
  return result
#---------------------------------------------------------------#Caminhando para oeste
def oeste(M):
  i=1
  while True:
    C = find('🤖', M)
    if M[C[0]][C[1]] == '🤖' and M[C[0]][(C[1])-1] == '⬛': ######
      rr = random.randint(1,4)                            #
      if rr == 1:                                         #
        leste(M)                                          #
      if rr == 2:                                         #
        sul(M)                                            #      É aleatorio para escolher uma direção para mover quando chegar na parede "X"
      if rr == 3:                                         #
        norte(M)                                          #
      if rr == 4:                                         #
        oeste(M)                                          #
      break                                               ######
    if M[-1][C[1]] == '🚪' and M[-2][C[1]] == '🤖':         #
      M[-1][C[1]] = '🤖'                                   #
      M[-2][C[1]] = '⬜'                                   #
      Ca.append("S")                                      #      É encontrar saída de lado inferior
      print("Encontrei uma saida!")                       #
      break                                               ######
    if M[0][C[1]] == '🚪' and M[1][C[1]] == '🤖':           #
      M[0][C[1]] = '🤖'                                    #
      M[1][C[1]] = '⬜'                                    #
      Ca.append("N")                                      #      É encontrar saída de lado superior
      print("Encontrei uma saida!")                       #
      break                                               ######
    else:                                                 #
      M[C[0]][C[1]] = '⬜'                                 #      Em loop, robô andando até abrir if acima
      M[C[0]][(C[1])-1] = '🤖'                             #
      Ca.append("O")                                      ######
    print(" ")                                            
    for item in S: #--------------------------------------#Visualizando matriz
      print(''.join(item))
#---------------------------------------------------------------#Caminhando para sul
def sul(M):
  i=1
  while True:
    C = find('🤖', M)
    if M[-1].count('🤖') == 1: #Aborte quando @ atravessa a parede de norte (segurança)
      break 
    if M[C[0]][C[1]] == '🤖' and M[(C[0])+1][(C[1])] == '⬛': ######
      rr = random.randint(1,4)                              #                  
      if rr == 1:                                           #
        leste(M)                                            #
      if rr == 2:                                           #
        sul(M)                                              #      É aleatorio para escolher uma direção para mover quando chegar na parede "X"
      if rr == 3:                                           #
        norte(M)                                            #
      if rr == 4:                                           #
        oeste(M)                                            #
      break                                                 ######
    if M[C[0]][-1] == '🚪' and M[C[0]][-2] == '🤖':           #
      M[C[0]][-1] = '🤖'                                     #
      M[C[0]][-2] = '⬜'                                     #
      Ca.append("L")                                        #      É encontrar saída de lado direito
      print("Encontrei uma saida!")                         #
      break                                                 #
    if M[C[0]][0] == '🚪' and M[C[0]][1] == '🤖':             ######
      M[C[0]][0] = '🤖'                                      #
      M[C[0]][1] = '⬜'                                      #
      Ca.append("O")                                        #
      print("Encontrei uma saida!")                         #      É encontrar saída de lado esquerdo
      break                                                 #
    else:                                                   ######
      M[C[0]][C[1]] = '⬜'                                   #
      M[(C[0])+1][(C[1])] = '🤖'                             #      Em loop, robô andando até abrir if acima
      Ca.append("S")                                        #
    print(" ")                                              ###### 
    for item in S: #--------------------------------------#Visualizando matriz
      print(''.join(item))
#---------------------------------------------------------------#Caminhando para leste
def leste(M):
  i=1
  while True:
    C = find('🤖', M)
    if M[C[0]][C[1]] == '🤖' and M[(C[0])][(C[1])+1] == '⬛': ######
      rr = random.randint(1,4)                              #
      if rr == 1:                                           #
        leste(M)                                            #
      if rr == 2:                                           #
        sul(M)                                              #      É aleatorio para escolher uma direção para mover quando chegar na parede "X"
      if rr == 3:                                           #
        norte(M)                                            #
      if rr == 4:                                           #
        oeste(M)                                            #
      break                                                 ######
    if M[(0)][C[1]] == '🚪' and M[1][C[1]] == '🤖':           #
      M[(0)][C[1]] = '🤖'                                    #
      M[1][C[1]] = '⬜'                                      #
      Ca.append("N")                                        #      É encontrar saída de lado superior
      print("Encontrei uma saida!")                         #
      break                                                 ######
    if M[-1][C[1]] == '🚪' and M[-2][C[1]] == '🤖':           #
      M[-1][C[1]] = '🤖'                                     #
      M[-2][C[1]] = '⬜'                                     #
      Ca.append("S")                                        #      É encontrar saída de lado inferior
      print("Encontrei uma saida!")                         #                             
    else:                                                   ######     
      M[C[0]][C[1]] = '⬜'                                   #      
      M[(C[0])][(C[1])+1] = '🤖'                             #      Em loop, robô andando até abrir if acima
      Ca.append("L")                                        #
    print(" ")                                              ######
    for item in S: #--------------------------------------#Visualizando matriz
      print(''.join(item))
    
#---------------------------------------------------------------#Caminhando para norte
def norte(M):
  i=1
  while True:
    C = find('🤖', M)
    if M[0].count('🤖') == 1: #Aborte quando @ atravessa a parede de norte (segurança)
      break 
    if M[C[0]][C[1]] == '🤖' and M[(C[0])-1][C[1]] == '⬛':  ######
      rr = random.randint(1,4)                             #
      if rr == 1:                                          #
        leste(M)                                           #
      if rr == 2:                                          #
        sul(M)                                             #      É aleatorio para escolher uma direção para mover quando chegar na parede "X"
      if rr == 3:                                          #
        norte(M)                                           #
      if rr == 4:                                          #
        oeste(M)                                           #
      break                                                #
    if M[C[0]][0] == '🚪' and M[C[0]][1] == '🤖':            ######
      M[C[0]][0] = '🤖'                                     #
      M[C[0]][1] = '⬜'                                     #
      Ca.append("O")                                       #
      print("Encontrei uma saida!")                        #      É encontrar saída de lado esquerdo
      break                                                #
    if M[C[0]][-1] == '🚪' and M[C[0]][-2] == '🤖':          ######
      M[C[0]][-1] = '🤖'                                    #
      M[C[0]][-2] = '⬜'                                    #
      Ca.append("L")                                       #
      print("Encontrei uma saida!")                        #      É encontrar saída de lado direito
      break                                                #
    else:                                                  ######
      M[C[0]][C[1]] = '⬜'                                  #
      M[(C[0])-1][C[1]] = '🤖'                              #      Em loop, robô andando até abrir if acima
      Ca.append("N")                                       #
    print(" ")                                             ######
    for item in S: #--------------------------------------#Visualizando matriz
      print(''.join(item))
for i in range(x1): #--------------------------------------------------------------#Verificando se tem 🚪 em matriz. Obs as vezes falhou colocar 🚪 em matrix, mas não sei qual é o motivo. Estou investigando
  if M[i].count('🚪') == 1:
    norte(S)
    for item in S: 
      print(''.join(item))
    print("Resultado:", ''.join(Ca))
  else:
    erro.append(1)
    if sum(erro) == x1:
      print("FALHADO! Motivo: 🚪 não foi encontrado. Tente novamente") #--------------------- É aviso e aborto de codigo
