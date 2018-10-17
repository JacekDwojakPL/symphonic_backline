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
    instruments = db.execute("SELECT * FROM 'instruments'").fetchall()
    db.commit()
    return render_template("admin.html", sections=sections, instruments=instruments)

@app.route("/edit_sections", methods=["POST"])
def edit_sections():
    id = request.form.get("id")
    nazwa = request.form.get("nazwa")
    name = request.form.get("name")
    opis = request.form.get("opis")
    description = request.form.get("description")
    instrumentSection = 1 if request.form.get("instrumentSection") == "on" else 0

    db.execute("UPDATE sections SET nazwa=:nazwa, name=:name, opis=:opis, description=:description, instrumentSection=:instrumentSection WHERE id=:id",
                {"nazwa": nazwa, "name": name, "opis": opis, "description": description, "instrumentSection": int(instrumentSection), "id": int(id)})
    db.commit()
    return redirect(url_for('admin'))

@app.route("/add_sections", methods=["POST"])
def add_sections():
    # dodawanie nowych sekcji do bazy danych
    nazwa = request.form.get("nazwa")
    name = request.form.get("name")
    opis = request.form.get("opis")
    description = request.form.get("description")
    # okreslenie czy sekcja dotyczy instrumentow, aby poprawnie umiescic ja w nawigacji
    instrumentSection = 1 if request.form.get("instrumentSection") == "on" else 0

    db.execute("INSERT INTO sections (nazwa, name, opis, description, instrumentSection) VALUES (:nazwa, :name, :opis, :description, :instrumentSection)",
    {"nazwa": nazwa, "name": name, "opis": opis, "description": description, "instrumentSection": int(instrumentSection)})
    db.commit()

    return redirect(url_for("admin"))


@app.route("/add_instrument", methods=["POST"])
def add_instrument():
    # dodanie nowego instrumentu do bazy danych.
    nazwa = request.form.get("nazwa")
    name = request.form.get("name")
    opis = request.form.get("opis")
    description = request.form.get("description")
    # okreslenie ID sekcji w danych, aby poprawnie przypisywach instrument do kategorii
    section_id = request.form.get("section_id")

    db.execute("INSERT INTO instruments (nazwa, name, opis, description, section_id) VALUES (:nazwa, :name, :opis, :description, :section_id)",
    {"nazwa": nazwa, "name": name, "opis": opis, "description": description, "section_id": int(section_id)})
    db.commit()
    return redirect(url_for("admin"))

@app.route("/delete_instrument", methods=["POST"])
def delete_instrument():
    id = int(request.form.get("id"))
    db.execute("DELETE FROM instruments WHERE id=:id", {"id": id})
    db.commit()
    return redirect(url_for("admin"))

@app.route("/api/get_links")
def get_links():
    links = db.execute("SELECT nazwa, name, instrumentSection FROM 'sections'").fetchall()
    db.commit()
    output = [dict(row) for row in links]
    return (jsonify(output))


@app.route("/api/get_sections")
def get_sections():
    sections = db.execute("SELECT * FROM 'sections'").fetchall()
    db.commit()
    output = [dict(row) for row in sections]
    return jsonify(output)

@app.route("/api/get_instruments")
def get_instruments():
    instruments = db.execute("SELECT * FROM 'instruments'").fetchall()
    db.commit()
    output = [dict(row) for row in instruments]
    return jsonify(output)

@app.route("/api/get_landing")
def get_landing():
    landing = db.execute("SELECT * FROM 'landing'").fetchall()
    db.commit()
    output = [dict(row) for row in landing]
    return jsonify(output)
