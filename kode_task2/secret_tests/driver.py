import importlib.util
import os
import numpy as np

def test_student_code(solution_path):
    # Dynamically load solution.py
    spec = importlib.util.spec_from_file_location("solution", solution_path)
    student_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(student_module)

    results = []
    results.append("🧪 Running Independent Tests for: ExamScoreAnalyzer\n")

    # Test 1: __init__ + load_scores
    try:
        tracker = student_module.ExamScoreAnalyzer()
        arr = tracker.load_scores([50, 90, 30, 75])
        if isinstance(arr, np.ndarray) and np.array_equal(arr, np.array([50, 90, 30, 75])):
            results.append("✅ Test 1 Passed: load_scores stores scores correctly")
        else:
            results.append("❌ Test 1 Failed: load_scores did not return correct array")
    except Exception as e:
        results.append(f"❌ Test 1 Failed: load_scores raised error: {e}")

    # Test 2: compute_summary independently
    try:
        tracker = student_module.ExamScoreAnalyzer()
        tracker.load_scores([70, 80, 90])
        summary = tracker.compute_summary()
        if summary == "Average: 80.0, Max: 90, Min: 70":
            results.append("✅ Test 2 Passed: compute_summary works correctly")
        else:
            results.append("❌ Test 2 Failed: compute_summary output incorrect")
    except Exception as e:
        results.append(f"❌ Test 2 Failed: compute_summary raised error: {e}")

    # Test 3: get_passing_scores independently
    try:
        tracker = student_module.ExamScoreAnalyzer()
        tracker.load_scores([25, 40, 55, 90])
        passed = tracker.get_passing_scores()
        if isinstance(passed, np.ndarray) and np.array_equal(passed, np.array([40, 55, 90])):
            results.append("✅ Test 3 Passed: get_passing_scores filters correctly")
        else:
            results.append("❌ Test 3 Failed: get_passing_scores output incorrect")
    except Exception as e:
        results.append(f"❌ Test 3 Failed: get_passing_scores raised error: {e}")

    # Test 4: assign_grades independently
    try:
        tracker = student_module.ExamScoreAnalyzer()
        tracker.load_scores([95, 78, 61, 43, 20])
        grades = tracker.assign_grades()
        expected = ['A', 'B', 'C', 'D', 'F']
        if grades == expected:
            results.append("✅ Test 4 Passed: assign_grades assigns correct grades")
        else:
            results.append("❌ Test 4 Failed: assign_grades returned incorrect grades")
    except Exception as e:
        results.append(f"❌ Test 4 Failed: assign_grades raised error: {e}")

    # Hidden test: empty list summary
    try:
        tracker = student_module.ExamScoreAnalyzer()
        tracker.load_scores([])
        result = tracker.compute_summary()
        if result == "Average: 0.0, Max: 0, Min: 0":
            results.append("✅ Hidden Test Passed: compute_summary handles empty input")
        else:
            results.append("❌ Hidden Test Failed: compute_summary wrong for empty input")
    except Exception as e:
        results.append(f"❌ Hidden Test Failed: compute_summary raised error on empty input: {e}")

    # REPORTING: Save to /reports/report_N.txt (incremental)
    report_folder = os.path.join(os.path.dirname(solution_path), "..", "reports")
    os.makedirs(report_folder, exist_ok=True)
    existing = [f for f in os.listdir(report_folder) if f.startswith("report") and f.endswith(".txt")]
    report_filename = f"report_{len(existing)+1}.txt"
    report_path = os.path.join(report_folder, report_filename)

    with open(report_path, "w", encoding="utf-8") as f:
        for line in results:
            print(line)
            f.write(line + "\n")
