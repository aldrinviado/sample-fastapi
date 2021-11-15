from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm.util import randomize_unitofwork
from .. import models,schemas,oauth2
from typing import Optional, List  
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..database import get_db 

router = APIRouter(prefix="/posts",tags=['Posts'])


#@router.get("/",response_model=List[schemas.PostResponse])
@router.get("/",response_model=List[schemas.Postout])
def read_users(db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user),limit: int = 10,skip: int = 0, search: Optional[str] = ""):
    #que = db.query(models.Posts).filter(models.Posts.user_id == current_user.id).filter(models.Posts.title.contains(search)).limit(limit).offset(skip).all()
    que = db.query(models.Posts).filter(models.Posts.title.contains(search)).limit(limit).offset(skip).all()
    results = db.query(models.Posts, func.count(models.Votes.post_id).label("votes")).join(models.Votes, models.Votes.post_id == models.Posts.id,isouter=True).group_by(models.Posts.id),filter(models.Posts.title.contains(search)).limit(limit).offset(skip).all()
  #  que = db.query(models.Posts).filter(models.Posts.content.contains(search)).limit(limit).offset(skip).all()
    
    return results



# @app.get("/login")
# def Login_User():
#     return {"message": "Hello World This is Aldrin!"}


# @app.get("/password")
# def login_password():
#     cur.execute("""SELECT * FROM posts """)
#     posts = cur.fetchall()
#     print(posts)
#     return{"data": posts}

@router.get("/{id}",response_model=schemas.PostResponse)
def get_post(id: int, response: Response,db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    post = db.query(models.Posts).filter(models.Posts.id == id).first()

    # cur.execute("SELECT * from posts where id = %s",(str(id)))
    # post = cur.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return{"message": f"post with id: {id} was not found"}
    if post.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized to delete post")
    return post




@router.post("/",status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def create_posts(post: schemas.PostCreate,db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
   # print(current_user.email)
   # print(current_user.id)
    new_post = models.Posts(user_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    # cur.execute("""INSERT INTO posts (userid,password,published) VALUES(%s,%s,%s) RETURNING *""",
    #                 (new_post.userid,new_post.password,new_post.published))
    # created_post = cur.fetchone()
    # conn.commit()
   # post_dict = new_post.dict()
   # post_dict['id'] = randrange(0,100)
   # print(new_post.dict())
   #  my_posts.append(post_dict)
    return new_post
   



@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Posts).filter(models.Posts.id == id)
    # deleting of post
    # find the index in the array that has required ID
    #my_posts.pop(index)
    # cur.execute("DELETE FROM posts WHERE id = %s returning *",(str(id),))
    # deleted_post = cur.fetchone()
    # conn.commit()
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} does not exist")
    
    if post.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized to delete post")
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

    

@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED,response_model=schemas.PostResponse)
def update_post(id: int,post_1: schemas.PostUpdate,db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):

    updated_post = db.query(models.Posts).filter(models.Posts.id == id)
    post = updated_post.first()

    # cur.execute("UPDATE posts SET userid = %s, password = %s WHERE id = %s RETURNING *",(post.userid,post.password,(str(id),)))
    # updated_post = cur.fetchone()
    # conn.commit()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} does not exist")
    if post.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized to update the post")
    updated_post.update(post_1.dict(),synchronize_session=False)
    db.commit()
    return updated_post.first()

####################################################################################################################################
####################################################################################################################################
####################################################################################################################################