import dash
import dash_html_components as html
import dash_core_components as dcc
import base64
from os import listdir
from os.path import isfile, join
MYPATH = "pokemon.json-master/thumbnails"


app = dash.Dash()

list_of_images = [MYPATH + "/" + f for f in listdir(MYPATH) if isfile(join(MYPATH, f))]

app.layout = html.Div([
    dcc.Dropdown(
        id='image-dropdown-1',
        style={'width': '50%'},
        options=[{'label': i, 'value': i} for i in list_of_images],
        # initially display the first entry in the list
        value=list_of_images[0]
    ),
    dcc.Dropdown(
        id='image-dropdown-2',
        style={'width': '50%'},
        options=[{'label': i, 'value': i} for i in list_of_images],
        # initially display the first entry in the list
        value=list_of_images[0]
    ),
    html.Img(id='image-1'),
    html.Img(id='image-2')
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