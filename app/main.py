from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, users, auth, vote
from .config import Settings
from fastapi.middleware.cors import CORSMiddleware

#print(settings.database_password)
models.Base.metadata.create_all(bind=engine)
app = FastAPI()
#11:50:32
origins = ["https://www.google.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return{"message": "Hellow World!!!"}


# my_posts = [{"userid": "user id of post1","password": "paswsword of post1","id": 1},
#             {"userid": "userid of post2", "password:": "password ko to","id": 2}]
# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p

# def find_index_post(id):
#     for i,p in enumerate(my_posts):
#         if p['id'] == id:
#             return i



