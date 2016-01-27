import re
import math

# ########################################################
# fileName = "/var/www/GpsFlightMaps/04-02-15/1st Velocity Test Timestamp.txt"
# dataInputsFile = open(fileName, "r");

# print fileName, "\n"

# for line in dataInputsFile:
# 	sent = re.search(r'([0-9]*) sent at: ([0-9]*.[0-9]*)', line)
# 	arrived = re.search(r'arrived at: ([0-9]*.[0-9]*)', line)
# 	# print sent, arrived

# 	# print sent.group(1)
# 	if(int(sent.group(1)) == 1):
# 		print "Time calculated for Waypoint ", sent.group(1), "is = ", float(arrived.group(1))-float(sent.group(2))

# dataInputsFile.close()

# print "\n"


# ########################################################
# fileName = "/var/www/GpsFlightMaps/04-02-15/2nd Velocity Test Timestamp.txt"
# dataInputsFile = open(fileName, "r");

# print fileName, "\n"

# for line in dataInputsFile:
# 	sent = re.search(r'([0-9]*) sent at: ([0-9]*.[0-9]*)', line)
# 	arrived = re.search(r'arrived at: ([0-9]*.[0-9]*)', line)

# 	if(int(sent.group(1)) == 1):
# 		print "Time calculated for Waypoint ", sent.group(1), "is = ", float(arrived.group(1))-float(sent.group(2))

# dataInputsFile.close()

# print "\n"

# ########################################################

# fileName = "/var/www/GpsFlightMaps/04-02-15/3rd Velocity Test Timestamp.txt"
# dataInputsFile = open(fileName, "r");

# print fileName, "\n"

# for line in dataInputsFile:
# 	sent = re.search(r'([0-9]*) sent at: ([0-9]*.[0-9]*)', line)
# 	arrived = re.search(r'arrived at: ([0-9]*.[0-9]*)', line)

# 	if(int(sent.group(1)) == 1 or int(sent.group(1)) == 3):
# 		print "Time calculated for Waypoint ", sent.group(1), "is = ", float(arrived.group(1))-float(sent.group(2))

# dataInputsFile.close()

# print "\n"

# ########################################################

# fileName = "/var/www/GpsFlightMaps/04-02-15/4th Velocity Test Timestamp.txt"
# dataInputsFile = open(fileName, "r");

# print fileName, "\n"

# for line in dataInputsFile:
# 	sent = re.search(r'([0-9]*) sent at: ([0-9]*.[0-9]*)', line)
# 	arrived = re.search(r'arrived at: ([0-9]*.[0-9]*)', line)

# 	if(int(sent.group(1)) == 1 or int(sent.group(1)) == 3):
# 		print "Time calculated for Waypoint ", sent.group(1), "is = ", float(arrived.group(1))-float(sent.group(2))

# dataInputsFile.close()

# print "\n"

# ########################################################

# fileName = "/var/www/GpsFlightMaps/04-02-15/5th Velocity Test Timestamp.txt"
# dataInputsFile = open(fileName, "r");

# print fileName, "\n"

# for line in dataInputsFile:
# 	sent = re.search(r'([0-9]*) sent at: ([0-9]*.[0-9]*)', line)
# 	arrived = re.search(r'arrived at: ([0-9]*.[0-9]*)', line)

# 	if(int(sent.group(1)) == 1 or int(sent.group(1)) == 3):
# 		print "Time calculated for Waypoint ", sent.group(1), "is = ", float(arrived.group(1))-float(sent.group(2))

# dataInputsFile.close()

# print "\n"










string = "/hum2"
other_string = "AutoPilotNodelet/doesntMatter"

hummvalue = re.search(r'(([a-z]+)([0-9]+))', string)
print "hummvalue: ", hummvalue.group(1), hummvalue.group(2), hummvalue.group(3)

hummCurrentQuadNumber = int(hummvalue.group(3))
hummOtherQuadNumber = hummCurrentQuadNumber + 1
hummBase = hummvalue.group(2)
hummBaseNameOtherQuad = hummBase + str(hummOtherQuadNumber) + "/"
isOddQuadNumber = int(hummvalue.group(3)) % 2

print "other quad value number =  ", hummBaseNameOtherQuad
print "isOddQuadNumber: ", isOddQuadNumber


print "\n\n"

if(1):
	print "1 equals true"

if(0):
	print "0 also equals true"
else:
	print "0 equals false\n\n\n"


print "Divide value: ", 12/7.0, math.ceil(12/7.0)














































