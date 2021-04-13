from flask import Flask, render_template, abort
from lxml import etree
import os

app = Flask(__name__)

@app.route('/')
def indice():
	return render_template("indice.html")

@app.route('/potencia',methods=["GET","POST"])
@app.route('/potencia/<int:base>/<exponente>', methods=["GET","POST"])
def potencia(base=0, exponente=0):
	resultado=base**int(exponente)
	return render_template("potencia.html",resultado=resultado,base=base,exponente=exponente)

@app.route('/cuenta/<palabra>/<letra>')
def contarletras(palabra,letra):
	if len(letra) == 1:
		resultado=palabra.count(letra)
	else:
		abort(404)
	return render_template("cuentaletras.html",resultado=resultado,palabra=palabra,letra=letra)

@app.route('/libro/<codigo>')
def libros(codigo):
	doc=etree.parse('/home/usuario/github/Flask/libros.xml')
	if codigo in doc.xpath("//codigo/text()"):
		libro=doc.xpath(f"//titulo[../codigo={codigo}]/text()")[0]
		autor=doc.xpath(f"//autor[../codigo={codigo}]/text()")[0]
	else:
		abort(404)
	return render_template("libros.html",libro=libro,autor=autor)

port=os.environ["PORT"]
app.run('0.0.0.0',int(port),debug=True)