from .langhelpers import titleize
from dictknife.jsonknife.lifting import Handler, SubDefinitionLifting


class MyHandler(Handler):
    def add_name(self, name):
        self.path.append(titleize(name))


def lifting_definition(data, replace=True):
    w = SubDefinitionLifting(replace=replace)
    for name in list(data["definitions"].keys()):
        prop = data["definitions"].pop(name)
        extracted = w.extract(prop, MyHandler([name]))
        extracted[name] = prop
        data["definitions"].update(reversed(extracted.items()))
    return data
