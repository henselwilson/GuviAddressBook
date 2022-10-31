import sqlalchemy as _sql
import sqlalchemy.orm as _orm
from database import Base

class address(Base):
    __tablename__ = 'address'
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    addressLat = _sql.Column(_sql.Float,index=True)
    addressLong = _sql.Column(_sql.Float,index=True)


