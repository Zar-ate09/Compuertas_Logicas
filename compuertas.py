import pandas as pd
import os

#Compuerta AND
def continuar():
    input("presione enter para continuar")
    os.system ("cls")
    

def compuerta_AND():
      A = [1,1,0,0]
      B = [1,0,1,0]
      AandB = [None]*4
      for i in range(4):
            AandB[i] = A[i] and B[i]
      
      print("Compuerta Lógica AND")
      tablaAND = {'A': A, 'B': B, 'A and B': AandB}
      tablaAND_df = pd.DataFrame(tablaAND)
      print(tablaAND_df)


#Compuerta OR
def compuerta_OR():
      A = [1,1,0,0]
      B = [1,0,1,0]
      AorB = [None]*4
      for i in range(4):
            AorB[i] = A[i] or B[i]
      
      print("Compuerta Lógica OR")
      tablaAND = {'A': A, 'B': B, 'A and B': AorB}
      tablaAND_df = pd.DataFrame(tablaAND)
      print(tablaAND_df)

#Compuerta XOR
def compuerta_XOR(): 
      A = [1,1,0,0]
      B = [1,0,1,0]
      AxorB = [None]*4
      for i in range(4):
            AxorB[i] = not((A[i]==0 and B[i]==0) or (A[i]==1 and B[i]==1))
            if AxorB[i]==True:
                  AxorB.append(1)
            else:
                  AxorB.append(0)
      del(AxorB[0:4])
      print(AxorB)
      print("Compuerta Lógica XOR")
      tablaAND = {'A': A, 'B': B, 'A and B': AxorB}
      tablaAND_df = pd.DataFrame(tablaAND)
      print(tablaAND_df)



#Compuerta NAND
def compuerta_NAND():
      A = [1,1,0,0]
      B = [1,0,1,0]
      AnandB = [None]*4
      for i in range(4):
            AnandB[i] = not( A[i] and B[i])
            
            if AnandB[i]==True:
                  AnandB.append(1)
            else:
                  AnandB.append(0)
                  
      del(AnandB[0:4])
      print("Compuerta Lógica NAND")
      tablaNAND = {'A': A, 'B': B, 'A and B': AnandB}
      tablaNAND_df = pd.DataFrame(tablaNAND)
      print(tablaNAND_df)



def compuerta_NOR():
    
      A = [1,1,0,0]
      B = [1,0,1,0]
      AnorB = [None]*4
      for i in range(4):
            AnorB[i] = not(A[i] or B[i])
            if AnorB[i]==True:
                  AnorB.append(1)
            else:
                  AnorB.append(0)
      del(AnorB[0:4])
      print("Compuerta Lógica NOR")
      tablaNOR = {'A': A, 'B': B, 'A and B': AnorB}
      tablaNOR_df = pd.DataFrame(tablaNOR)
      print(tablaNOR_df)



#Compuerta XNOR
def compuerta_XNOR(): 
      A = [1,1,0,0]
      B = [1,0,1,0]
      AxnorB = [None]*4
      for i in range(4):
            AxnorB[i] = not(not((A[i]==0 and B[i]==0) or (A[i]==1 and B[i]==1)))
            if AxnorB[i]==True:
                  AxnorB.append(1)
            else:
                  AxnorB.append(0)
      del(AxnorB[0:4])
      print(AxnorB)
      print("Compuerta Lógica XOR")
      tablaXNOR = {'A': A, 'B': B, 'A and B': AxnorB}
      tablaXNOR_df = pd.DataFrame(tablaXNOR)
      print(tablaXNOR_df)

def main_menu (rep):
    while rep == 1:
        print("PROYECTO: COMPUERTAS LÓGICAS\nEQUIPO: N \nCOMPUESTO POR:\n->\n->\n")
        print("Seleccione una compuerta\n1)Compuerta AND\n2)Compuerta OR\n3)Compuerta XOR\n4)Compuerta NAND\n5)Compuerta NOR\n6)Compuerta XNOR\n")
        op = int(input("ingrese un numero para ver la compuesta deseada: "))
    
        if op == 1:
            compuerta_AND()
            continuar()
    
        elif op == 2:
            compuerta_OR()
            continuar()
    
        elif op == 3:
            compuerta_XOR()
            continuar()

        elif op == 4:
            compuerta_NAND()
            continuar()

        elif op == 5:
            compuerta_NOR()
            continuar()

        elif op == 6:
            compuerta_XNOR()
            continuar()
        
        else:
            print("opcion invalida")
            continuar()
            main_menu(1)
        
    
    

main_menu(1)
    


    