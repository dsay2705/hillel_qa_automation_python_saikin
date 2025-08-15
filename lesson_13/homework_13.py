import csv
import json
import os
import random
import logging
import xml.etree.ElementTree as ET

console_logger = logging.getLogger('console_logger')
console_logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
console_logger.addHandler(console_handler)

file_logger = logging.getLogger('file_logger')
file_logger.setLevel(logging.ERROR)
file_handler = logging.FileHandler('json__Saikin.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
file_logger.addHandler(file_handler)

#Task_1:

def is_row_included(new_row, existing_rows):
    for exist in existing_rows:
        included = True
        for i, val in enumerate(new_row):
            if val and val != exist[i]:
                included = False
                break
        if included:
            return True
    return False

def no_duplicates_merge_csv(input_files, output_file):
    all_rows = []
    seen_sets = []

    all_headers = []
    for path in input_files:
        if not os.path.exists(path):
            console_logger.error(f"File not found: {path}")
            continue
        try:
            with open(path, 'r', newline='', encoding='utf-8') as csvfile:
                sample = csvfile.read(1024)
                csvfile.seek(0)
                sniffer = csv.Sniffer()
                dialect = sniffer.sniff(sample)
                reader = csv.DictReader(csvfile, dialect=dialect)
                if reader.fieldnames:
                    for h in reader.fieldnames:
                        if h not in all_headers:
                            all_headers.append(h)
        except Exception as e:
            console_logger.error(f"Read file error {path}: {e}")

    if not all_headers:
        console_logger.error("No valid data to write.")
        return

    for path in input_files:
        if not os.path.exists(path):
            continue
        try:
            with open(path, 'r', newline='', encoding='utf-8') as csvfile:
                sample = csvfile.read(1024)
                csvfile.seek(0)
                sniffer = csv.Sniffer()
                dialect = sniffer.sniff(sample)
                reader = csv.DictReader(csvfile, dialect=dialect)
                for row in reader:
                    if not any(row.values()):
                        continue
                    row_tuple = tuple(row.get(h, '') if row.get(h, '') is not None else '' for h in all_headers)
                    row_set = set([v.strip() for v in row_tuple if v is not None and v.strip()])
                    if not any(row_set == s for s in seen_sets) and not is_row_included(row_tuple, all_rows):
                        all_rows.append(row_tuple)
                        seen_sets.append(row_set)
        except Exception as e:
            console_logger.error(f"Read file error {path}: {e}")

    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(all_headers)
            for row_tuple in all_rows:
                writer.writerow(row_tuple)
    except Exception as e:
        console_logger.error(f"Write file error {output_file}: {e}")

def get_two_random_files(folder_name, file_type):
    folder_path = os.path.join(os.path.dirname(__file__), folder_name)
    all_files = [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.endswith(file_type) and os.path.isfile(os.path.join(folder_path, f))
    ]
    result_files = random.sample(all_files, 2)
    print(result_files)
    return result_files


csv_files = get_two_random_files('work_with_csv', '.csv')

#uncommit to run Task 1:
#no_duplicates_merge_csv(csv_files, 'result_Saikin.csv')

#Task_2:

def validate_json_files(folder_name):
    folder_path = os.path.join(os.path.dirname(__file__), folder_name)
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    json.load(f)
                console_logger.info(f"{filename}: valid JSON")
            except Exception as e:
                console_logger.info(f"{filename}: invalid JSON")
                file_logger.error(f"Invalid JSON file: {file_path} | Error: {e}")

#uncommit to run Task 2:
#validate_json_files('work_with_json')

#Task_3:

def find_incoming_by_group_number(xml_path, group_number):
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        for group in root.findall('group'):
            number = group.find('number')
            if number is not None and number.text == str(group_number):
                timing = group.find('timingExbytes')
                if timing is not None:
                    incoming = timing.find('incoming')
                    if incoming is not None:
                        console_logger.info(f"group/number={group_number}: incoming={incoming.text}")
                        return incoming.text
        console_logger.info(f"group/number={group_number}: not found")
        return None
    except Exception as e:
        console_logger.error(f"XML read error: {e}")
        return None

xml_file_path = os.path.join(os.path.dirname(__file__), 'work_with_xml', 'groups.xml')

#uncommit to run Task 3:
#find_incoming_by_group_number(xml_file_path, '2')