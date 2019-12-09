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
    # print(text,'\n')
    pattern = r"\[\[Category:(.*?)(?:\|.*?)?\]\]"
    prog = re.compile(pattern)

    #findall
    result = prog.findall(text)
    if result != []:
        for r in result:
            print(r)

    #search
    pattern = r"\[\[Category:(?P<text>.*?)(?:\|.*?)?\]\]"
    prog = re.compile(pattern)
    for line in text.split('\n'):
        result = prog.search(line)
        if result != None:
            print(result.group("text"))

    
