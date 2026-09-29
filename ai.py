from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/ai", tags=["AI Features"])


class BlogContent(BaseModel):
    content: str


@router.post("/summarize")
def summarize_blog(data: BlogContent):
    words = data.content.split()

    if len(words) <= 30:
        summary = data.content
    else:
        summary = " ".join(words[:30]) + "..."

    return {
        "summary": summary,
        "word_count": len(words),
        "message": "Blog summary generated successfully"
    }