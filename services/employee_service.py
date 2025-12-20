from sql.crud import get_all_emps, add_emp, update_emp, delete_emp
from sqlalchemy.orm import session
from sql.models import Department, Employee


def get_all_employees(db: session):
    return get_all_emps(db)


def add_a_employee(data: dict, db: session):
    return add_emp(data, db)


def update_a_employee(data: dict, emp_id: int, db: session):
    return update_emp(data, emp_id, db)


def delete_a_employee(emp_id_id: int, db: session):
    return delete_emp(emp_id, db)