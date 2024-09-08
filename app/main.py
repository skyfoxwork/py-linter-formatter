def format_linter_error(error: dict) -> dict:
    return {
        ("name" if key == "code" else "source" if key == "filename" else
         "message" if key == "text" else tuple(key.split("_"))[0]):
        ("flake8" if key == "filename" else value)
        for key, value in error.items() if key != "physical_line"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {("errors" if i == "error" else i) : ([format_linter_error(error) for error in errors] if i == "error" else file_path if i == "path" else "failed" if i == "status" else "")for i in ("error", "path", "status")}


def format_linter_report(linter_report: dict) -> list:
    # write your code here
    return None


errors = [
    {
        "code": "E501",
        "filename": "./source_code_2.py",
        "line_number": 18,
        "column_number": 80,
        "text": "line too long (99 > 79 characters)",
        "physical_line": '    return f"I like to filter, rounding, doubling, '
        "store and decorate numbers: {', '.join(items)}!\"",
    },
    {
        "code": "W292",
        "filename": "./source_code_2.py",
        "line_number": 18,
        "column_number": 100,
        "text": "no newline at end of file",
        "physical_line": '    return f"I like to filter, rounding, doubling, '
        "store and decorate numbers: {', '.join(items)}!\"",
    },
]

print(format_single_linter_file(file_path="./source_code_2.py", errors=errors))
