from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from blog_Api import schemas, models, crud

from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# POST
@app.post("/blogs", status_code=201)
def create_blog(blog: schemas.BlogCreate, db: Session = Depends(get_db)):
    return crud.create_blog(db, blog)


# GET all blogs
@app.get("/blogs")
def get_blogs(db: Session = Depends(get_db)):
    return crud.get_blogs(db)


# GET blog by id
@app.get("/blogs/{id}")
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = crud.get_blog(db, id)

    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    return blog


# PUT update blog
@app.put("/blogs/{id}")
def update_blog(id: int, blog: schemas.BlogUpdate, db: Session = Depends(get_db)):
    updated_blog = crud.update_blog(db, id, blog)

    if not updated_blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    return updated_blog


# DELETE blog
@app.delete("/blogs/{id}")
def delete_blog(id: int, db: Session = Depends(get_db)):
    deleted_blog = crud.delete_blog(db, id)

    if not deleted_blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    return {"message": "Blog deleted successfully"}