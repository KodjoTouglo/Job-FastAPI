from fastapi import APIRouter

from route import users, jobs


api_router = APIRouter()
api_router.include_router(users.router, prefix="/user", tags=["users"])
api_router.include_router(jobs.router, prefix="/job", tags=["jobs"])