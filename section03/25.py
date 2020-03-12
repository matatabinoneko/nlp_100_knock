import gzip
import json
import re



def extraction(target):
    with gzip.open("./jawiki-country.json.gz",'rt') as f:
        for line in f.readlines():
            json_data = json.loads(line)
            if json_data["title"] == target:
                return json_data["text"]


if __name__ == "__main__":
    text = extraction("イギリス")
    pattern = r"\|(?P<key>.*?) = (?P<value>.*)"
    result = re.compile(pattern).search
    base_info = {result(line).group("key"):result(line).group("value") for line in text.split('\n') if result(line) != None}
    
    for key, value in base_info.items():
        print(key, value)
