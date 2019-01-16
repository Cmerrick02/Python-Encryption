import sys

"""
Author: Cory Merrick
Python script to encrypt files with simple cipher substitution.
option to reverse below
"""


key = {"A":"T","B":"D","C":"L","D":"O","E":"F","F":"A","G":"G","H":"J","I":"K","J":"R","K":"I","L":"C","M":"V","N":"P","O":"W","P":"U","Q":"X","R":"Y","S":"B","T":"E","U":"Z","V":"Q","W":"S","X":"N","Y":"M","Z":"H",
	"a":"t","b":"d","c":"l","d":"o","e":"f","f":"a","g":"g","h":"j","i":"k","j":"r","k":"i","l":"c","m":"v","n":"p","o":"w","p":"u","q":"x","r":"y","s":"b","t":"e","u":"z","v":"q","w":"s","x":"n","y":"m","z":"h"}

"""
Uncomment follow to reverse encryption
"""

"""
key = dict(zip(key.values(),key.keys()))
"""


list_key = key.values()
for item in list_key:
	if list_key.count(item) != 1:
		print "problem with: ", item, " count is ", list_key.count(item)

inputfile = sys.argv[1]
outputfile = 'encrypted_' + inputfile
result = ''

f = open(inputfile, 'r')

while True:
	a = f.read(1)
	if not a: break
	if a in key:
		result = result + key[a]
	else:
		result = result + a
f.close()
g = open(outputfile, 'w')
g.write(result)
g.close()
