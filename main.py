# Example of reading an external JSON file into a Python Dictionary
import json
import sys


def import_employees_from_json_file(filename: str) -> dict:
    with open(filename) as f:
        data: dict = json.load(f)
    return data


def echo_employees(employees: dict) -> None:
    # print header row
    print(f'{"ID":>4} {"Last":<15}{"First":<10}{"Dept"}')

    # print detail rows
    for employee in employees['employees']:
        employee_id = int(employee['id'])
        # print with fixed column widths in a form
        # that allows moving things around, thus the extra pair of parens
        field_layout = (
                f"{employee_id:>4} "
                f"{employee['lastName']:<15}"
                f"{employee['firstName']:<10}"                
                f"{employee['department']}"
            )
        print(field_layout)


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'

def set_employee_id(employees: dict, old_id:str, new_id: str):
    # locate the employee by its existing employee ID value
    all_emps = employees['employees']
    print(f'type(all_emps)={type(all_emps)}')
    # one_emp = all_emps[0]
    # print(f'type(d)={type(one_emp)}')
    filtered = filter(lambda item: item['id'] == old_id, all_emps)
    emp_list = list(filtered)
    emp = dict(emp_list[0])
    print(f'type(emp)={type(emp)}')
    #FAILS: emp = filter(lambda d: dict[d]['id'] == old_id)
    #FAILS emp = dict((k,v) for (k, v) in d.iteritems() if k== 'id' and v == old_id)
    if emp is not None:
        print('found')
        print(f'Old ID: {emp['id']}')




if __name__ == '__main__':
    print(f'Python version {get_python_version()}')
    filename = 'employees.json'
    employees_dictionary = import_employees_from_json_file(filename)
    echo_employees(employees_dictionary)
    set_employee_id(employees_dictionary, '04','03')
    print('done')
