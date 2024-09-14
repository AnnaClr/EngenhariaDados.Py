# >>>>> OPERADORES ARITMÉTICOS <<<<<
prod1 = 20
prod2 = 10

#* >>>>> SOMA:
print(prod1 + prod2)
    # result = 30

# * >>> SUBTRAÇÃO: 
print(prod1 - prod2)
    # result = 10

#* >>> MULTIPLICAÇÃO:
print(prod1 * prod2)
    # result = 200

#* >>> DIVISÃO:
print(prod1 / prod2)
    # result = 2.0

#* >>> DIVISÃO INTEIRA:
print(prod1 // prod2)
    # result = 2

#* >>> MÓDULO:
print(prod1 % prod2)
    # result = 0

#* >>> EXPONENCIAÇÃO:
print(prod1 ** prod2)
    # result = 102240000000000

#* >>> PRECEDÊNCIA DE OPERADORES:
print(10 - 5 * 2)
    # result = 0
print((10 - 5) * 2)
    # result = 10
print(10 ** 2 * 2)
    # result = 200
print(100 ** (2 * 2))
    # result = 10.000
print(10 / 2 * 4)
    # result = 20.0

# --------------------------------------------------------------------------------------
# >>>>> OPERADORES DE COMPARAÇÃO <<<<<
saldo = 450
saque = 200

#* >>> IGUALDADE:
print(saldo == saque)
    # result = False

#* >>> DIFERENÇA:
print(saldo != saque)
    # result = True
    
#* >>> MENOR QUE, MAIOR OU IGUAL, MAIOR QUE:
print(saldo > saque) # maior que
    # result = True
print(saldo >= saque) # maior ou igual
    # result = True
print(saldo < saque) # menor que
    # result = False

# --------------------------------------------------------------------------------------
# >>>>> OPERADORES DE ATRIBUIÇÃO <<<<<
#* >>> ATRIBUIÇÃO SIMPLES:
saldo = 500

print(saldo)
    # result = 500

#* >>> ATRIBUIÇÃO COM ADIÇÃO:
saldo = 500
saldo += 200

print(saldo)
    # result = 700
    
#* >>> ATRIBUIÇÃO COM SUBTRAÇÃO:
saldo = 500
saldo -= 100

print(saldo)
    # result = 400
    
#* >>> ATRIBUIÇÃO COM MULTIPLICAÇÃO:
saldo = 500
saldo *= 2

print(saldo)
    # result = 1000

#* >>> ATRIBUIÇÃO COM DIVISÃO:
saldo = 500
saldo /= 5

print(saldo)
    # result = 100.0
    
saldo = 500
saldo //= 5

print(saldo)
    # result = 100
    
#* >>> ATRIBUIÇÃO COM MÓDULO:
saldo = 500
saldo %= 480

print(saldo)
    # result = 20
    
#* >>> ATRIBUIÇÃO COM EXPONENCIAÇÃO:
saldo = 80
saldo **= 2

print(saldo)
    # result = 6400

# --------------------------------------------------------------------------------------
# >>>>> OPERADORES LÓGICOS <<<<<
saldo = 1000
saque = 200
limite = 100

#* >>> OPERADOR E(and):
saldo >= saque and saque <= limite
    # result = False
    
#* >>> OPERADOR E(and):
saldo >= saque or saque <= limite
    # result = True
    
#* >>> OPERADOR NEGAÇÃO:
contatos_emergency = []

not 1000 > 1500
    # result = True
not contatos_emergency
    # result = True
not "saque 1500;"
    # result = False
not ""
    # result = True
    
#* >>> PARENTESES: 
saldo = 1000
saque = 250
limite = 200
conta_especial = True

saldo >= saque and saque <= limite or conta_especial and saldo >= saque
    # result = True
(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
    # result = True


# --------------------------------------------------------------------------------------
# >>>>> OPERADORES DE IDENTIDADE <<<<<
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso
    # result = True
curso is not nome_curso
    # result = False
saldo is limite
    # result = True

# --------------------------------------------------------------------------------------
# >>>>> OPERADORES DE ASSOCIAÇÃO <<<<<
curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

"Python" in curso
    # result = True
"maça" not in frutas
    # result = True
200 in saques
    # result = False