from fastapi import FastAPI, HTTPException

app = FastAPI()

employees = [
    {"id": 1, "name": "John", "department": "IT"},
    {"id": 2, "name": "Alice", "department": "HR"}
]


@app.get("/")
def home():
    return {"message": "Employee Management API is running"}


@app.get("/employees")
def get_employees():
    return employees


@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    for emp in employees:
        if emp["id"] == employee_id:
            return emp

    raise HTTPException(status_code=404, detail="Employee not found")


@app.post("/employees")
def create_employee(employee: dict):
    employees.append(employee)
    return {
        "message": "Employee added",
        "employee": employee
    }


@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, updated_employee: dict):
    for index, emp in enumerate(employees):
        if emp["id"] == employee_id:
            employees[index] = updated_employee
            return {"message": "Employee updated"}

    raise HTTPException(status_code=404, detail="Employee not found")


@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    for emp in employees:
        if emp.get("id") == employee_id:
            employees.remove(emp)
            return {"message": "Employee deleted"}

    raise HTTPException(status_code=404, detail="Employee not found")