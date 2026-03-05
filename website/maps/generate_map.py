import pandas as pd
import plotly.express as px

def generate_map(results_popularity):
    # Odczyt danych z pliku Excela
    df = pd.read_excel('./website/maps/dane/Zeszyt1.xlsx')

    # DataFrame z destynacjami i popularnością
    vacation_df = pd.DataFrame({
        'destination': df['destination'].to_list(),
        'popularity': results_popularity,
        'latitude': df['latitude'].to_list(),
        'longitude': df['longitude'].to_list()
    })

    fig = px.scatter_geo(
        vacation_df,
        lat='latitude',
        lon='longitude',
        text='destination',
        size='popularity',
        color='popularity',  #kolorowanie w zależności od popularności
        projection='natural earth',
        title='',
        labels={'popularity': 'Popularity'},
        template='plotly',
        size_max=30,
        color_continuous_scale=px.colors.sequential.Pinkyl  # Możesz zmienić na inny gradient kolorów
    )

    # Dodatkowe informacje do wyświetlenia
    vacation_df['info'] = vacation_df.apply(lambda row: f"Destination: {row['destination']}<br>Popularity: {row['popularity']}", axis=1)

    fig.update_layout(height=900, width=1250)

    graph = fig.to_html(full_html=False, include_plotlyjs='cdn')
    return graph
