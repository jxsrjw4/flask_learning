from flask import Blueprint,render_template

route_supplier = Blueprint("supplier_page", __name__)

@route_supplier.route("/index")
def index():
    return render_template("/supplier/index.html")

@route_supplier.route("/edit")
def edit():
    return render_template("/supplier/edit.html")

@route_supplier.route("/add")
def edit():
    return render_template("/supplier/add.html")