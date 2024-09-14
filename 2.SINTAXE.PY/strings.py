# >>>>> MÉTODOS DA CLASSE STRING <<<<<
#* >>> MAIUSCULA, MINUSCULA E TÍTULO:
curso = "pYthon"

print(curso.upper())
    # result = PYTHON
print(curso.lower())
    # result = python
print(curso.title())
    # result = Python
    
#* >>> ELIMINANDO ESPAÇOS:
curso = "   Python"

print(curso.strip())
    # result = "Python"
print(curso.lstrip())
    # result = "Python "
print(curso.rstrip())
    # result = "    Python"
    
#* >>> JUNÇÕES E CENTRALIZAÇÃO:
curso = "   Python"

print(curso.CENTER(10, "#"))
    # result = "##Python##"
print(".".join(curso))
    # result = "P.y.t.h.o.n"

# --------------------------------------------------------------------------------------
# >>>>> INTERPOLAÇÃO DE VARIAVEIS <<<<<
nome = "Guilherme"
idade = 28
profissao = "Progamador"
linguagem = "Python"

#* >>> OLD STYLE %:
print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))
# >>> Olá, me chamo Guilherme. Eu tenho 28 anos de idade, trabalho como Progamador e utilizo e estou matriculado no curso de Python.

#* >>> MÉTODO FORMAT:
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))
pessoa = {"nome": nome, "idade": idade, "profissao": profissao, "linguagem": linguagem}
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(**pessoa))
# >>> Olá, me chamo Guilherme. Eu tenho 28 anos de idade, trabalho como Progamador e utilizo e estou matriculado no curso de Python.

#* >>> F-STRING:
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de dade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")
# >>> Olá, me chamo Guilherme. Eu tenho 28 anos de idade, trabalho como Progamador e utilizo e estou matriculado no curso de Python.

# --------------------------------------------------------------------------------------
# >>>>> FATIAMENTO DE STRING <<<<<
#* >>> FATIAMENTO:
nome = "Guilherme Arthur de Carvalho"
nome[0]
# >>> "G"
nome [:9]
# >>> "Guilherme"
nome [10:]
# >>> "Arthur de Carvalho"
nome [10:16]
# >>> "Arthur"
nome [10:16:2]
# >>> "Atu"
nome[:]
# >>> "Guilherme Arthur de Carvalho"
nome [::-1]
# >>> "ohlavraC ed ruhtrA emrehliuG"

#* >>> STRINGS TRIPLAS:
nome = "Guilherme"
mensagem = f"""
Olá meu nome é {nome},
Eu estou aprendendo Python
"""
# >>>
# Olá meu nome é Guilherme,
# Eu estou aprendendo Python

nome = "Guilherme"
mensagem = f'''
    Olá meu nome é {nome},
Eu estou aprendendo Python
    Essa mensagem tem diferentes recuos.
'''
# >>>   
#   Olá meu nome é Guilherme,   
# Eu estou aprendendo Python
#   Essa mensagem tem diferentes recuos.