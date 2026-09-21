import web
import sqlite3

render = web.template.render('views/')

class Index:
    def GET(self):
        return render.index(None)

    def POST(self):
        datos = web.input(matricula="", carrera="", nombre="", tramite="")
        conn = sqlite3.connect("fila.db")
        conn.execute(
            "INSERT INTO fila (matricula, carrera, nombre, tramite) VALUES (?, ?, ?, ?)",
            (datos.matricula, datos.carrera, datos.nombre, datos.tramite)
        )
        conn.commit()
        conn.close()
        return render.index(f"{datos.nombre} se agregó a la fila.")
        