from sqlalchemy.orm import session
from sql.models import Department, Employee


def get_all_deptts(db: session):
    deptt = db.query(Department).all()
    return deptt


def add_deptt(data: dict, db: session):
    deptt = Department(**data)
    db.add(deptt)
    db.commit()
    db.refresh(deptt)

    return deptt


def update_deptt(data: dict, deptt_id: int, db: session):
    deptt = db.query(Department).filter(Department.id = deptt_id).first()

    for key, value in data.items():
        setattr(deptt, key, value)

    db.commit()
    db.refresh(deptt)
    return deptt


def delete_deptt(deptt_id: int, db: session):
    deptt = db.query(Department).filter(Department.id = deptt_id).first()
    db.delete(deptt)
    db.commit()
    return True


def get_all_emps(db: session):
    emp = db.query(Employee).all()
    return emp


def add_emp(data: dict, db: session):
    emp = Employee(**data)
    db.add(emp)
    db.commit()
    db.refresh(emp)
    return emp


def update_emp(data: dict, deptt_id: int, db: session):
    emp = = db.query(Employee).filter(Employee.id = emp_id).first()

    for key, value in data.items():
        setattr(emp, key, value)

    db.commit()
    db.refresh(emp)
    return emp


def delete_emp(emp_id: int, db: session):
    emp = db.query(Employee).filter(Employee.id = emp_id).first()
    db.delete(emp)
    db.commit()
    return True