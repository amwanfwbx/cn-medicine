from pymongo import MongoClient
from py2neo import *


db = MongoClient('localhost', 27017).eat
graph = Graph('neo4j+s://155a58b3.databases.neo4j.io',  auth=('neo4j', 'lw7e9QV-1HtQDWxo9E93H0GbK6wK7eBqCoEqLeF_xhA'))

guijin_arr = ["心", "肝", "脾", "肺", "肾", "胆", "胃", "小肠", "大肠", "膀胱", "三焦"]
xin_arr = ["寒", "热", "温", "凉", "平"]
wei_arr = ["辛", "甘", "酸", "苦", "咸", "淡", "涩"]
batch_no = 201910141402


##############
# (:YaoCai){name: ,names:}
# (:YaoCai)-[:REF]->(:Record)
# (:YaoCai)-[:GUIJIN]->(:ZangFu)
# ((:YaoCai)-[:GUIJIN]->(:YaoFang)
##############
def main():
    init()
    line = 0
    docs = db['zy_yaocai'].find({})

    REF = Relationship.type("REF")
    GUIJIN = Relationship.type("GUIJIN")
    XIN = Relationship.type("XIN")
    WEI = Relationship.type("WEI")

    zfmather = NodeMatcher(graph)
    zangfu_nodes = zfmather.match("ZangFu").all()
    xin_nodes = zfmather.match("Xin").all()
    wei_nodes = zfmather.match("Wei").all()
    for doc in docs:
        # 药材_刷名字
        line = line+1


        # 去重
        if not zfmather.match("YaoCai", name=doc['name']).exists():
            # 药结点
            yaocai_node = Node("YaoCai", name=doc['name'], names=doc['names'])
            tx = graph.begin()
            if 'recodes' in doc:
                for rec in doc['recodes']:
                    record_node = Node("Record")
                    for attr in rec:
                        record_node[attr] = rec[attr]
                    ref = REF(yaocai_node, record_node)
                    ref["bookname"] = rec['refbook']
                    tx.create(ref)
                    if 'guijin' in rec:
                        for zangfu in zangfu_nodes:
                            if rec['guijin'].find(zangfu['name']) >= 0:
                                gj = GUIJIN(yaocai_node, zangfu)
                                tx.create(gj)
                    if 'xinwei' in rec:
                        for xin in xin_nodes:
                            if rec['xinwei'].find(xin['name']) >= 0:
                                r_xin = XIN(yaocai_node, xin)
                                tx.create(r_xin)
                        for wei in wei_nodes:
                            if rec['xinwei'].find(wei['name']) >= 0:
                                r_wei = WEI(yaocai_node, wei)
                                tx.create(r_wei)
            tx.commit()
            print(line, doc['name'], doc['_id'])

def init():
    # 脏腑
    nm = NodeMatcher(graph)
    zfs = nm.match("ZangFu")
    if(zfs.count() == 0):
    # if True:
        for zfname in guijin_arr:
            node = Node("ZangFu", name=zfname)
            graph.create(node)
        for xin in xin_arr:
            node = Node("Xin", name=xin)
            graph.create(node)
        for wei in wei_arr:
            node = Node("Wei", name=wei)
            graph.create(node)


if __name__ == "__main__":
    # execute only if run as a script
    main()

