from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

posts: list[dict] = [
    {
        "id": 1,
        "author": "Mohamed Ali",
        "title": "Getting Started with Node.js",
        "content": "Node.js is a runtime environment that allows you to run JavaScript on the server side...",
        "date_posted": "2026-04-01T10:30:00Z"
    },
    {
        "id": 2,
        "author": "Sara Ben",
        "title": "Understanding REST APIs",
        "content": "REST APIs are a way for systems to communicate over HTTP using standard methods like GET, POST, PUT, DELETE...",
        "date_posted": "2026-04-02T14:15:00Z"
    },
    {
        "id": 3,
        "author": "Youssef Karim",
        "title": "MongoDB Basics",
        "content": "MongoDB is a NoSQL database that stores data in flexible, JSON-like documents...",
        "date_posted": "2026-04-03T09:00:00Z"
    },
    {
        "id": 4,
        "author": "Lina Haddad",
        "title": "Intro to Express.js",
        "content": "Express.js is a minimal and flexible Node.js web application framework...",
        "date_posted": "2026-04-04T18:45:00Z"
    },
    {
        "id": 5,
        "author": "Ahmed Saidi",
        "title": "Async/Await in JavaScript",
        "content": "Async/await makes it easier to write promises in a synchronous style...",
        "date_posted": "2026-04-05T12:20:00Z"
    }
]

# Using response_class=HTMLResponse To Send HTML
# Using include_in_schema=False To Hide This Routes From The API Documentation
@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{posts[0]['title']}</h1>"

@app.get("/api/posts")
def get_posts():
    return posts