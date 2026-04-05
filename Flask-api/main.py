from flask import Flask, request
from typing import List

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Hello"}

def process_data (nums, threshold):
    if not nums:
        return {
            "sum": 0,
            "average": 0,
            "filtered": [],
            "outliers": [],
            "max": None,
            "min": None,
            "count": 0
        }
    total = sum(nums)
    count  = len(nums)
    average = total / count
    max_val = max(nums)
    min_val = min(nums)
    filtered = [ n for n in nums if 0 < n <= threshold ]
    outliers = [ n for n in nums if n < 0 or n > threshold]

    response = {
        "sum": total,
        "average": average,
        "filtered": filtered,
        "outliers": outliers,
        "max": max_val,
        "min": min_val,
        "count": count
    }
    return response

@app.route("/process-data", methods=["POST"])
def process_data_api():
    data = request.get_json()

    # Validation
    if not data:
        return {"error": "Invalid JSON"}, 400

    if "numbers" not in data or "threshold" not in data:
        return {"error": "Missing fields"}, 400

    nums = data["numbers"]
    threshold = data["threshold"]

    if not isinstance(nums, list):
        return {"error": "numbers must be list"}, 400

    if not isinstance(threshold, int) or threshold < 0:
        return {"error": "threshold must be >= 0"}, 400

    result = process_data(nums, threshold)

    return result


if __name__ == "__main__":
    app.run(debug=True) 

