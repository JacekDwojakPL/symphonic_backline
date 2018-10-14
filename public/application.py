import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask, render_template, request, jsonify, redirect, url_for

path = os.path.abspath("./")
url = os.path.join(path, "data.db")
engine = create_engine("sqlite:///"+url)
db = scoped_session(sessionmaker(bind=engine))
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/admin")
def admin():
    sections = db.execute("SELECT * FROM 'sections'").fetchall()
    return render_template("admin.html", sections=sections)

@app.route("/edit_sections", methods=["POST"])
def edit_sections():
    id = request.form.get("id")
    nazwa = request.form.get("nazwa")
    name = request.form.get("name")
    opis = request.form.get("opis")
    description = request.form.get("description")
    instrumentSection = 1 if request.form.get("instrumentSection") == "on" else 0

    db.execute("UPDATE sections SET nazwa=:nazwa, name=:name, opis=:opis, description=:description WHERE id=:id",
                {"nazwa": nazwa, "name": name, "opis": opis, "description": description, "id": id, "instrumentSection": int(instrumentSection)})
    db.commit()
    return redirect(url_for('admin'))

@app.route("/add_sections", methods=["POST"])
def add_sections():
    nazwa = request.form.get("nazwa")
    name = request.form.get("name")
    opis = request.form.get("opis")
    description = request.form.get("description")
    instrumentSection = 1 if request.form.get("instrumentSection") == "on" else 0

    db.execute("INSERT INTO sections (nazwa, name, opis, description, instrumentSection) VALUES (:nazwa, :name, :opis, :description, :instrumentSection)",
    {"nazwa": nazwa, "name": name, "opis": opis, "description": description, "instrumentSection": int(instrumentSection)})
    db.commit()

    return redirect(url_for("admin"))


@app.route("/add_instrument", methods=["POST"])
def add_instrument():
    nazwa = request.form.get("nazwa")
    name = request.form.get("name")
    opis = request.form.get("opis")
    description = request.form.get("description")
    section_id = request.form.get("section_id")

    db.execute("INSERT INTO instruments (nazwa, name, opis, description, section_id) VALUES (:nazwa, :name, :opis, :description, :section_id)",
    {"nazwa": nazwa, "name": name, "opis": opis, "description": description, "section_id": int(section_id)})
    db.commit()
    return redirect(url_for("admin"))

@app.route("/api/get_links")
def get_links():
    links = db.execute("SELECT nazwa, name, instrumentSection FROM 'sections'").fetchall()
    output = [dict(row) for row in links]
    return (jsonify(output))


@app.route("/api/get_sections")
def get_sections():
    sections = db.execute("SELECT * FROM 'sections'").fetchall()
    output = [dict(row) for row in sections]
    return jsonify(output)

@app.route("/api/get_instruments")
def get_instruments():
    instruments = db.execute("SELECT * FROM 'instruments'").fetchall()
    output = [dict(row) for row in instruments]
    return jsonify(output)

@app.route("/api/get_landing")
def get_landing():
    landing = db.execute("SELECT * FROM 'landing'").fetchall()
    output = [dict(row) for row in landing]
    return jsonify(output)
