etudiants = [
	{
		"matricule" : 1000,
		"nom" : "JOHN",
		"prenome" : "DOE",
		"note": 15
	},
	{
		"matricule" : 2000,
		"nom" : "BOB",
		"prenome" : "CARLON",
		"note": 9
	},

	{
		"matricule" : 3000,
		"nom" : "RAYANE",
		"prenome" : "SMITH",
		"note": 13
	},

]

def estAdmissible(note) :
	return note > 9

for e in etudiants :
	if(estAdmissible(e['note'])):
		print(e)


