from pymongo import MongoClient
import time
import re

db = MongoClient('localhost', 27017).eat
batch_no = 201910141402


def main():
    line = 0
    docs = db["yaocai_info"].find({})

    for doc in docs:
        # 药材_刷名字
        line = line+1
        print(line, doc['name'], doc['_id'])
        if 'recodes' in doc:
            names = [doc['name']]
            for rec in doc['recodes']:
                if 'alias' in rec:
                    alias_str = rec['alias']
                    print(alias_str)
                    alias_arr = None
                    if alias_str.find('，') > 0:
                        alias_arr = alias_str.split('，')
                    elif alias_str.find('，') > 0:
                        alias_arr = alias_str.split('，')
                    elif alias_str.find('、') > 0:
                        alias_arr = alias_str.split('、')
                    elif alias_str.find(',') > 0:
                        alias_arr = alias_str.split(',')
                    elif alias_str.find(' ') > 0:
                        alias_arr = alias_str.split(' ')
                    elif len(alias_str) < 5:
                        alias_arr = [alias_str]
                    else:
                        alias_arr = [alias_str]
                        print("####可能有误#####", alias_str)
                    for n in alias_arr:
                        #清格式
                        n = re.sub(r'（.*）', "", n)
                        n = re.sub(r'《.*》', "", n)
                        n = n.replace('。', "")
                        n = n.replace('。', "")
                        n = n.replace(' ', "")
                        if n not in names:
                            names.append(n)
            #刷名字
            print(names)
            upd_status = {"$set": {"names": names, "updtime": time.time()}}
            db["yaocai_info"].update_one(doc, upd_status)


if __name__ == "__main__":
    # execute only if run as a script
    main()

