import linecache

def centerText(font, text, screenWidth):
	newsc = screenWidth / 2
	newsc -= (font.size(text)[0])/2
	return newsc
	
def getText(line, filename="text.txt"):
	ret = linecache.getline(filename, line)
	return ret