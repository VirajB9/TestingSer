from sql.crud import get_all_deptts,add_deptt,update_deptt,delete_deptt
from sqlalchemy.orm import Session
from sql.models import Department,Employee


def get_all_departments(db:Session):
	return get_all_deptts(db)
	
def add_a_department(data:dict,db:Session):
	return add_deptt(data,db)
	
def update_a_department(data:dict,deptt_id:int,db:Session):
	return update_deptt(data,deptt_id,db)

def delete_a_department(deptt_id:int,db:Session):
		return delete_deptt(deptt_id,db)

