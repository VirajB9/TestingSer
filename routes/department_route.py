from fastapi import APIRouter,Depends
from sql.database import get_db
from services.department_service import get_all_departments,add_a_department,update_a_department,delete_a_department



department_router = APIRouter( prefix = "/departments", tags = ["Departments"])

@department_router.get("/", summary = "get all departments")
def get_departments(db = Depends(get_db)):
	return get_all_departments(db)
	
@department_router.post("/", summary = "add a department")
def add_department(data:dict,db = Depends(get_db)):
	return add_a_department(data,db)

@department_router.put("/{id}",summary = "update a department with id")
def update_department(data:dict, deptt_id:int,db = Depends(get_db)):
	return update_a_department(data,deptt_id,db)
	
@department_router.delete("/{id}",summary = "delete a department with id")
def delete_department(data:dict,deptt_id:int,db = Depends(get_db)):
	return delete_a_department(data,deptt_id,db)
