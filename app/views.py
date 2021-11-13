from flask import render_template, request
from models import Log
import os
from datetime import date
import warnings
warnings.filterwarnings("ignore")


def index():
    if request.method == 'POST':
        return "got a post request"

    return render_template("index.html", count=result_db_count())


def docs():
    return render_template("docs.html")


def db_add(result):

    from app import db
    today = date.today()
    today = today.strftime("%b-%d-%Y")
    data = Log(date=today, result=result)
    db.session.add(data)
    db.session.commit()


def db_read():
    from app import db

    all = Log.query.all()
    print(all)


def result_db_count():
    from app import db

    try:
        all = Log.query.all()
        return len(all)
    except:
        return "many"
