import gzip
import json
import re



# with open("./jawiki-country.json") as f:
#     jsonData = json.load(f)

    # print(jsonData)
def extraction(target):
    with gzip.open("./jawiki-country.json.gz",'rt') as f:
        for line in f.readlines():
            json_data = json.loads(line)
            if json_data["title"] == target:
                return json_data["text"]


text = extraction("イギリス")
pattern = r'\|(?P<key>.*?) = (?P<value>.*)'
prog = re.compile(pattern)
# for line in text.split('\n'):
#     result = prog.match(line)
#     if(result!=None):
#         dic[result.group("key")] = result.group("value")
dic = dict((prog.match(line).group("key"),prog.match(line).group("value")) for line in text.split('\n') if prog.match(line)!= None)
# for key, value in dic.items():
#     print(key,value,sep=' : ')
# print()



replace_pattern = r"(?P<text>''+.*?''+)"
replace = re.compile(replace_pattern)
for key, value in dic.items():
    text = replace.search(value)
    if text != None:
        # print(text.group("text"))
        # print(value)
        value = replace.sub(text.group("text").replace("'",''),value)
        # print(value)
    dic[key] = value

# for key,value in dic.items():
#     print(key,value,sep=' : ')
# print()


def repl(matchobj):
    if matchobj.group().find('|') == -1:
        return matchobj.group().replace('[','').replace(']','')
    else:
        pattern = r"\|(?P<text>.*?)\]\]"
        prog = re.compile(pattern)
        result = prog.search(matchobj.group())
        return result.group("text")

replace_pattern = r"\[\[(?P<text>(?!ファイル:).*?)\]\]"
replace = re.compile(replace_pattern)
for key, value in dic.items():
    value = replace.sub(repl,value)
    dic[key] = value



def repl1(matchobj):
    return ''

def repl2(matchobj):
    return matchobj.group("text")

def repl3(matchobj):
    return matchobj.group("text")

pattern1 = r"<.*>"
pattern2 = r"\{\{.*\|(?P<text>.*?)\}\}"
pattern3 = r"\[\[ファイル:.*\|(?P<text>.*?)\]\]"
prog1 = re.compile(pattern1)
prog2 = re.compile(pattern2)
prog3 = re.compile(pattern3)
for key,value in dic.items():
    value = prog1.sub(repl1,value)
    value = prog2.sub(repl2,value)
    value = prog3.sub(repl3,value)
    dic[key] = value

# for key,value in dic.items():
#     print(key,value,sep=' : ')





import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "titles": "File:Flag_of_the_United_Kingdom.svg"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA["query"]["pages"]

for k, v in PAGES.items():
    print(v["title"] + " is uploaded by User:" + v["imageinfo"][0]["user"])


def printdict(dic,count):
    if(type(dic)==dict):
        for key, value in dic.items():
            print('\t'*count,key)
            printdict(value,count+1)
    elif type(dic) == list:
        for a in dic:
            printdict(a,count)
    else:
        print(dic)

printdict(DATA,1)
print(DATA["query"]["pages"]["23473560"]["pageid"]["imageinfo"]["user"])

