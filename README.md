# TestingSer


CRUD · FK validation · Delete rules · Clean layering

📌 Problem

Build a REST API to manage Departments and their Employees.

🧱 Models
Department
Field	Type
id	int (PK)
name	string
Employee
Field	Type
id	int (PK)
name	string
role	string
department_id	FK → departments.id
🔁 Relationship

One Department → Many Employees

Use relationship() with back_populates

❌ No cascade delete

🛠️ APIs
Departments
POST   /departments
GET    /departments
PUT    /departments/{id}
DELETE /departments/{id}


📌 Delete rule:


Employees
POST   /employees
GET    /employees
PUT    /employees/{id}
DELETE /employees/{id}

🧠 Rules

1️⃣ Employee requires valid department
2️⃣ Prevent delete if children exist
3️⃣ All checks in service layer
4️⃣ CRUD only DB ops
