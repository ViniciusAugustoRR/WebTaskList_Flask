from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime




db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable = False)
    date_creation = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' %self.id



