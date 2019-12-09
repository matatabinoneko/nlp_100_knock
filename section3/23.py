import gzip
import json
import re



def extraction(target):
    with gzip.open("./jawiki-country.json.gz",'rt') as f:
        for line in f.readlines():
            json_data = json.loads(line)
            if json_data["title"] == target:
                return json_data["text"]




# pattern = r'(?P<level>=+)(?P<section>.*?)=+'
# # pattern = r'={3}(.*?)={3}'
# prog = re.compile(pattern)
# for line in text.split('\n'):
#     result = prog.match(line)
#     if(result!=None):
#         print(len(result.group("level")),result.group("section"))
    
if __name__ == "__main__":
    text = extraction("イギリス")
    pattern = r"=(?P<level>=+) *?(?P<section>.*?) *?="
    prog = re.compile(pattern)
    for line in text.split('\n'):
        result = prog.search(line)
        if result != None:
            print("level={}, section={}".format(len(result.group("level")), result.group("section")))

    