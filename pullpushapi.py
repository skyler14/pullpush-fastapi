from fastapi import FastAPI, Query, HTTPException
from fastapi.openapi.utils import get_openapi
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, Field
from typing import List, Optional, Union

app = FastAPI(
    title="PullPush Reddit API Documentation",
    description="Interactive documentation for the PullPush Reddit API",
    version="1.0.0",
)

OFFICIAL_API_URL = "https://api.pullpush.io"

class Comment(BaseModel):
    author: str
    body: str
    created_utc: int
    id: str
    link_id: str
    score: int
    subreddit: str

class Submission(BaseModel):
    author: str
    title: str
    selftext: str
    created_utc: int
    id: str
    score: int
    num_comments: int
    subreddit: str

class APIResponse(BaseModel):
    data: List[Union[Comment, Submission, str]]
    metadata: dict

@app.get("/", include_in_schema=False)
async def root():
    """Redirect to the API documentation."""
    return RedirectResponse(url="/docs")

@app.get("/reddit/search/comment/", response_model=APIResponse, include_in_schema=False)
async def search_comments():
    """This endpoint is for documentation purposes only."""
    raise HTTPException(status_code=501, detail="This is a documentation server. Please use the official API.")

@app.get("/reddit/search/submission/", response_model=APIResponse, include_in_schema=False)
async def search_submissions():
    """This endpoint is for documentation purposes only."""
    raise HTTPException(status_code=501, detail="This is a documentation server. Please use the official API.")

@app.get("/reddit/comment/ids/", response_model=APIResponse, include_in_schema=False)
async def get_comment_ids():
    """This endpoint is for documentation purposes only."""
    raise HTTPException(status_code=501, detail="This is a documentation server. Please use the official API.")

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="PullPush Reddit API Documentation",
        version="1.0.0",
        description="Interactive documentation for the PullPush Reddit API",
        routes=app.routes,
    )

    openapi_schema["servers"] = [{"url": OFFICIAL_API_URL}]

    # Initialize components and schemas if they don't exist
    if "components" not in openapi_schema:
        openapi_schema["components"] = {}
    if "schemas" not in openapi_schema["components"]:
        openapi_schema["components"]["schemas"] = {}

    # Add schema definitions
    openapi_schema["components"]["schemas"]["Comment"] = {
        "type": "object",
        "properties": {
            "author": {"type": "string"},
            "body": {"type": "string"},
            "created_utc": {"type": "integer"},
            "id": {"type": "string"},
            "link_id": {"type": "string"},
            "score": {"type": "integer"},
            "subreddit": {"type": "string"},
        },
    }

    openapi_schema["components"]["schemas"]["Submission"] = {
        "type": "object",
        "properties": {
            "author": {"type": "string"},
            "title": {"type": "string"},
            "selftext": {"type": "string"},
            "created_utc": {"type": "integer"},
            "id": {"type": "string"},
            "score": {"type": "integer"},
            "num_comments": {"type": "integer"},
            "subreddit": {"type": "string"},
        },
    }

    openapi_schema["components"]["schemas"]["APIResponse"] = {
        "type": "object",
        "properties": {
            "data": {
                "type": "array",
                "items": {
                    "oneOf": [
                        {"$ref": "#/components/schemas/Comment"},
                        {"$ref": "#/components/schemas/Submission"},
                        {"type": "string"},
                    ]
                },
            },
            "metadata": {"type": "object"},
        },
    }

    openapi_schema["paths"]["/reddit/search/comment/"] = {
        "get": {
            "summary": "Search Comments",
            "operationId": "search_comments",
            "parameters": [
                {"name": "q", "in": "query", "required": True, "schema": {"type": "string"}, "description": "Search term"},
                {"name": "subreddit", "in": "query", "schema": {"type": "string"}, "description": "Restrict to a specific subreddit"},
                {"name": "author", "in": "query", "schema": {"type": "string"}, "description": "Restrict to a specific author"},
                {"name": "size", "in": "query", "schema": {"type": "integer", "default": 100, "maximum": 100}, "description": "Number of results to return"},
                {"name": "sort", "in": "query", "schema": {"type": "string", "default": "desc", "enum": ["asc", "desc"]}, "description": "Sort order"},
                {"name": "after", "in": "query", "schema": {"type": "string"}, "description": "Return results after this date"},
                {"name": "before", "in": "query", "schema": {"type": "string"}, "description": "Return results before this date"},
            ],
            "responses": {
                "200": {
                    "description": "Successful Response",
                    "content": {"application/json": {"schema": {"$ref": "#/components/schemas/APIResponse"}}},
                }
            },
        }
    }

    openapi_schema["paths"]["/reddit/search/submission/"] = {
        "get": {
            "summary": "Search Submissions",
            "operationId": "search_submissions",
            "parameters": [
                {"name": "q", "in": "query", "required": True, "schema": {"type": "string"}, "description": "Search term"},
                {"name": "subreddit", "in": "query", "schema": {"type": "string"}, "description": "Restrict to a specific subreddit"},
                {"name": "author", "in": "query", "schema": {"type": "string"}, "description": "Restrict to a specific author"},
                {"name": "size", "in": "query", "schema": {"type": "integer", "default": 100, "maximum": 100}, "description": "Number of results to return"},
                {"name": "sort", "in": "query", "schema": {"type": "string", "default": "desc", "enum": ["asc", "desc"]}, "description": "Sort order"},
                {"name": "after", "in": "query", "schema": {"type": "string"}, "description": "Return results after this date"},
                {"name": "before", "in": "query", "schema": {"type": "string"}, "description": "Return results before this date"},
            ],
            "responses": {
                "200": {
                    "description": "Successful Response",
                    "content": {"application/json": {"schema": {"$ref": "#/components/schemas/APIResponse"}}},
                }
            },
        }
    }

    openapi_schema["paths"]["/reddit/comment/ids/"] = {
        "get": {
            "summary": "Get Comment IDs",
            "operationId": "get_comment_ids",
            "parameters": [
                {"name": "link_id", "in": "query", "required": True, "schema": {"type": "string"}, "description": "ID of the submission"},
            ],
            "responses": {
                "200": {
                    "description": "Successful Response",
                    "content": {"application/json": {"schema": {"$ref": "#/components/schemas/APIResponse"}}},
                }
            },
        }
    }

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)