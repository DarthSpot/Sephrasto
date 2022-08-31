
all: compile

compile:
	pyinstaller ./src/Sephrasto/Sephrasto.py --onefile
	cp -r ./src/Sephrasto/Data ./dist/
	cp -r ./src/Sephrasto/Doc ./dist/
	cp -r ./src/Sephrasto/Bin ./dist/
