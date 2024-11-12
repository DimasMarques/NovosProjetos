
idade = int(input("entre com a sua idade: "))
if idade >= 18:
   print ("Você é maior de idade.")
elif idade < 18 and idade >= 13:
   print("Você é um adolescente.")
else:
   print("Você é uma criança.")