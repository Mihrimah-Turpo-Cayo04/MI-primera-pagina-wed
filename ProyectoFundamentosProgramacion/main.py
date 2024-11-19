from flask import Flask, render_template

app = Flask(_name_)

@app.route('/')
def pagina1():
    return render_template('pagina1.html')  # Página de introducción

@app.route('/pagina2')
def pagina2():
    return render_template('pagina2.html')  # Página del formulario

@app.route('/pagina3')
def pagina3():
    return render_template('pagina3.html')  # Página de resultados

if _name_ == '_main_':
    app.run(debug=True)
