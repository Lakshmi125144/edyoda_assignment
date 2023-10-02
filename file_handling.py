import json 

class Employee: 
    def __init__(self, name, dob, height, city, state): 
        self.name = name 
        self.dob = dob 
        self.height = height 
        self.city = city 
        self.state = state 
    def read_employees_from_json(file_path): 
        with open(file_path, "r") as f: 
            employee_data = json.load(f) 
        employees = [] 
        for employee in employee_data: 
            employee_obj = Employee(employee["name"], employee["dob"], employee["height"], employee["city"], employee["state"]) 
            employees.append(employee_obj) 
        return employees 
    def print_employees(employees): 
        for employee in employees: 
            print(f"Name: {employee.name}") 
            print(f"DOB: {employee.dob}") 
            print(f"Height: {employee.height}") 
            print(f"City: {employee.city}") 
            print(f"State: {employee.state}") 
    def create_states_json(states): 
        with open("states.json", "w") as f: 
            json.dump(states, f) 
    if __name__ == "__main__": 
        # Assignment 1a
        file_path = "employee.json" 
        employees = read_employees_from_json(file_path) 
        
        print_employees(employees) 
        # Assignment 1b 
        states = { 
            "Andhra Pradesh": "Amaravati", 
            "Karnataka": "Bangalore", 
            "Kerala": "Thiruvananthapuram", 
            "Tamil Nadu": "Chennai", 
            "Maharashtra": "Mumbai", 
            "Uttar Pradesh": "Lucknow", 
            "West Bengal": "Kolkata" 
        } 
        create_states_json(states)
