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
# new_dic = dict()
# for key, value in dic.items():
#     text = replace.search(value)
#     if text != None:

#         value = replace.sub(text.group("text").replace("'",''),value)
#     new_dic[key] = value

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
# for key, value in new_dic.items():
#     value = replace.sub(repl,value)
#     new_dic[key] = value



# for key,value in new_dic.items():
#     print(key,value,sep=' : ')



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


    for key, value in base_info.items():
        print(key, value)
