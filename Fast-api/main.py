from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

class Input(BaseModel):
    numbers: list[int]
    threshold: int = Field(0, ge=0)


def process_data(nums: list[int], threshold: int):
    # Case 1: Empty Input list
    if not nums:
        return {
            "sum": 0,
            "average": 0,
            "filtered": [],
            "outlier": [],
            "max": None,
            "min": None,
            "count": None
        }
    
    # Case 2: Non-empty Input List
    total = sum(nums)
    average = total/len(nums)
    max_val = max(nums)
    min_val = min(nums)
    count = len(nums)

    # filtered = []
    # outliers = []
    # for i in range(len(nums)):
    #     if (0 < nums[i] <= threshold):
    #         filtered.append(nums[i])
    #     if(nums[i] > threshold or nums[i] < 0):
    #         outliers.append(nums[i])

    filtered = [n for n in nums if 0 < n <= threshold]
    outliers = [n for n in nums if n > threshold or n < 0]

    response = {
        "sum": total,
        "average": average,
        "filtered": filtered,
        "outlier": outliers,
        "max": max_val,
        "min": min_val,
        "count": count      
    }
    return response

@app.get("/")
def root():
    return {"message": "Hello"}

@app.post("/process-data")
def process_data_api(data: Input):
    nums = data.numbers
    threshold = data.threshold

    # Validation
    if threshold < 0:
        raise HTTPException(status_code=400, detail="Threshold must be >= 0")

    return process_data(nums, threshold)
