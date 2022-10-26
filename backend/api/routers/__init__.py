from . import authentication as auth,blog,user

from fastapi import APIRouter



routers = APIRouter(
    prefix='/api'
)

routers.include_router(auth.router)
routers.include_router(blog.router)
routers.include_router(user.router)

