from sqlalchemy.orm import Session
from blog_Api import models, schemas


def create_blog(db: Session, blog: schemas.BlogCreate):
    new_blog = models.Blog(
        title=blog.title,
        content=blog.content,
        author=blog.author
    )

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog


def get_blogs(db: Session):
    return db.query(models.Blog).all()


def get_blog(db: Session, blog_id: int):
    return db.query(models.Blog).filter(models.Blog.id == blog_id).first()


def update_blog(db: Session, blog_id: int, blog: schemas.BlogUpdate):
    existing_blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()

    if existing_blog:
        existing_blog.title = blog.title
        existing_blog.content = blog.content
        db.commit()
        db.refresh(existing_blog)

    return existing_blog


def delete_blog(db: Session, blog_id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()

    if blog:
        db.delete(blog)
        db.commit()

    return blog