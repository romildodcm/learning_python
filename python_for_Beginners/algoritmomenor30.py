total = 0
contadorDeValoresInseridos = 0

while (total<30):
    totalMenorQueTrinta = total
    valor = float(input("Insira um valor: "))
    total = total+valor
    if (total<30):
        contadorDeValoresInseridos = contadorDeValoresInseridos+1

print(f'Foram inseridos {contadorDeValoresInseridos} valores, somados totalizaram {totalMenorQueTrinta}.')

