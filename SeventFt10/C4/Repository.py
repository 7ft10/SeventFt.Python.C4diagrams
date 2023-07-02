"""
Repository
"""
from .Factory import Factory

class Repository():
    def Print(self):
        """
        """
        for member in dir(self):
            typ = getattr(self, member)
            if isinstance(typ, Factory):
                typ.Print()
