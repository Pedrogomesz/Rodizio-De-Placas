print('Exemplo com if-elif-else')
print('------------------------')

final_placa = int(input('Numero: '))
if final_placa == 1 or final_placa == 2:
    print('Rodizio de Segunda=Feira')
elif final_placa == 3 or final_placa == 4:
    print('Rodizio de Terça-feira')
elif final_placa == 5 or final_placa == 6:
    print('Rodizio de Quarta-Feira')
elif final_placa == 7 or final_placa == 8:
    print('Rodizio de Quinta-Feira')
elif final_placa == 9 or final_placa == 0:
    print('Rodizio de Sexta-Feira')
else:
    print('Numero Invalido!')

print('-Exemplo com match case-')
print('------------------------')

final_placa = int(input('Numero do Placa: '))

match final_placa:
    case 1|2:   
        print('Segunda-Feira')
    case 3|4:   
        print('Segunda-Feira')
    case 5|6:   
        print('Segunda-Feira')
    case 7|8:   
        print('Segunda-Feira')
    case 9|0:   
        print('Segunda-Feira')
    case _:
        print('Numero invalido')

