from application.extension import db
from application.models import TaskTbl, CommentTbl
from datetime import datetime

class Tasks_Services():
    def gettingAllTask(self):
        return TaskTbl.query.all()

    def createTaskRecords(self, data):
        new_task = TaskTbl(
            title = data.get('title'),
            description = data.get('description'),
            status = data.get('status'),
            hours = data.get('hours'),
            planned_start_date = data.get('planned_start_date'),
            planned_end_date = data.get('planned_end_date'),
            created_on = datetime.utcnow(),
            created_by = 1
        )
        db.session.add(new_task)
        db.session.commit()

    def getTaskPerId(self, id):
        return TaskTbl.query.get_or_404(id)

    def updateTask(self, data, id):
        task_to_edit = TaskTbl.query.get_or_404(id)
        task_to_edit.title = data.get('title')
        task_to_edit.status = data.get('status')
        task_to_edit.hours = data.get('hours')
        task_to_edit.planned_start_date = data.get('planned_start_date')
        task_to_edit.planned_end_date = data.get('planned_end_date')
        task_to_edit.description = data.get('description')
        task_to_edit.modified_on = datetime.utcnow()
        task_to_edit.modified_by = 1
        db.session.commit()

    def startTask(self, data, id):
        task_detail = TaskTbl.query.get_or_404(id)
        task_detail.actual_start_date = data.get('actual_start_date')
        task_detail.actual_end_date = data.get('actual_end_date')
        db.session.commit()

    def taskComments(self, data, id):
        task_record = TaskTbl.query.get_or_404(id)
        comment_data = CommentTbl(
            task_id = task_record.id,
            title = data.get('title'),
            description = data.get('description'),
            created_on = datetime.utcnow(),
            created_by = 1
        )

        db.session.add(comment_data)
        db.session.commit()

    def getCommentList(self):
        return CommentTbl.query.all()


