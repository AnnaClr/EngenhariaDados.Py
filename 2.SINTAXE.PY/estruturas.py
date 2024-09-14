# >>>>> INDENTAÇÃO E BLOCOS <<<<<
#* >>> BLOCO EM PYTHON:
def sacar(self, valor: float) -> None: #inicio do bloco método
    if self.saldo >= valor: # inicio do bloco if
        self.saldo -= valor
    # fim do bloco if
# fim do bloco método
    
# --------------------------------------------------------------------------------------
# >>>>> ESTRUTURAS CONDICIONAIS <<<<<
#* >>> IF ELSE:
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque: 
    print("Realizando saque!")
else:
    print("Saldo Insuficiente.")
    
#* >>> IF, ELIF, ELSE:
opção = float(input("Informe uma opçãp: [1] Sacar /n [2] Extrato: "))

if opção == 1:
    valor = float(input("Informe a quantia para o saque: "))
elif opção == 2:
    print("Exibindo o extrato...")
else:
    SystemExit("Opção Inválida")
    
#* >>> IF ANINHADO:
if conta_normal: # type: ignore
    if saldo >= saque:
        print("Saldo realizado!")
    elif saldo <= (saldo + cheque_especial): # type: ignore
        print("Saque realizado com cheque especial!")
elif conta_universitaria: # type: ignore
    if saldo >= saque:
        print("Saldo realizado!")
    else: 
        print("Saldo insuficiente.")
        
#* >>> IF TERNÁRIO:
status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")
        
# --------------------------------------------------------------------------------------
# >>>>> ESTRUTURAS DE REPETIÇÃO <<<<<
#* >>> FOR:
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print() # adiciona quabra de linha
    
#* >>> FOR ELSE:
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print() # adiciona quabra de linha

#* >>> RANGE:
# range(stop) -> range object
# range(start, stop[, step]) -> range object

list(range(4))
    # result = [0, 1, 2, 3]
    
#* >>> RANGE COM FOR:
for num in range(0, 11):
    print(num, end=" ")
    # result = 0 1 2 3 4 5 6 7 8 8 10

for num in range(0, 51, 5):
    print(num, end=" ")
    # result = 0 5 10 15 20 25 30 35 40 45 50

#* >>> WHILE:
opção = -1

while opção != 0:
    opção = int(input("[1] Sacar /n [2] Extrato /n [3] Sair /n: "))
    if opção == 1:
        print("Sacando...")
    elif opção == 2:
        print("Extrato...")

#* >>> WHILE ELSE:
opção = -1

while opção != 0:
    opção = int(input("[1] Sacar /n [2] Extrato /n [3] Sair /n: "))
    if opção == 1:
        print("Sacando...")
    elif opção == 2:
        print("Extrato...")
else:
    print("Obrigada por usar nosso serviço. Até breve!")