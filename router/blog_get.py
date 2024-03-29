from fastapi import APIRouter,status, Response
from enum import Enum
from typing import Optional

router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)


# @router.get('/blog/all')
# def get_all_blogs():
#     return {"message": "All Blogs provided"}

@router.get(
      "/blog/all",
      summary="Get All Blogs",
      description="Get all blogs with pagination support",
      response_description="List of available blogs",
      )
def get_all_blogs(page=1, page_size: Optional[int] = None):
    return {"message": f"Page is {page} and Page Size is {page_size}"}

@router.get("/blog/{id}/comments/{comment_id}", tags=["comment"])
def get_blog_comments(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
   """
   Simulates retrieving a comment of a blog

   - **id**: mandatory path parameter
    - **comment_id**: mandatory path parameter
    - **valid**: optional query parameter
    - **username**: optional query parameter
   """
   
   return {"blog_id": id, "comment_id": comment_id, "valid": valid, "username": username} 
    
class BlogType(str,Enum):
    short= "short"
    story= "story"
    howto= "howto"

@router.get("/blog/type/{type}")
def get_blog_type(type: BlogType):
    return {"message": f"Blog Type is {type}"}

@router.get("/blog/{id}",status_code=status.HTTP_200_OK)
def get_blog(id: int, response : Response):
  if id > 5:
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"error": "Blog not found"}
  else:
    response.status_code = status.HTTP_200_OK
    return {"message": f"Blog with ID {id} is provided"}
  
  