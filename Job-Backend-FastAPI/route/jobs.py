from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session

from data.session import get_db

from models.jobs import Job

from schemas.jobs import JobCreate, ShowJob

from repository.jobs import create_new_job, retrieve_job, list_job, update_job, delete_job


router = APIRouter()


@router.post("/create_job", response_model=ShowJob)
def create_job(job: JobCreate, db:Session=Depends(get_db)):
    owner_id = 1
    job = create_new_job(job=job, db=db, owner_id=owner_id)
    return job

@router.get("/get/{id}", response_model=ShowJob)
def retrieve_job_by_id(id: int, db: Session=Depends(get_db)):
    job = retrieve_job(id=id, db=db)
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                      detail=f"Job with id {id} does not exist.")
    return job

@router.get("/all", response_model=List[ShowJob])
def retrieve_all_jobs(db: Session=Depends(get_db)):
    jobs = list_job(db=db)
    return jobs

@router.put("/update/{id}")
def update_job_by_id(id: int, job:JobCreate, db:Session=Depends(get_db)):
    owner_id = 1
    message = update_job(id=id, job=job, db=db, owner_id=owner_id)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Job with id {id} does not exist.")
    return {"detail": "Job updated"}

@router.delete("/delete/{id}")
def delete_job_by_id(id: int, db:Session=Depends(get_db)):
    owner_id = 1
    message = delete_job(id=id, db=db, owner_id=owner_id)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Job with id {id} does not exist.")
    return {"detail": "Job deleted."}