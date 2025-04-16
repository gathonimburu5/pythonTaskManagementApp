from flask import Blueprint

comment_ctl = Blueprint("comment_ctl", __name__)

@comment_ctl.route("/")
def comment_page():
    return "Hello from comment page"