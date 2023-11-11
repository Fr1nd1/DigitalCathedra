import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
indent = 4

def task() -> None:
    with open(INPUT_FILENAME, "r", encoding='utf-8') as file_input:
        data_csv = csv.DictReader(file_input)

        # Конвертация данных в список словарей
        data = [row for row in data_csv]

    with open(OUTPUT_FILENAME, "w", encoding='utf-8') as file_output:
        data_json = json.dumps(data, indent=indent)
        file_output.write(data_json)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
