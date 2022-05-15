GIVEN_INPUT_STRING = 'Python is a case sensitive language'
print("THE GIVEN STRING IS: 'Python is a case sensitive language'")
print("(a)- THE LENGTH OF THE STRING IS",len(GIVEN_INPUT_STRING))
print("(b)- STRING AFTER REVERSING ITS ORDER IS-:",GIVEN_INPUT_STRING[ : :-1])
NEW_STRING = GIVEN_INPUT_STRING[12:26]
print("(c)- A NEW STRING CONTAINING A PART OF GIVEN STRING AS:-", NEW_STRING)
print("(d)- FOLLOWING GIVEN INSTRUCTIONS NEW STRING WILL BE:- ",GIVEN_INPUT_STRING.replace('a case sensitive','object oriented'))
print("(e)- THE INDEX OF SUBSTRING 'a' IS",GIVEN_INPUT_STRING.index('a'))
print("(f)- REMOVING BLANK SPACES FROM STRING :-",GIVEN_INPUT_STRING.replace(' ',''))