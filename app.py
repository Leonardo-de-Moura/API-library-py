from flask import Flask
from configuration import configure_all
app= Flask(__name__)

configure_all(app)

app.run(host='localhost', debug=True)
