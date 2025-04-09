numeri_interi = list(range(1,11))
reciproci = [1/i for i in numeri_interi]
reciproci_formattati = [f"{i:.8f}" for i in reciproci]
for numero in reciproci_formattati:
    print(numero)