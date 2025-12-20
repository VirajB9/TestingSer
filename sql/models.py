from sqlalachemy import Column,ForeignKey,Integer,String
from sqlalchemy.orm import relationship
from sql.database import Base

class Department(Base):

	__tablename__ = "Department" 
	
	id = Column(Integer,primary_key = True, index = True)\
	name = Column(String,nullable = False)
	
	employee = relationship("Employee", back_populates = "department")
	
class Employee(Base):

	__tablename__ = "Employee"
	
	id = Column(Integer,primary_key=True,index=True)
	name = Column(String,nullable=False)
	role = Column(String,nullable=False)
	department_id = Column(Integer,ForeignKey(Department.id),nullable=False)
	
	department = relationship("Department",back_populates = "employee")
