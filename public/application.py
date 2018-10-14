import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask, render_template, jsonify

path = os.path.abspath("./")
url = os.path.join(path, "data.db")
engine = create_engine("sqlite:///"+url)
db = scoped_session(sessionmaker(bind=engine))
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/api/get_sections")
def get_sections():
    sections = db.execute("SELECT * FROM 'sections'").fetchall()
    output = [dict(row) for row in sections]
    return jsonify(output)

@app.route("/api/get_landing")
def get_landing():
    landing = db.execute("SELECT * FROM 'landing'").fetchall()
    output = [dict(row) for row in landing]
    return jsonify(output)
