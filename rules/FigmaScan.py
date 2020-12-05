
class Element:
    name: str
    type: str
    def __init__(self, name, type):
        
        self.name = name
        self.type = type

def get_element_by_path(childs: list, name:str, type: str):
    for elm in childs:
        if (not name or name in elm.get("name", "").split("/")) \
        and (not type or type == elm.get("type", None)):
            return elm
        
    return None
