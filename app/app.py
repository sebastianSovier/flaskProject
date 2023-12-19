

from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/')
def inicio():  # put application's code here
    return render_template('Inicio.html')
@app.route('/ejercicio1',methods=['POST','GET'])
def formNotas():
    estado = ''
    notas = {'nota1': 0, 'nota2': 0, 'nota3': 0, 'asistencia': 0}
    if(request.method=='POST'):
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])

        promedio = round((nota1 + nota2 + nota3)  / 3)
        if promedio >= 40 and asistencia >= 75:
            estado = 'APROBADO'
        else:
            estado = 'REPROBADO'
        notas = {'nota1':nota1,'nota2':nota2,'nota3':nota3,'asistencia':asistencia}
        return render_template('formulario1.html',notas=notas,promedio = promedio,estado = estado)

    return render_template('formulario1.html',notas=notas)

@app.route('/ejercicio2',methods=['POST','GET'])
def formNombres():
    maxNombre = ''
    cantCaracteres = 0
    nombres = {'nombre1': "", 'nombre2': "", 'nombre3': ""}
    if(request.method=='POST'):
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']
        nombres = {'nombre1': nombre1, 'nombre2': nombre2, 'nombre3': nombre3}
        if len(nombre1) > len(nombre2) and len(nombre1) > len(nombre3):
             maxNombre = nombre1
             cantCaracteres = len(nombre1)
        elif len(nombre2) > len(nombre1) and len(nombre2) > len(nombre3):
             maxNombre = nombre2
             cantCaracteres = len(nombre2)
        elif len(nombre3) > len(nombre1) and len(nombre3) > len(nombre2):
             maxNombre = nombre3
             cantCaracteres = len(nombre3)
        else:
             pass

        return render_template('formulario2.html',nombres = nombres,maxNombre = maxNombre,cantCaracteres = cantCaracteres)

    return render_template('formulario2.html',nombres=nombres,maxNombre = maxNombre,cantCaracteres = cantCaracteres)

if __name__ == '__main__':
    app.run(debug=True)
