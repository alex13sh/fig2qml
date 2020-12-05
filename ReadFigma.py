import json
import rules

def proc_json(js):
    rule = rules.get_rule(js["name"], js["type"])
    if rule is not None:
        print(f'{js["name"]}, {js["type"]}')
    children = []
    if "children" in js:
        for child in js["children"]:
            res = proc_json(child)
            if type(res) is list:
                children.extend(res)
            else:
                children.append(res)

    if rule:
        rule = rule(js)
        rule.children = children
        return rule
    else:
        return children

if __name__ == "__main__":
    
    js = {}
    with open("./figma_json/obj_figmaPage.json") as f:
        js = json.loads(f.read())
       
    res = proc_json(js)
    print(res)
    #tst = 2
    #if p := tst:
        #print(p)
