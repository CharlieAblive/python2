idade = int(input("Informe sua idade:"))
temVIP = input("Possui vip (s/n):")
adm = input("Acesso a organização (s/n):")

if adm == 's':
    print("Acesso liberado.")
elif temVIP == 's'  and idade >= 18:
    print("Acesso liberado.")
else :
    print("Acesso negado.")