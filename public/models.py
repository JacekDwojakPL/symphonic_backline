from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Section(db.Model):
    __tablename__ = "sections"
    id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    opis = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    instrumentSection = db.Column(db.Boolean, nullable=False)


class Instrument(db.Model):
    __tablename__ = "instruments"
    id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    opis = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    section_id = db.Column(db.Integer, db.ForeignKey("sections.id"), nullable=False)


class Landing(db.Model):
    __tablename__ = "landing"
    id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    opis = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
