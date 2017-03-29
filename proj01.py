#get Richter scale input that accepts float
#return energy in joules
#return energy in tons of TNT

def get_in():
	richter = float(input("Richter scale measurement: "))
	print("Richter measurement: {}".format(richter))
	return richter

def calculate_energy(richter):
	energy = 10**((1.5*richter)+4.8)
	print("Joules: {}".format(energy))
	return energy

def calculate_tnt(energy):
	tons_tnt = energy/(4.184e9)
	print("Tons of TNT: {}".format(tons_tnt))
	return tons_tnt
	
calculate_tnt(calculate_energy(get_in()))
