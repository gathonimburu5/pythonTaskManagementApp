from flask import Blueprint, render_template, redirect, url_for, flash, request
from application.services.task_service import Tasks_Services

home_blue = Blueprint("home_blue", __name__)
taskService = Tasks_Services()

@home_blue.route("/", methods=["GET", "POST"])
def home_index():
    if request.method == "GET":
        tasks = taskService.gettingAllTask()
        return render_template("task.html", tasks = tasks)