import copy

class Item:
    __figma_type__ = ""
    __can_children__ = True
    
    def __init__(self, js):
        if "absoluteBoundingBox" in js:
            pos = js["absoluteBoundingBox"]
            self.x = pos["x"]
            self.y = pos["y"]
            self.width = pos["width"]
            self.height = pos["height"]
            
    def get_js(self):
        js = self.__dict__
        js["type"] = self.__class__.__name__
        childs = []
        for child in self.children:
            childs.append(child.get_js())
        js["children"] = childs
        return js
    
    def get_qml(self):
        js =  copy.copy(self.__dict__)
        qml_type = self.__class__.__name__
        txt = qml_type + " {"
        del js["children"]
        for prop, value in js.items():
            if type(value) is str:
                txt_line = f'{prop}: "{value}"'
            else:
                txt_line = f'{prop}: {value}'
            txt += "\n\t" + txt_line
        for child in self.children:
            txt_child = "\n" + child.get_qml()
            txt_child = txt_child.replace("\n", "\n\t")
            txt += txt_child
        txt += "\n}"
        return txt
