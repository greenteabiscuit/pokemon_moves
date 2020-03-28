import dash
import dash_html_components as html
import dash_core_components as dcc
import base64
from os import listdir
from os.path import isfile, join
import pandas as pd
MYPATH = "pokemon.json-master/thumbnails"

pokedex_data = pd.read_csv("all_pokemon_names_types.csv", index_col=0)

app = dash.Dash()

list_of_images =\
    [MYPATH + "/" + f for f in listdir(MYPATH) if isfile(join(MYPATH, f))]
list_of_images.sort()

app.layout = html.Div([
    html.Div([
        dcc.Dropdown(
            id='image-dropdown-1',
            options=[{'label': pokedex_data[pokedex_data["id"] == num + 1]["english_name"].values[0],
                    'value': i} for num, i in enumerate(list_of_images)],
            # initially display the first entry in the list
            value=list_of_images[0]
        ),
    ], style={'width': '49%', 'display': 'inline-block'}),
    html.Div([
        dcc.Dropdown(
            id='image-dropdown-2',
            options=[{'label': pokedex_data[pokedex_data["id"] == num + 1]["english_name"].values[0],
                    'value': i} for num, i in enumerate(list_of_images)],
            # initially display the first entry in the list
            value=list_of_images[0]
        ),
    ], style={'width': '49%', 'display': 'inline-block'}),
    html.Div([
        html.Div([
            html.Img(id='image-1'),
        ], style={'width': '49%', 'display': 'inline-block', 'margin-left': 'auto', 'margin-right': 'auto'}),
        html.Div([
            html.Img(id='image-2')
        ], style={'width': '49%', 'display': 'inline-block', 'margin-left': 'auto', 'margin-right': 'auto'}),
    ], style={'text-align': 'center'}),
])



@app.callback(
    dash.dependencies.Output('image-1', 'src'),
    [dash.dependencies.Input('image-dropdown-1', 'value')])
def update_image_src(image_path):
    # print the image_path to confirm the selection is as expected
    print('current image_path = {}'.format(image_path))
    encoded_image = base64.b64encode(open(image_path, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded_image.decode())


@app.callback(
    dash.dependencies.Output('image-2', 'src'),
    [dash.dependencies.Input('image-dropdown-2', 'value')])
def update_image_src(image_path):
    # print the image_path to confirm the selection is as expected
    print('current image_path = {}'.format(image_path))
    encoded_image = base64.b64encode(open(image_path, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded_image.decode())


if __name__ == '__main__':
    app.run_server(debug=True, port=8053, host='0.0.0.0')