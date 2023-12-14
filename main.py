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


if __name__ == '__main__':
    print(f'Python version {get_python_version()}')
    filename = 'employees.json'
    employees_dictionary = import_employees_from_json_file(filename)
    echo_employees(employees_dictionary)
