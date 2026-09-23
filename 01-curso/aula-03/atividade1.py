# Faça um programa que peça as 4 notas bimestrais e mostre a média.

print(f"""
    +--------------------------------+
    |            MEDIA               |
    +--------------------------------+
""")
nome = input(" Digite o nome do aluno: ")

nota_1 = float(input(" Digite a nota do primeiro simestre: "))
nota_2 = float(input(" Digite a nota do segundo simestre: "))
nota_3 = float(input(" Digite a nota do terceiro simestre: "))
nota_4 = float(input(" Digite a nota do quarto simestre: "))

print(f"""
    >> A média do aluno {nome} é {(nota_1 + nota_2 + nota_3 + nota_4) / 4}
""")
