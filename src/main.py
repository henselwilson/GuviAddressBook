from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import geopy.distance
from database import engine, SessionLocal
from schemas import address, retriever
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
    addrLat="%.7f"%request.addressLat
    print(addrLat)
    addrLong="%.7f"%request.addressLong
    print(addrLong)
    new_addr = models.address(addressLat=addrLat, addressLong=addrLong)
    db.add(new_addr)
    db.commit()
    db.refresh(new_addr)

    return new_addr

@app.post('/retrieve')
def add_address(request: retriever, db: Session = Depends(get_db)):
    locLat=request.addressLat
    locLong=request.addressLong
    dist_range=request.rang
    coord=(locLat,locLong)
    print(coord)
    dbs = db.query(models.address).all()
    result=[]
    for row in dbs:
        lat1=row.addressLat
        print(lat1)
        long1=row.addressLong
        print(long1)
        coord1=(lat1,long1)
        dist=geopy.distance.geodesic(coord,coord1).km
        print(dist)
        if dist<dist_range:
            print(row)
            result.append(row)

    return result
"""
if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1")
"""