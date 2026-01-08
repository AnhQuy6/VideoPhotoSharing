from fastapi import FastAPI, HTTPException

app = FastAPI()

text_posts={1: {"title": "New Post", "content": "This is my first post"},
            2: {"title": "New Post 2", "content": "This is my second post"}
            }

@app.get("/posts")
def get_all_posts():
    return text_posts

@app.get("/posts/{id}")
def get_post_by_id(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    else:
        text_posts.get(id)