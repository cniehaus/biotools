class Tier:
	def __init__(self):
		print "da bin ich"

	def stirb(self):
		print "ich bin dann mal weg"

t = Tier()
t.stirb()

class Mensch(Tier):
	def stirb(self):
		print "ICh bin ein Mensch gewesen"

m = Mensch()
m.stirb()
