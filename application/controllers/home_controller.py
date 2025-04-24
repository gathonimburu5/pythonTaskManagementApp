from flask import Blueprint, render_template, redirect, url_for, flash, request
from application.services.task_service import Tasks_Services

home_blue = Blueprint("home_blue", __name__)
taskService = Tasks_Services()

@home_blue.route("/", methods=["GET", "POST"])
def home_index():
    if request.method == "GET":
        tasks = taskService.gettingAllTask()
        return render_template("task.html", tasks = tasks)

    if request.method == "POST":
        data = request.form
        taskService.createTaskRecords(data)
        return redirect(url_for('home_blue.home_index'))

@home_blue.route("/start/<int:id>", methods=["GET", "POST"])
def start_page(id):
    details = taskService.getTaskPerId(id)
    if request.method == "GET":
        return render_template("start_modal.html", details = details)

    if request.method == "POST":
        data = request.form
        taskService.startTask(data, id)
        return redirect(url_for('home_blue.home_index'))

@home_blue.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_page(id):
    taskDetails = taskService.getTaskPerId(id)
    if request.method == "GET":
        return render_template("edit_modal.html", taskDetails = taskDetails)

    if request.method == "POST":
        data = request.form
        taskService.updateTask(data, id)
        return redirect(url_for('home_blue.home_index'))

@home_blue.route("/comment/<int:id>", methods=["GET", "POST"])
def comment_page(id):
    tasks = taskService.getTaskPerId(id)
    if request.method == "GET":
        return render_template("comment_modal.html", tasks = tasks)

    if request.method == "POST":
        data = request.form
        taskService.taskComments(data, id)
        return redirect(url_for('home_blue.home_index'))