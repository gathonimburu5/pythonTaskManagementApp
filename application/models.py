from application.extension import db
from sqlalchemy import Table

class TaskTbl(db.Model):
    __table__ = Table("task_tbl", db.metadata, autoload_with=db.engine)

class CommentTbl(db.Model):
    __table__ = Table("comment_tbl", db.metadata, autoload_with=db.engine)