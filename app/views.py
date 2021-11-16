from flask import render_template, request
from models import Besticons, Log, Besticons
import os
from datetime import date
import warnings

warnings.filterwarnings("ignore")


def index():
    if request.method == 'POST':
        query = str(request.form["url"])
        if(query[-1] == "/"):
            query = query[:-1]
        faviconurl = query+"/favicon.ico"
        return render_template("index.html", query=query, faviconurl=faviconurl)

    return render_template("index.html", logcount=len(log_read()), besticoncount=len(besticons_read()))


def docs():
    return render_template("docs.html")


def api():
    return "<h1>API</h1>"


def log_add(result):

    from app import db
    today = date.today()
    today = today.strftime("%b-%d-%Y")
    data = Log(date=today, result=result)
    db.session.add(data)
    db.session.commit()


def log_read():
    from app import db

    all = Log.query.all()
    print(all)
    return all


def besticons_read():
    from app import db

    all = Besticons.query.all()
    print(all)
    return all


def besticons_add(url, iconurl):

    from app import db
    data = Besticons(url=url, iconurl=iconurl)
    db.session.add(data)
    db.session.commit()
