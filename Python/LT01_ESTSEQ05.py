import math

A = float(input("Digite o coeficiente A da equação de 2º grau:"))

B = float(input("Digite o coeficiente B da equação de 2º grau:"))

C = float(input("Digite o coeficiente C da equação de 2º grau:"))

delta = (B**2) - 4* A * C

X1= ((-B) + math.sqrt(delta)) / 2*A

X2 =((-B) -. math.sqrt(delta)) / 2*A

print(f"As raízes são: {X1:.2f} e {X2:.2f}")
