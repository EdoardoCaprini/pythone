reddito=int(input("Inserisci il reddito: "))
aliquota_1=0.23
aliquota_2=0.35
aliquota_3=0.43
imposta=0

if reddito <= 28000:
    imposta = reddito * aliquota_1
elif 28000 < reddito <= 50000:
    imposta = reddito * aliquota_2
else:
    imposta = reddito * aliquota_3
print("L'imposta da pagare è: ", imposta)