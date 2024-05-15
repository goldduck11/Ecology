class PropertySelection:
	_variant: int
	_gerts: int
	_B: float
	_s: int
	_Sogr: int
	_L: float
	_Alfa: float
	_Lp: float
	R: float
	R1: float
	R0: float
	Sorg: int

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

	def set_R(self, R):
		self.R = R

	def get_R(self):
		return self.R

	def set_R1(self, R1):
		self.R1 = R1

	def get_R1(self):
		return self.R1

	def set_R0(self, R0):
		self.R0 = R0

	def get_R0(self):
		return self.R0

	def set_Sorg(self, Sorg):
		self.Sorg = Sorg

	def get_Sorg(self):
		return self.Sorg