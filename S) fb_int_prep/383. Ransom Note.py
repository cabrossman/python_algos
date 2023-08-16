def main(s1, s2):
	#create map on count of chars for s1.
	# iterate through s2 decrimenting characters
	# if character not found in map or count <= 0 then False
	#finish iterating through set
	mapp = {}
	for i in range(len(s1)):
		mapp[ s1[i] ] = mapp.get( s1[i] , 0) + 1
	
	for i in range(len(s2)):
		if mapp.get( s2[i], 0) == 0:
			return False
		else:
			mapp[ s2[i] ] = mapp.get( s2[i] , 0) - 1
	return True

assert main(s2='a', s1='b') == False
assert main(s2='aa', s1='ab') == False
assert main(s2='aa', s1='aab') == True
print('all tests passed!')