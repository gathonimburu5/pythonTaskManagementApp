from application.extension import db
from sqlalchemy import Table

class TaskTbl(db.Model):
    _table_ = Table("task_tbl", db.metadata, autoload_with=db.engine)

class CommentTbl(db.Model):
    _table_ = Table("comment_tbl", db.metadata, autoload_with=db.engine)