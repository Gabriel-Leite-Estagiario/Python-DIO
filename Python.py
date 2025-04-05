
#Contas, tipo, comparação

print('hello world')

print(type("number"))

print(type(1))

print(type(2.5))

print(type(2>5))

print( 10+10 )

print( 10-10 )

print( 10<10 )

print( 10>10 )

print( 10 != 10 )

print( 10 == 10 )

print( 10 | 10 )

number = 10

number2 = 20

print(number + number2)

age = 21

print(f'Eu tenho {age} Anos')

# nome = input ("Informe seu nome")

# print(f"Seu nome é {nome}")

print(10*10)

print(10//10)

print(10**2*2)

#Variávies

saldo =100
saldo +=100

print(saldo)

saldo=1000
grana=200
dinheiro=100

print(saldo >= grana or saldo <= dinheiro)

print(not 1000>1500)

print(10 >= 20 and 10 <= 20 or 10 <= 20 and 10 >= 20)

name = "Gabriel"

print(name is name)

print(name is not name)

#Listas

frutas = ["lemon", "abacate", "manga"]

print ("orange" not in frutas)

print ("lemon" not in frutas)


#Condições

money = 1000

saque = float(input ("Informe um valor para retirada  "))

if money >= saque:
    print("Saque autorizado")

else:
    print("Voce não tem dinheiro suficiente")


#Condição com elif

opcao = int(input("Informe a opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float (input("Informe a quantia para o saque: "))

elif opcao == 2:
    print("Exibindo o extrato...")

else:
    print("Opção inválida")



#For

frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
  print(fruta)



for i in range(5):  # Gera números de 0 a 4
  print(i)



#While 

contador = 0
while contador < 5:
  print(contador)
  contador += 1



numero = 10
while True:
  palpite = int(input("Adivinhe o número (dica: é menor que 15): "))
  if palpite == numero:
    print("Parabéns, você acertou!")
    break  # Sai do loop
  elif palpite < numero:
    print("O número é maior.")
  else:
    print("O número é menor.")


    #Tabuada

    for numero in range (0, 51, 5):
       print(numero, end=" ")


#Interpolação

nome = "Gabriel"
idade = 21

print ("olá meu nome é %s e eu tenho %d anos de idade." % (nome, idade))


#Função

def nome():
   print("Gabriel Leite")


nome()

