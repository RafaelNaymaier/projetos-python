#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão


print('='*21)
print('10 termos de uma PA')
print('='*21)

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for c in range (10):
    pa = primeiro_termo + c * razao
    print(pa, '->', end=' ')
print('Acabou')





























