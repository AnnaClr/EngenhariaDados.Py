# >>>>> CONVERSÕES <<<<<
#* >>> INTEIRO PARA FLOAT:
preço = 10
print(preço)
    # result = 10

preço = float(preço)
print(preço)
    # result = 10.0
    
preço = 10 / 2
print(preço)
    # result = 5.0
    
#* >>> FLOAT PARA INTEIRO:
preço = 10.30
print(preço)
    # result = 10.3

preço = int(preço)
print(preço)
    # result = 10
    
#* >>> INTEIRO PARA FLOAT:
preço = 10
print(preço)
    # result = 10

preço = float(preço)
print(preço)
    # result = 10.0
    
#* >>> CONVERSÃO POR DIVISÃO:
preço = 10
print(preço)
    # result = 10
    
print(preço / 2)
    # result = 5.0
    
#* >>> NÚMERICO PARA STRING:
preço = 10.50
idade = 28

print(str(preço))
    # result = 10.5
print(str(idade))
    # result = 28
    
texto = (f"idade: {idade}, preço: {preço}")
print(texto)
    # result = idade: 28, preço: 10.5
    
#* >>> STRING PARA NÚMERO:
preço = "10.50"
idade = "28"

print(float(preço))
    # result = 10.50
print(int(idade))
    # result = 28