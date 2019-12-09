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
    base_info = dict([(result(line).group("key"),result(line).group("value")) for line in text.split('\n') if result(line) != None])
    pattern = r"('''''|'''|'')(?P<target>.*?)('''''|'''|'')"
    sub = re.compile(pattern).sub
    
    base_info = dict([(key, sub(lambda m:m.group("target"),value)) for key, value in base_info.items()])
    for key, value in base_info.items():
        print(key, value)
