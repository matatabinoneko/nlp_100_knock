# import gzip
# import json
# import re

# def extraction(target):
#     with gzip.open("./jawiki-country.json.gz",'rt') as f:
#         for line in f.readlines():
#             json_data = json.loads(line)
#             if json_data["title"] == target:
#                 return json_data["text"]


# text = extraction("イギリス")
# pattern = r'\|(?P<key>.*?) = (?P<value>.*)'
# prog = re.compile(pattern)

# dic = dict((prog.match(line).group("key"),prog.match(line).group("value")) for line in text.split('\n') if prog.match(line)!= None)



# replace_pattern = r"(?P<text>''+.*?''+)"
# replace = re.compile(replace_pattern)
# for key, value in dic.items():
#     text = replace.search(value)
#     if text != None:
#         value = replace.sub(text.group("text").replace("'",''),value)
#     dic[key] = value



# def repl(matchobj):
#     if matchobj.group().find('|') == -1:
#         return matchobj.group().replace('[','').replace(']','')
#     else:
#         pattern = r"\|(?P<text>.*?)\]\]"
#         prog = re.compile(pattern)
#         result = prog.search(matchobj.group())
#         return result.group("text")

# replace_pattern = r"\[\[(?P<text>(?!ファイル:).*?)\]\]"
# replace = re.compile(replace_pattern)
# for key, value in dic.items():
#     value = replace.sub(repl,value)
#     dic[key] = value



# def repl1(matchobj):
#     return ''

# def repl2(matchobj):
#     return matchobj.group("text")

# def repl3(matchobj):
#     return matchobj.group("text")

# pattern1 = r"<.*>"
# pattern2 = r"\{\{.*\|(?P<text>.*?)\}\}"
# pattern3 = r"\[\[ファイル:.*\|(?P<text>.*?)\]\]"
# prog1 = re.compile(pattern1)
# prog2 = re.compile(pattern2)
# prog3 = re.compile(pattern3)
# for key,value in dic.items():
#     value = prog1.sub(repl1,value)
#     value = prog2.sub(repl2,value)
#     value = prog3.sub(repl3,value)
#     dic[key] = value




# import requests

# S = requests.Session()

# URL = "https://en.wikipedia.org/w/api.php"

# PARAMS = {
#     "action": "query",
#     "format": "json",
#     "prop": "imageinfo",
#     "titles": "File:Flag_of_the_United_Kingdom.svg"
# }

# R = S.get(url=URL, params=PARAMS)
# DATA = R.json()

# PAGES = DATA["query"]["pages"]

# for k, v in PAGES.items():
#     print(v["title"] + " is uploaded by User:" + v["imageinfo"][0]["user"])


# def printdict(dic,count):
#     if(type(dic)==dict):
#         for key, value in dic.items():
#             print('\t'*count,key)
#             printdict(value,count+1)
#     else:
#         None

# printdict(DATA,1)



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

    enphasis_pattern = r"('''''|'''|'')(?P<target>.*?)('''''|'''|'')"
    sub = re.compile(enphasis_pattern).sub
    base_info = dict([(key, sub(lambda m:m.group("target"),value)) for key, value in base_info.items()])

    inner_link_pattern = r"\[\[([^\]]*\|)?(?P<link>.*?)\]\]"
    sub = re.compile(inner_link_pattern).sub
    base_info = dict([(key, sub(lambda m:m.group("link"),value)) for key,value in base_info.items()])

    other_markup_pattern = r"\{\{([^\{]*\|)*(?P<text>.*?)\}\}"
    sub = re.compile(other_markup_pattern).sub
    base_info = dict([(key, sub(lambda m:m.group("text"),value)) for key,value in base_info.items()])

    other_markup_pattern = r"(\<.*\>|\[.*\])"
    sub = re.compile(other_markup_pattern).sub
    base_info = dict([(key, sub(lambda m:'',value)) for key,value in base_info.items()])

    for key, value in base_info.items():
        print(key, value)
