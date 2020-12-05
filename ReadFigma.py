import json
import rules

def proc_json(js):
    rule = rules.get_rule(js["name"], js["type"])
    if rule is not None:
        rule = rule(js)
        if not rule.__can_children__:
            js["children"] = []
    
    children = []
    for child in js.get("children", []):
        res = proc_json(child)
        if type(res) is list:
            children.extend(res)
        else:
            children.append(res)

    if rule:
        rule.children = children
        return rule
    else:
        return children

if __name__ == "__main__":
    
    js = {}
    with open("./figma_json/obj_figmaPage.json") as f:
        js = json.loads(f.read())
       
    res = proc_json(js)
    if type(res) is list:
        for elm in res:
            print(elm.get_qml())
    else: print(res.get_qml())
    #tst = 2
    #if p := tst:
        #print(p)
