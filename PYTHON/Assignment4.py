class department:
    def __init__(self,deptid,deptname,loc,depthod): 
        self.deptid=deptid
        self.deptname =deptname    
        self.loc=loc
        self.depthod = depthod
    def display_dept_info(self):
        print(f"Department information:")
        print("-----------------------")
        print(f"DeptId: {self.deptid}")
        print(f"DeptName: {self.deptname}")
        print(f"location: {self.loc}")
        print(f"depthod: {self.depthod}")
        
def dept_info():
    dept_count = int(input("Enter the number of department"))
    dept_list = []
    for i in range(0,dept_count):
         deptid = int(input())
         deptname = input()
         loc = input()
         depthod = input()
         dept = department(deptid,deptname,loc,depthod)
         dept_list.append(dept)
    return dept_list
    
dept1 = dept_info()
for i in  dept1:
    i.display_dept_info()

search = int(input("Enter Department ID to search: "))
flag = False
for dept in dept1:
    if dept.deptid == search:
        print("Department found:")
        dept.display_dept_info()
        flag= True
        break
if not flag:
    print("Department ID not found.")

## we are searching by Department name 
search_name = input("\nEnter Department Name to search: ")
flag = False
for dept in dept1:
    if dept.deptname== search_name:
        print("Department found:")
        dept.display_dept_info()
        flag = True
        break
if not flag:
    print("Department Name not found.")

