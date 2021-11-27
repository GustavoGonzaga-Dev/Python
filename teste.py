Ht = int (input("insira a quantidade de horas trabalhadas por mês: "))
Vh = float (input("insira o valor por hora: "))
Pd = float (input("insira o valor do percentual de desconto: "))
Nd= int (input("insira o numero de descendentes: "))
Sb = (Ht * Vh)
Des = ( Pd * Sb) / 100
Sl = Sb - Des
Total = (Nd * 100) + Sl
print("seu salario total ja com o desconto e os acrécimos é: R$", Total)

#from tkinter import *

#class Pessoa:
        #def __init__(self, master = None):#(self, nome, idade):
                #pass
        #root = Tk()
        #Application(root)
        #root.mainloop()
        
               # self.nome = nome
                #self.idade = idade

       # def setNome(self, nome):
               # self.nome = nome

       # def setIdade(self, idade):
                #self.idade = idade

        #def getNome(self):
                #return self.nome

        #def getIdade(self):
                #return self.idade

                
