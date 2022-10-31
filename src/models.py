import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import database as _database

class User(_database.Base):
    __tablename = 'address'
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    address = _sql.Column(_sql.Float,index=True)

    posts = _orm.relationship("Post", back_populates="owner")

