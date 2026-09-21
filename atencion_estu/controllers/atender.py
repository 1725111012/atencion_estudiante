import web
import sqlite3

render = web.template.render('views/')

class Atender:
    def GET(self):
        conn = sqlite3.connect("fila.db")
        estudiante = conn.execute("SELECT * FROM fila ORDER BY id LIMIT 1").fetchone()

        if estudiante:
            conn.execute("DELETE FROM fila WHERE id=?", (estudiante[0],))
            conn.commit()

        conn.close()
        return render.atender(estudiante)
        