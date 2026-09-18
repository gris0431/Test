import sys
import json

def load_json(path: str):
    with open(path, 'r', encoding='utf-16') as f: #ИСПОЛЬЗУЙТЕ JSON В КОДИРОВКЕ UTF-16
        return json.load(f)

def fill_values(node, value_map: dict):
    if isinstance(node, dict):
        if 'id' in node and 'value' in node:
            node_id = node['id']
            if node_id in value_map:
                node['value'] = value_map[node_id]
        for key, val in node.items():
            if isinstance(val, (dict, list)):
                fill_values(val, value_map)
    elif isinstance(node, list):
        for item in node:
            fill_values(item, value_map)

def main():
    if len(sys.argv) != 4:
        print("Пример: python task3.py values.json tests.json report.json")
        print("ИСПОЛЬЗУЙТЕ JSON В КОДИРОВКЕ UTF-16") #(я ж из ворда брал)
    else:
        values_path, tests_path, report_path = sys.argv[1:4]
        values_data = load_json(values_path)
        tests_data = load_json(tests_path)
        value_map = {}
        for item in values_data.get('values', []):
            value_map[item['id']] = item['value']
        fill_values(tests_data, value_map)

        with open(report_path, 'w', encoding='utf-16') as f: #ИСПОЛЬЗУЙТЕ JSON В КОДИРОВКЕ UTF-16
            json.dump(tests_data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
