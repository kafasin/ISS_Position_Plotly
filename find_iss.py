import pandas as pd
import plotly.express as px


API = 'http://api.open-notify.org/iss-now.json'


def find_iss():
    """
    Finds and locates the position of Iss on 2D WorldMap
    """
    df = pd.read_json(API)
    df['lat'] = df.loc['latitude', 'iss_position']
    df['long'] = df.loc['longitude', 'iss_position']
    fig = px.scatter_geo(df, lat='lat', lon='long')
    fig.show()


if __name__ == '__main__':
    find_iss()
