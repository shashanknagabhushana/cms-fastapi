from fastapi import APIRouter, HTTPException
from app.crud import create_content, get_content_by_id, get_contents, update_content
from app.schemas.content_schema import ContentCreate, ContentOut

router = APIRouter(prefix="/content", tags=["Content"])

@router.post("/", response_model=ContentOut)
def add_content(content: ContentCreate):
    content_dict = content.dict()
    inserted_id = create_content(content_dict)
    return {**content_dict, "id": inserted_id}

@router.get("/{content_id}", response_model=ContentOut)
def read_content(content_id: str):
    content = get_content_by_id(content_id)
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    content["id"] = str(content["_id"])
    return content

@router.get("/", response_model=list[ContentOut])
def list_contents(skip: int = 0, limit: int = 10):
    contents = get_contents(skip, limit)
    for c in contents:
        c["id"] = str(c["_id"])
    return contents

@router.put("/{content_id}", response_model=ContentOut)
def edit_content(content_id: str, content: ContentCreate):
    updated = update_content(content_id, content.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Content not found")
    updated["id"] = str(updated["_id"])
    return updated
