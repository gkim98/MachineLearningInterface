import dash 

app = dash.Dash(__name__)
server = app.server 
app.scripts.config.serve_locally=True
app.config.suppress_callback_exceptions=True 

