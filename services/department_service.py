from sql.crud import get_all_deptts,add_deptt,update_deptt,
from sqlalchemy.orm import session
from sql.models import Department,Employee


def get_all_departments(db:session):
	return get_all_deptts(db)
	
def add_a_department(data:dict,db:session):
	return add_deptt(data,db)
	
def update_a_department(data:dict,deptt_id:int,db:session):
	return update_deptt(data,deptt_id,db)

def delete_a_department(deptt_id:int,db:session):
	if deptt.id == Employee.id:
		return delete_deptt(deptt_id,db)
	else:
		return "Department not exist"
