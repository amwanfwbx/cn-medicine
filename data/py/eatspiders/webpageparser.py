from pymongo import MongoClient
from bs4 import BeautifulSoup
import time

db = MongoClient('localhost', 27017).eat
batch_no = 201910141402


def main():
    docs = db["ori_webpageinfo"].find({"batch_no": {"$ne": batch_no}, "spidername": "ZYSJ_FangJi_Spider"})
    for doc in docs:
        soup = BeautifulSoup(doc['data'], features="lxml")
        # 原料_MSJ
        if doc['url'].endswith('useful/') and db["material_info"].find_one({"refid": doc['_id']}) is None:
            name = soup.title.string[0:soup.title.string.find('的营养')]
            pdoc = {"title": soup.title.string, "name": name, "url": doc['url'], "refid": doc['_id'], "creattime": time.time(), "parse_no": batch_no, "nutrition": []}
            curtitle = ''
            for p in soup.select('.wrap .space_left p'):
                if p.strong:
                    curtitle = parse_key(p.strong.text)
                elif pdoc.get(curtitle):
                         pdoc[curtitle] = pdoc[curtitle]+p.text
                else:
                        pdoc[curtitle] = p.text
            #成份
            for n in soup.select('.wrap .space_right .category_use_table li'):
                item = n.text.split()
                if len(item) == 3:
                    pdoc["nutrition"].append({"name": item[0], "val": item[1], "unit": item[2]})
            db["material_info"].insert_one(pdoc)

            upd_status = {"$set": {"batch_no": batch_no, "last_parsetime":  time.time()}}
            db["ori_webpageinfo"].update(doc, upd_status)

        if doc['spidername'] == 'zysj_zhongyao_spider' and db["yaocai_info"].find_one({"refid": doc['_id']}) is None:
            if soup.title and soup.title.string.find('_中药材')>=0:
                contentbox = soup.select('#content')[0];
                # name = contentbox.find("h1").string
                pdoc = {"title": soup.title.string,  "url": doc['url'], "refid": doc['_id'], "creattime": time.time(), "parse_no": batch_no, "recodes": []}
                curRecode = {}
                curkey = None
                for child in contentbox.children:
                    if child.name == 'h1':
                        pdoc["name"] = child.string
                    if child.name == 'h2':
                        if 'refbook' in curRecode:
                            pdoc['recodes'].append(curRecode)
                            curRecode = {}
                    if child.name == 'p':
                        if 'class' in child.attrs:
                            if 'drug' in child.attrs['class']:
                                curkey = child.attrs['class'][1]
                                child.select(".fieldname")[0].clear()
                                if curkey == 'tp':
                                    pdoc['img'] = child.find("img").attrs['data-popbigimg']
                                else:
                                    curRecode[parse_zysj_key(curkey)] = child.text
                            else:
                                print("#WARNNING 异常段落 ：\n")
                                print(child)
                        else:
                            curRecode[parse_zysj_key(curkey)] = curRecode[parse_zysj_key(curkey)] + '\n' + child.text
                if curRecode not in pdoc['recodes']:
                    pdoc['recodes'].append(curRecode)

                db["yaocai_info"].insert_one(pdoc)
                upd_status = {"$set": {"batch_no": batch_no, "last_parsetime": time.time()}}
                db["ori_webpageinfo"].update(doc, upd_status)

        if doc['spidername'] == 'ZYSJ_FangJi_Spider' and db["yaofang_info"].find_one({"refid": doc['_id']}) is None:
            if soup.title and soup.title.string.find('_中药方剂') >= 0:
                contentbox = soup.select('#content')[0];
                pdoc = {"title": soup.title.string, "url": doc['url'], "refid": doc['_id'], "creattime": time.time(),
                        "parse_no": batch_no}
                curkey = None
                name = None
                for child in contentbox.children:
                    if child.name == 'h1':
                        name = child.string
                        pdoc["name"] =name
                    if child.name == 'h2':
                        if 'refbook' in pdoc:  # 第二本，存第一本
                            db["yaofang_info"].insert_one(pdoc)
                            pdoc = {"title": soup.title.string, "url": doc['url'], "refid": doc['_id'], "creattime": time.time(), "parse_no": batch_no, "name": name}
                    if child.name == 'p':
                        if 'class' in child.attrs:
                            if 'drug' in child.attrs['class']:
                                curkey = child.attrs['class'][1]
                                child.select(".fieldname")[0].clear()
                                pdoc[parse_zysj_key(curkey)] = child.text
                            else:
                                print("#WARNNING 异常段落 ：\n")
                                print(child)
                        else:
                            pdoc[parse_zysj_key(curkey)] = pdoc[parse_zysj_key(curkey)] + '\n' + child.text
                #最后一本，只有一本时的第一本
                db["yaofang_info"].insert_one(pdoc)
                upd_status = {"$set": {"batch_no": batch_no, "last_parsetime": time.time()}}
                db["ori_webpageinfo"].update(doc, upd_status)

def parse_key(title):
    return {
        '食材简介': 'intro',
        '营养价值': 'nutritional',
        '食用功效': 'function',
        '适用人群': 'fit_for',
        '禁忌人群': 'avoid_for',
        '选购技巧': 'how_buy',
        '存储简述': 'store',
        '其它相关说明': 'appendix'
    }.get(title, title)
def parse_zysj_key(ky):
    return {
        'py': 'pinyin',
        'ywm': 'enname',
        'bm': 'alias',
        'cc': 'ref',
        'ly': 'birth',
        'yxt': 'model',
        'sjfb': 'place',
        'xz': 'character',
        'gnzz': 'function',
        'yfyl': 'usemethod',
        'gjls': 'appendix',
        'zl': 'refbook',
        'xw': 'xinwei',
        'ff': 'usewith',
        'zy': 'attention',
        'hxcf': 'chemial',
        'dx': 'by-effect',
        'jb': 'recognize',
        'pz': 'produce',
        'gj': 'guijin',
        'zc': 'store',
        'lcyy': 'applyfor',
        'bz': 'memo',
        'cf': 'construction',
        'zf': 'produce'
    }.get(ky, ky)
if __name__ == "__main__":
    # execute only if run as a script
    main()

