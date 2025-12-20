from fastapi import FastAPI
from routes.employee_route import employee_router
from routes.department_route import department_router
from sql.database import Base,engine


app = FastAPI(

	title : "Employee-Department Management",
	version : "1:0:0"
)

Base.metadata.create_all(bind =engine)

@app.get("/")
def home():
	return {"message": "Welcome to fastapi and postgresql based Employee-Department Management "}
	
	
app.include_router(employee_router)
app.include_router(department_router)
