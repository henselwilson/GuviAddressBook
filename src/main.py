from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import engine, SessionLocal
from schemas import address
import models
import uvicorn

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.get('/')
def home():
    data = { 'inner':{'in':'core'}}
    return data
@app.post('/add')
def add_address(request: address, db: Session = Depends(get_db)):

    new_addr = models.address(addressLat=request.addressLat, addressLong=request.addressLong)
    db.add(new_addr)
    db.commit()
    db.refresh(new_addr)

    return new_addr
"""
if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1")
"""