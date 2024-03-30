from fastapi import APIRouter,Query,Body, Path
from pydantic import BaseModel
from fastapi.params import Body
from typing import Optional,List,Dict

router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)

class ImageModel(BaseModel):
    url: str
    alias: str

class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published: Optional[bool] 
    tags: List[str]=[]
    metadata: Dict[str,str]={'key1':'val1'}
    image: Optional[ImageModel]=None


@router.post('/new')
def create_blog(blog: BlogModel, id: int, version: int =1):
    return {
        'id': id,
        'data': blog,
        'version': version,
        }

@router.post('new/{id}/comment/{comment_id}')
def create_comment(
    blog: BlogModel, 
    id: int, 
    comment_title: str = Query(
          None,
          title="Title of the comment",
          description="Some description for comment_title",
          alias="commentTitle",
          deprecated=True,),
    content: str = Body(...,
                        min_length=10,
                        max_length=50,
                        regex='^[a-z\s]*$',),
    v: Optional[List[str]] = Query(['1.0', '1.1'], title="API Version"),
    comment_id: int = Path(..., gt=5,le=10)
    ):
    return {
        'blog': blog,
        'id': id,
        'comment_title': comment_title,
        'comment_id': comment_id,
        'content': content,
        'version': v
        }
