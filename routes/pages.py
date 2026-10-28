from flask import Blueprint, render_template, request, redirect, url_for
from models.BakeryItem import BakeryItem



pages = Blueprint("pages", __name__)




@pages.route("/")
def index():
    items = BakeryItem.query.all()

    return render_template("index.html", bakery_items=items)







