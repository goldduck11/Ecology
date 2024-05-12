class PropertySelection:
	_variant: int
	_gerts: int
	_B: float
	_s: int
	_Sogr: int
	_L: float
	_Alfa: float
	_Lp: float

	def __new__(cls):
		if not hasattr(cls, 'instance'):
			cls.instance = super(PropertySelection, cls).__new__(cls)
		return cls.instance

	def __init__(self):
		pass

	def get_Variant(self):
		return self._variant

	def set_Variant(self, a):
		self._variant = a

	def get_Gerts(self):
		return self._gerts

	def set_Gerts(self, a):
		self._gerts = a

	def set_B(self, a):
		self._B = a
	def get_B(self):
		return self._B

	def get_s(self):
		return self._s

	def set_s(self, s):
		self._s = s

	def get_Sogr(self):
		return self._Sogr

	def set_Sogr(self, Sogr):
		self._Sogr = Sogr

	def get_L(self):
		return self._L

	def set_Sogr(self, L):
		self._L = L

	def set_Alfa(self, alfa):
		self._Alfa = alfa

	def get_Alfa(self):
		return self._Alfa

	def get_Lp(self):
		return self._Lp

	def set_Lp(self, Lp):
		self._Lp = Lp