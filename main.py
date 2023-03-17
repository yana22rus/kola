import sqlite3

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def create_post():
    with sqlite3.connect("Data.db") as con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Comment')
        lst_data = cur.fetchall()

    if request.method == "POST":
        if request.form["submit"] == "Сохранить":
            first_name = request.form['first_name']
            text = request.form['text']
            date = request.form['date']

            with sqlite3.connect("Data.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO Comment (first_name,text,date) VALUES  (?,?,?)", (first_name, text, date))

            return redirect(url_for("create_post"))

        if request.form["submit"] == "Удалить":

            with sqlite3.connect("Data.db") as con:
                cur = con.cursor()
                cur.execute("DELETE FROM Comment WHERE id = ?", (request.form["id"],))
            return redirect(url_for("create_post"))

    return render_template("create_post.html", lst_data=lst_data)


if __name__ == "__main__":
    app.run(debug=True)
