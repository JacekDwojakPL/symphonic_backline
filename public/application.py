import os

from flask import Flask, flash, render_template, request, jsonify, redirect, url_for, session
from passlib.hash import pbkdf2_sha256
from models import *
from helpers import to_dict

path = os.path.abspath("./")
db_path = os.path.join(path, "data.db")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_path
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

db.init_app(app)


@app.route("/")
def main():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        admin = Users.query.first()
        password = request.form.get("password")
        hash = admin.password_hash
        if pbkdf2_sha256.verify(password, hash) and request.form.get("name") == "admin":
            session["admin"] = True
            return redirect(url_for("admin"))
        else:
            flash("Nieprawidłowa nazwa użytkownika lub hasło")
            return redirect(url_for("login"))


@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "GET" and "admin" in session:
        sections = Section.query.all()
        instruments = Instrument.query.all()
        landing = Landing.query.first()
        return render_template("admin.html", sections=sections, instruments=instruments, landing=landing)
    else:
        return redirect(url_for("login"))


@app.route("/edit_landing", methods=["POST"])
def edit_landing():
    nazwa = request.form.get("nazwa")
    name = request.form.get("name")
    opis = request.form.get("opis")
    description = request.form.get("description")

    landing = Landing.query.first()
    landing.nazwa = nazwa
    landing.name = name
    landing.opis = opis
    landing.description = description

    db.session.add(landing)
    db.session.commit()

    return redirect(url_for("admin"))

@app.route("/add_sections", methods=["POST"])
def add_sections():
    # dodawanie nowych sekcji do bazy danych
    nazwa = request.form.get("nazwa")
    name = request.form.get("name")
    opis = request.form.get("opis")
    description = request.form.get("description")
    # okreslenie czy sekcja dotyczy instrumentow, aby poprawnie umiescic ja w nawigacji
    instrumentSection = 1 if request.form.get("instrumentSection") == "on" else 0

    new_section = Section(nazwa=nazwa, name=name, opis=opis, description=description, instrumentSection=instrumentSection)
    db.session.add(new_section)
    db.session.commit()

    return redirect(url_for("admin"))

@app.route("/edit_sections", methods=["POST"])
def edit_sections():
    id = request.form.get("id")
    nazwa = request.form.get("nazwa")
    name = request.form.get("name")
    opis = request.form.get("opis")
    description = request.form.get("description")
    instrumentSection = 1 if request.form.get("instrumentSection") == "on" else 0

    section_to_edit = Section.query.get(int(id))
    section_to_edit.nazwa = nazwa
    section_to_edit.name = name
    section_to_edit.opis = opis
    section_to_edit.description = description
    section_to_edit.instrumentSection = instrumentSection
    db.session.add(section_to_edit)
    db.session.commit()

    return redirect(url_for('admin'))

@app.route("/add_instrument", methods=["POST"])
def add_instrument():
    # dodanie nowego instrumentu do bazy danych.
    nazwa = request.form.get("nazwa")
    name = request.form.get("name")
    opis = request.form.get("opis")
    description = request.form.get("description")
    # okreslenie ID sekcji w danych, aby poprawnie przypisywach instrument do kategorii
    section_id = request.form.get("section_id")

    new_instrument = Instrument(nazwa=nazwa, name=name, opis=opis, description=description, section_id=section_id)
    db.session.add(new_instrument)
    db.session.commit()

    return redirect(url_for("admin"))

@app.route("/delete_instrument", methods=["POST"])
def delete_instrument():
    id = int(request.form.get("id"))
    #db.execute("DELETE FROM instruments WHERE id=:id", {"id": id})
    #db.commit()
    instrument_to_delete = Instrument.query.get(id)
    db.session.delete(instrument_to_delete)
    db.session.commit()

    return redirect(url_for("admin"))

@app.route("/api/get_links")
def get_links():
    links = Section.query.all()
    output = to_dict(links)

    return (jsonify(output))

@app.route("/api/get_sections")
def get_sections():
    sections = Section.query.all()
    output = to_dict(sections)

    return jsonify(output)

@app.route("/api/get_instruments")
def get_instruments():
    instruments = Instrument.query.all()
    output = to_dict(instruments)

    return jsonify(output)

@app.route("/api/get_landing")
def get_landing():
    landing = Landing.query.all()
    output = to_dict(landing)

    return jsonify(output)

def create_database():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        create_database()
