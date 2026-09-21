import web
import sqlite3

render = web.template.render('views/')

class Estado:
    def GET(self):
        conn = sqlite3.connect("fila.db")
        estudiantes = conn.execute("SELECT * FROM fila ORDER BY id").fetchall()
        total = len(estudiantes)
        conn.close()
        return render.estado(estudiantes, total)
        