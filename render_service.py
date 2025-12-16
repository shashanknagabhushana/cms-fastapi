from fastapi import HTTPException
from jinja2 import Environment, FileSystemLoader
from app.utils.cache import redis_client
from app.utils.db import content_collection
from bson import ObjectId
import os

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "..", "templates")
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))

def render_content(content_id: str):
    cache_key = f"rendered_page:{content_id}"

    # Check Redis cache
    cached_html = redis_client.get(cache_key)
    if cached_html:
        return cached_html

    # Fetch content from MongoDB
    if not ObjectId.is_valid(content_id):
        raise HTTPException(status_code=400, detail="Invalid content ID")
    content = content_collection.find_one({"_id": ObjectId(content_id)})
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")

    template_name = content.get("template", "content.html")
    template = env.get_template(template_name)

    html = template.render(
        title=content["title"],
        body=content["body"],
        tags=content.get("tags", []),
        date=content.get("date"),
        author=content.get("author")
    )

    # Store in Redis for 5 minutes
    redis_client.setex(cache_key, 300, html)

    return html
