from abc import ABC, abstractmethod

class Plugin(ABC):
    @abstractmethod
    def name(self):
        pass
    @abstractmethod
    def execute(self, input_data):
        pass

class PluginMeta(type):
    plugins = []
    def __init__(cls,name,bases,class_dict):
        super().__init__(name,bases,class_dict)
        if cls.__name__!='Plugin':
            PluginMeta.plugins.append(cls)

    @classmethod
    def register(cls,plugin_class):
        cls.plugins.append(plugin_class)

@PluginMeta.register
class SumPlugin(Plugin):
    def name(self):
        return "Sum Plugin"

    def execute(self, input_data):
        return sum(input_data)

@PluginMeta.register
class ProductPlugin(Plugin):
    def name(self):
        return "Product Plugin"

    def execute(self, input_data):
        res =1
        for val in input_data:
            res = res * val
        return res

input_data = [1,2,3,4,5]

for plugin_class in PluginMeta.plugins:
    plugin = plugin_class()
    res = plugin.execute(input_data)
    print(f"{plugin.name()}: {res}")
