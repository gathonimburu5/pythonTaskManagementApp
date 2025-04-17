from flask import Blueprint, render_template, redirect, url_for, flash

dashboard_ctrl = Blueprint('dashboard_ctrl', __name__)

@dashboard_ctrl.route("/", methods=["GET", "POST"])
def dashboard_page():
    return render_template("dashboard.html")