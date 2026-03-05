from flask import Blueprint, render_template, request, session
from website.maps.generate_map import generate_map
from website.maps.oblicz_dopasowanie import oblicz_dopasowanie
from website.maps.dodanie_info import nazwy


mapa_bp = Blueprint('map', __name__)

@mapa_bp.route('/map',  methods=['POST'])

def map():
    #pobieranie odp z formularza
    preferencja1 = request.form.get('preferencja1')
    preferencja2 = request.form.get('preferencja2')
    preferencja3 = request.form.get('preferencja3')
    preferencja4 = request.form.get('preferencja4')
    print(request.form.get('preferencja0'))
    answers = [preferencja1,preferencja2,preferencja3,preferencja4]

     
#obliczanie dopasowania dla kazdej z miejscowosci, zwraca liste puktów dopasowania dla kazdego miejsca
    results_popularity = oblicz_dopasowanie(answers)

#generowanie mapy uwzględniając punkty 
    graph = generate_map(results_popularity)
    nazwa_miejsca,opis_miejsca, zdjecie =nazwy(results_popularity)
    print('zdjecie', zdjecie)
    print()
    print()
    print()
    print()
    print()
    print()
    if graph is None:
        print("Warning: The 'graph' variable is None.")
    print(results_popularity)
    return render_template('mapa.html',  graph_1=graph, nazwa_miejsca=nazwa_miejsca,opis_miejsca=opis_miejsca, zdjecie=zdjecie,
                         ) #renderuje szablon strony z mapą
