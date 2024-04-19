class PropertySelection:
    _variant: int
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(PropertySelection, cls).__new__(cls)
        return cls.instance
    def __init__(self, variant=0):
        self._variant = variant
    def get_Variant(self):
        return self._variant
    def set_Variant(self, a):
        self._variant = a


