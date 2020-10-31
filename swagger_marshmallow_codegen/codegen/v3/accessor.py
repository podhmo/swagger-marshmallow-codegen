from ..v2.accessor import Accessor as V2Accessor


class Accessor(V2Accessor):
    def definitions(self, d):
        components = d.get("components")
        if components is None:
            return {}
        return (components.get("schemas") or {}).items()
