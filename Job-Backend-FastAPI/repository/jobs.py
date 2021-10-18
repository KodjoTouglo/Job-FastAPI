from sqlalchemy.orm import Session

from schemas.jobs import JobCreate

from models.jobs import Job



def create_new_job(job: JobCreate, db:Session, owner_id:int):
    job = Job(**job.dict(), owner_id=owner_id)
    db.add(job)
    db.commit()
    db.refresh(job)
    return job

def retrieve_job(id: int, db:Session):
    job = db.query(Job).filter(Job.id==id).first()
    return job

def list_job(db: Session):
    jobs = db.query(Job).filter(Job.is_active==True).all()
    return jobs

def update_job(id: int, job:JobCreate, db:Session, owner_id: int):
    jobs = db.query(Job).filter(Job.id==id)
    if not jobs.first():
        return False
    job.__dict__.update(owner_id=owner_id)
    jobs.update(job.__dict__)
    db.commit()
    return True

def delete_job(id:int, db:Session, owner_id):
    jobs = db.query(Job).filter(Job.id==id)
    if not jobs.first():
        return False
    jobs.delete(synchronize_session=False)
    db.commit()
    return True