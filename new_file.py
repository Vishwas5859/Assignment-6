Employees = {'Employee':{'employee1':{"name":"Mike","DOB":"12-01-1985","height":"1.3m","city":"Hydrabad",
"state": "Telangana"},'employee2':{"name":"Raj","DOB":"22-03-1985","height":"1.6m","city":"Bangalore",
"state": "Karnataka"},'employee3':{"name":"Suraj","DOB":"16-02-1985", "height":"1.55m","city":"Cochi",
"state": "Kerala"},'employee4':{"name":"Anmol","DOB":"28-07-1985","height":"1.75m","city":"Kolkata",
"state": "West Bengal"},'employee5':{"name":"Randeep","DOB":"17-04-1985","height":"1.64m","city":"Ahmedabad",
"state": "Gujarat" }}}

import json
json_obj = json.dumps(Employees,indent=5)
print(json_obj)
