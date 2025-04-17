from flask import Blueprint
from application.services.task_service import Tasks_Services

home_blue = Blueprint("home_blue", __name__)
taskService = Tasks_Services()

@home_blue.route("/", methods=["GET", "POST"])
def home_index():
    tasks = taskService.gettingAllTask()
    return f"Task List: {tasks}"