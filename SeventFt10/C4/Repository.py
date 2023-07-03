"""
Repository
"""
import os
import importlib
import requests
from .Factory import Factory

class Repository():

    @staticmethod
    def LoadFromString(content, module_name, file_name = None):
        """
        """
        if not file_name: file_name = '{0}.py'.format(module_name)
        value = compile(content, file_name, 'exec')
        module_spec = importlib.machinery.ModuleSpec(module_name, None)
        module = importlib.util.module_from_spec(module_spec)
        exec (value, module.__dict__)
        return module

    @staticmethod
    def LoadFromUrl(url, module_name = None):
        """
        """
        file_name:str = os.path.basename(url).lower()
        if (not file_name.endswith(".py") or file_name.endswith("/")):
            file_name = '__init__.py'
            url += "/" + file_name
        if not module_name: module_name = os.path.splitext(file_name)[0]
        r = requests.get(url)
        r.raise_for_status()
        return Repository.LoadFromString(r.content, module_name, file_name = file_name)

    def DisplayMarkdown(self):
        """
        """
        for member in dir(self):
            typ = getattr(self, member)
            if isinstance(typ, Factory):
                typ.DisplayMarkdown()

    def Print(self):
        """
        """
        for member in dir(self):
            typ = getattr(self, member)
            if isinstance(typ, Factory):
                typ.Print()
