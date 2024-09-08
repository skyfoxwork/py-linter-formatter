def format_linter_error(error: dict) -> dict:
    return {
        ("name" if key == "code" else "source" if key == "filename" else
         "message" if key == "text" else tuple(key.split("_"))[0]):
        ("flake8" if key == "filename" else value)
        for key, value in error.items() if key != "physical_line"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    # write your code here
    pass


def format_linter_report(linter_report: dict) -> list:
    # write your code here
    pass


error = {
    "code": "E501",
    "filename": "./source_code_2.py",
    "line_number": 18,
    "column_number": 80,
    "text": "line too long (99 > 79 characters)",
    "physical_line": '    return f"I like to filter, rounding, doubling, '
    "store and decorate numbers: {', '.join(items)}!\"",
}

print(format_linter_error(error=error))
# # The output will be:
# {
#     "line": 18,
#     "column": 80,
#     "message": "line too long (99 > 79 characters)",
#     "name": "E501",
#     "source": "flake8"
# }
