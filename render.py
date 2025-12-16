from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from app.services.render_service import render_content

router = APIRouter(prefix="/pages", tags=["Render"])

@router.get("/{content_id}/render", response_class=HTMLResponse)
def render_page(content_id: str):
    return render_content(content_id)
