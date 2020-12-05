
from .Rectangle import Rectangle
from .Page import Page


__rules__ = [Rectangle, Page]

def get_rule(name, type):
    for rule in __rules__:
        elm = rule.__element__
        if elm.name == name \
        and elm.type == type:
            return rule
        
    return None
