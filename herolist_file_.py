fav_characters= ["hulk","thor","black windows","black panther"]

def myfunction(herolist):    
	print(" the last is:", herolist[-1])
        with open("heroes.txt","w") as slappy:
	    for char in herolist:
		print(char,file=slappy)
myfunction(fav_characters)
