
from .Rectangle import Rectangle
from .Page import Page
from .PageHeader import PageHeader
from .Button import Button

__rules__ = [Rectangle, Page, PageHeader, Button]

def get_rule(name, type):
    for rule in __rules__:
        elm = rule.__element__
        if (not elm.name or elm.name in name.split("/")) \
        and (not elm.type or elm.type == type):
            return rule
        
    return None
