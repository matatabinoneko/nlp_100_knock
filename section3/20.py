import gzip
import json



def extraction(target):
    with gzip.open("./jawiki-country.json.gz",'rt') as f:
        for line in f.readlines():
            json_data = json.loads(line)
            if json_data["title"] == target:
                print(json_data["text"])
                break
            

if __name__ == "__main__":
    extraction("イギリス")
    # with gzip.open("./jawiki-country.json.gz",'rt') as f:
        # for line in f.readlines():
        #     json_data = json.loads(line)
        #     print(json_data.keys(),json_data["title"])