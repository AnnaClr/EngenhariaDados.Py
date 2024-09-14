# >>>>> FUNÇÕES <<<<<
def exibir_msg():
    print("Hello world!")

def exibir_msg2(nome):
    print(f"Seja bem vindo, {nome}!")

def exibir_msg3(nome="Anônimo"):
    print(f"Seja bem vindo, {nome}!")

exibir_msg()
exibir_msg2(nome="Guilherme")
exibir_msg3()
exibir_msg3(nome="Chappie")

#* >>> RETORNANDO VALORES:
def calcular_total(nums):
    return sum(nums)

def return_antecessor_sucessor(num):
    antecessor = num - 1
    sucessor = num + 1
    
    return antecessor, sucessor

calcular_total([10, 20, 34]) 
    # result = 64
return_antecessor_sucessor(10)
    # result = (9, 11)

#* >>> ARGUMENTOS NOMEADOS:
def salvar_carro(marca, modelo, ano, placa):
    # salvar carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano="1999", placa="ABC-1234")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
# Carro inserido com sucesso! Fiat/Palio/1999/ABC-1234

#* >>> ARGS E KWARGS:
def exibir_poema(data_extenso, *args, **kwargs):
    texto = "/n".join(args)
    meta_dados = "/n".join(([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()]))
    mensagem = f"{data_extenso}/n/n{texto}/n/n{meta_dados}"
    print(mensagem)
    
exibir_poema("Zen of Python", "Beautiful is better than ugly", autor="Tim Peters", ano=1999)

#* >>> POSITIONAL ONLY:
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
    
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
    # válido
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
    # inválido

#* >>> KEYWORD ONLY:
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
    
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
    # válido
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
    # inválido
    
#* >>> KEYWORD AND POSITIONAL ONLY:
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
    
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
    # válido
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
    # inválido
    
#* >>> OBJETOS DE PRIMEIRA CLASSE:
def sum(a, b):
    return a + b

def exibir_result(a, b, função):
    result = função(a, b)
    print(f"O resultado de {a} + {b} = {result}")
    
exibir_result(10, 20, sum) 
    # O resultado de 10 + 10 = 20
    
#* >>> ESCOPO LOCAL E ESCOPO GLOBAL:
salary = 2000

def bonus_salary(bunus):
    global salary
    salary += bunus
    return salary

bonus_salary(500)
    # result = 2500