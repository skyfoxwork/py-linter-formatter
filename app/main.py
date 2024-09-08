def format_linter_error(error: dict) -> dict:
    return {
        ("name" if key == "code" else "source" if key == "filename" else
         "message" if key == "text" else tuple(key.split("_"))[0]):
        ("flake8" if key == "filename" else value)
        for key, value in error.items() if key != "physical_line"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        ("errors" if elem == "error" else elem):
        ([format_linter_error(error) for error in errors]
         if elem == "error" else file_path if elem == "path" else
         "failed" if elem == "status" else "")
        for elem in ("error", "path", "status")
    }


def format_linter_report(linter_report: dict) -> list:
    # write your code here
    return None
