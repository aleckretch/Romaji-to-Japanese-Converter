import convert

def main():
	while 1:
		romaji = input("Enter a Romaji string: ")
		japanese = convert.romajiToJapanese(romaji.lower())
		print("Japanese equivalent: %s" % japanese)

main()
