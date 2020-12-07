#Trabalhando com strings e adicionando numeros nelas usando conversão
# de numero em string
days_in_feb = 28
#str() converte o parâmetro em string
print(str(days_in_feb)+' days in February')


#Trabalhando com strings e convertendo em números
# a função input() sempre retorna string
first_number = input('Enter first number: ')
second_number = input('Enter second number: ')
#então usamos os conversores de tipo int() ou float()
print(int(first_number)+int(second_number))
print(float(first_number)+float(second_number))