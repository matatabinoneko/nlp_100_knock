import gzip
import json
import re


def extraction(target):
    with gzip.open("./jawiki-country.json.gz",'rt') as f:
        for line in f.readlines():
            json_data = json.loads(line)
            if json_data["title"] == target:
                return json_data["text"]





# category = re.findall(r'\[\[Category:(.*?)(?:\|.*)?\]\]',text)
# print(category)

if __name__ == "__main__":
    text = extraction("イギリス")
    print(text,'\n')
    pattern = r"\[\[Category:.*?\]\]"
    prog = re.compile(pattern)
    result = prog.findall(text)
    if result != []:
        for r in result:
            print(r)

