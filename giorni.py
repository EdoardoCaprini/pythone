GIORNI=(
        "Lunedi   "+
        "Martedi  "+
        "Mercoledi"+
        "Giovedi  "+
        "Venerdi  "+
        "Sabato   "+
        "Domenica ")
NumeroGiorni=int(input("dammi un numero dall'1 al 7: "))
p=((NumeroGiorni-1)*9)
print(GIORNI[p],GIORNI[p+1],GIORNI[p+2],GIORNI[p+3],GIORNI[p+4],GIORNI[p+5],GIORNI[p+6],GIORNI[p+7],GIORNI[p+8])