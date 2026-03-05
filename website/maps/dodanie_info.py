import pandas as pd
# Jeżeli ma się wyświetlać informacja tylko o najlepszej destynacji:
# df = pd.read_excel('./website/maps/dane/Zeszyt2.xlsx')
# destination_list = df['destination'].to_list()
# def nazwy(results_popularity):
#     najwieksza = max(results_popularity)
#     lista_opisow = []
#     lista_zdjec = []
#     lista_nazw= []
#     if najwieksza != 0:
#             indeksy_najwiekszej = [i for i, liczba in enumerate(results_popularity) if liczba == najwieksza]
#             print("Największa liczba:", najwieksza)
#             print("Indeksy największej liczby:", indeksy_najwiekszej)
#             lista_nazw= [destination_list[indeks] for indeks in indeksy_najwiekszej]
#             for index, row in df.iterrows():
#                 if row['destination'] in lista_nazw:
#                     lista_opisow.append(row['opis'])
#                     lista_zdjec.append(row['zdjecie'])
#     print('Opisy', lista_opisow)
#     return lista_nazw, lista_opisow, lista_zdjec

df = pd.read_excel('./website/maps/dane/Zeszyt2.xlsx')
destination_list = df['destination'].to_list()
def nazwy(results_popularity):

    lista_opisow = []
    lista_zdjec = []
    lista_nazw= []

    słownik_punktów = {}

    for miasto, punkt in zip(destination_list , results_popularity):
        if punkt != 0:
         słownik_punktów[miasto] = punkt
   
    posortowany_słownik_punktow = dict(sorted(słownik_punktów.items(), key=lambda x: x[1], reverse=True))
    print(posortowany_słownik_punktow)

    for miasto, punkt in posortowany_słownik_punktow.items():
        print('MIASTOOO', miasto)
        for index, row in df.iterrows():
                if row['destination'] == miasto:
                    lista_nazw.append(miasto)
                    lista_opisow.append(row['opis'])
                    lista_zdjec.append(row['zdjecie'])
       
    return lista_nazw, lista_opisow, lista_zdjec
