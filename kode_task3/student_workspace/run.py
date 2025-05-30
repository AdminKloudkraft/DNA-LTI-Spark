import importlib.util
import os

# Ensure report.txt file exists for legacy compatibility
report_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "report.txt"))
if not os.path.exists(report_path):
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("")

# Load driver.py from ../secret_tests/
driver_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "secret_tests", "driver.py"))
if not os.path.exists(driver_path):
    raise FileNotFoundError(f"Driver file not found at {driver_path}")

# Load solution.py path to pass to driver
solution_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "solution.py"))

# Dynamically import and run driver.py
spec = importlib.util.spec_from_file_location("driver", driver_path)
driver_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(driver_module)

if __name__ == "__main__":
    driver_module.test_student_code(solution_path)
