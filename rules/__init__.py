
from .Rectangle import Rectangle


__rules__ = [Rectangle]

def get_rule(name, type):
    for rule in __rules__:
        elm = rule.__element__
        if elm.name == name \
        and elm.type == type:
            return rule
        
    return None
