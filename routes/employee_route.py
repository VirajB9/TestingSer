from fastapi import APIRouter,Depends
from sql.database import get_db
from services.employee_service import get_all_employees,add_a_employee,update_a_employee,delete_a_employee



employee_router = APIRouter( prefix = "/employees", tags = ["Employees"])

@employee_router.get("/", summary = "get all employees")
def get_employees(db = Depends(get_db)):
	return get_all_employees(db)
	
@employee_router.post("/", summary = "add a employee")
def add_employee(data:dict,db = Depends(get_db)):
	return add_a_employee(data,db)

@employee_router.put("/{id}",summary = "update a employee with id")
def update_employee(data:dict,emp_id:int,db = Depends(get_db)):
	return update_a_employee(data,emp_id,db)
	
@employee_router.delete("/{id}",summary = "delete a employee with id")
def delete_employee(emp_id:int,db = Depends(get_db)):
	return delete_a_employee(emp_id,db)
