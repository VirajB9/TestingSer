from sqlalchemy.orm import Session
from sql.models import Department, Employee


def get_all_deptts(db:Session):
    deptt = db.query(Department).all()
    return deptt


def add_deptt(data: dict, db: Session):
    deptt = Department(**data)
    db.add(deptt)
    db.commit()
    db.refresh(deptt)

    return deptt


def update_deptt(data: dict, deptt_id: int, db: Session):
    deptt = db.query(Department).filter(Department.id==deptt_id).first()

    for key, value in data.items():
        setattr(deptt, key, value)

    db.commit()
    db.refresh(deptt)
    return deptt


def delete_deptt(deptt_id: int, db: Session):
    deptt = db.query(Department).filter(Department.id==deptt_id).first()
    if deptt is None:
        return False
    db.delete(deptt)
    db.commit()
    return True


def get_all_emps(db: Session):
    emp = db.query(Employee).all()
    return emp


def add_emp(data: dict, db: Session):
    emp = Employee(**data)
    db.add(emp)
    db.commit()
    db.refresh(emp)
    return emp


def update_emp(data: dict, emp_id: int, db: Session):
    emp = db.query(Employee).filter(Employee.id==emp_id).first()

    for key, value in data.items():
        setattr(emp, key, value)

    db.commit()
    db.refresh(emp)
    return emp


def delete_emp(emp_id: int, db: Session):
    emp = db.query(Employee).filter(Employee.id==emp_id).first()
    if emp is None:
        return False
    db.delete(emp)
    db.commit()
    return True