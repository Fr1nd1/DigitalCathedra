import json
INPUT_FILE = 'input.json'

def task() -> float:
    with open(INPUT_FILE, "r") as json_data_file:
        json_data = json.load(json_data_file)

    sum_mult = sum([item["score"]*item["weight"] for item in json_data])

    return round(sum_mult, 3)

print(task())
