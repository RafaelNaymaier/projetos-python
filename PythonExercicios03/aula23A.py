
try:
    a = int(input('Numerador'))
    b = int(input('Denominador'))
    r = a / b

except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados.')

except ZeroDivisionError:
    print('Não é possível dividir por zero!')

except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados')

except Exception as erro:
    print(f'Erro de {erro.__class__}')

else:
    print(f'O resultado foi {r:.1f}')

finally:
    print('Volte sempre')

















