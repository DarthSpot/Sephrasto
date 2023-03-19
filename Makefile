
all: compile copydata

compile:
	~/.local/bin/pyinstaller ./src/Sephrasto/Sephrasto.py --onefile

copydata:
	cp -r ./src/Sephrasto/Data ./dist/
	cp -r ./src/Sephrasto/Doc ./dist/
	cp -r ./src/Sephrasto/Bin ./dist/
