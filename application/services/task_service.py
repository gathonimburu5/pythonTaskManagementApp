from application.extension import db
from application.models import TaskTbl, CommentTbl
from datetime import datetime

class Tasks_Services():
    def gettingAllTask(self):
        return TaskTbl.query.all()

    def createTaskRecords(self, data):
        new_task = TaskTbl(
            Title = data.get('title'),
            Description = data.get('description'),
            Status = data.get('status'),
            Hours = data.get('hours'),
            PlannedStartDate = data.get('planned_start_date'),
            PlannedEndDate = data.get('planned_end_date'),
            CreatedOn = datetime.utcnow(),
            CreatedBy = 1
        )
        db.session.add(new_task)
        db.session.commit()


