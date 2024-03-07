from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'Jay','surname':'Parsana'}}

@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data':f'{limit} published blog from db'}
    else:
        return {'data':f'{limit} blog from db'}
    
class Blog(BaseModel):
    title: str
    body: str
    Published: Optional[bool] = None

@app.post('/blog')
def create_blog(request: Blog):
    # return request
    return {'data': {'title': f'my first blog title is {request.title}',
                     'body':request.body,
                     'published':request.Published}
                     }

@app.get('/about')
def about():
    return {'data':{'about page'}}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blog'}

@app.get('/blog/{id}')  # dynamic routing
def show(id: int):
    return {'data':id}

@app.get('/blog/{id}/comments')
def comments(id: int):
    return {'data':{'1','2'}}