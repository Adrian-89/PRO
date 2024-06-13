flags = input('Escoja entre:Italia, España, Brasil o Alemania')

if flags == 'Italia':
    flag = '🇮🇹'
elif flags == 'España':
    flag = '🇪🇸'
elif flags == 'Brasil':
    flag = '🇧🇷'
elif flags == 'Alemania':
    flag = '🇩🇪'
else:
    flag = 'no flags'

print(flag)
