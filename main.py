from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from database import Base, engine, SessionLocal
from models import Blog
from ai import router as ai_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI BlogNest API",
    description="AI-powered Blog Management API",
    version="1.0.0"
)
app.include_router(ai_router)

# Database connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Blog request model
class BlogCreate(BaseModel):
    title: str
    content: str
    author: str
    category: str | None = None


# Home
@app.get("/")
def home():
    return {
        "message": "Welcome to AI BlogNest API",
        "status": "running"
    }


# Health check
@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


# Create blog
@app.post("/blogs")
def create_blog(blog: BlogCreate, db: Session = Depends(get_db)):
    new_blog = Blog(
        title=blog.title,
        content=blog.content,
        author=blog.author,
        category=blog.category
    )

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog


# Get all blogs
@app.get("/blogs")
def get_blogs(db: Session = Depends(get_db)):
    return db.query(Blog).all()


# Get one blog
@app.get("/blogs/{blog_id}")
def get_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()

    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    return blog


# Update blog
@app.put("/blogs/{blog_id}")
def update_blog(
    blog_id: int,
    blog_data: BlogCreate,
    db: Session = Depends(get_db)
):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()

    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    blog.title = blog_data.title
    blog.content = blog_data.content
    blog.author = blog_data.author
    blog.category = blog_data.category

    db.commit()
    db.refresh(blog)

    return blog


# Delete blog
@app.delete("/blogs/{blog_id}")
def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()

    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    db.delete(blog)
    db.commit()

    return {
        "message": "Blog deleted successfully"
    }