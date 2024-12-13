from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated

from app.models import User
from app.schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete

from slugify import slugify

router = APIRouter(prefix='/user', tags=['user'])




@router.get('/')
async def all_users(): #(db: Annotated[Session, Depends(get_db)]):
    pass
    # users = db.scalars(select(User)).all()
    # return users
'''
@router.get("/")
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users
'''
@router.get('/user_id')
async def user_by_id():
    pass


@router.post('/create')
async def create_user(db: Annotated[Session, Depends(get_db)], create_user: CreateUser):
    db.execute(insert(User).values(username=create_user.username,
                                   firstname=create_user.firstname,
                                   lastname=create_user.lastname,
                                   age=create_user.age,
                                   slug=slugify(create_user.username)))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED,
            'transaction': 'Successful'
            }


@router.put('/update')
async def update_user():
    pass


@router.delete('/delete')
async def delete_user():
    pass
