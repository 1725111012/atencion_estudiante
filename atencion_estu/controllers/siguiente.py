import web
import sqlite3

render = web.template.render('views/')

class Siguiente:
    def GET(self):
        conn = sqlite3.connect("fila.db")
        estudiante = conn.execute("SELECT * FROM fila ORDER BY id LIMIT 1").fetchone()
        conn.close()
        return render.siguiente(estudiante)
        