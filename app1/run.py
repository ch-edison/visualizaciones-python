from flask import render_template
from flask import Flask

import pandas as pd
import pdvega  # adds vgplot attribute to Pandas objects
import json

# app = Flask(__name__)
app = Flask(__name__, template_folder='templates')  # still relative to module


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/demo/')
@app.route('/demo/<name>')
def hello(name=None):
    data = pd.Series([1, 2, 3, 2, 3, 4, 3, 4, 5, 100])
    data.vgplot()
    plot = data.vgplot()
    valores = json.dumps(plot.spec, 'plot.json')
    print "valores"
    print valores
    print "end - valores"
    return render_template('index.html', name=name, valores=valores)


@app.route('/cne/')
def cne(name=None):

    data02 = pd.read_csv("../forjupyter/datos-cnt/candidatos_2002.csv", low_memory=False)
    # ../forjupyter/datos-cnt/candidatos_2002.csv
    data = pd.Series(data02.groupby('CANDIDATO_SEXO').size())
    print data
    data.vgplot()
    plot = data.vgplot()
    valores = json.dumps(plot.spec, 'plot.json')
    print "valores"
    print valores
    print "end - valores"
    return render_template('index.html', name=name, valores=valores)


@app.route('/cne3/')
def cne3(name=None):

    data02 = pd.read_csv("../forjupyter/datos-cnt/candidatos_2002.csv", low_memory=False)
    data = pd.Series(data02.groupby('CANDIDATO_PROVINCIA_CODIGO').size())
    print data
    data.vgplot()
    plot = data.vgplot()
    valores = json.dumps(plot.spec, 'plot.json')
    print "valores"
    print valores
    print "end - valores"
    return render_template('index.html', name=name, valores=valores)




if __name__ == '__main__':
    app.run(host='0.0.0.0')
