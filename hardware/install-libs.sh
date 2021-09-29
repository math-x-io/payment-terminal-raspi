#!/bin/bash
if [ ! -d ./src/py532lib ] && [ ! -d ./src/quick2wire ]; then
	git clone https://github.com/HubCityLabs/py532lib.git
	mv py532lib/py532lib ./src
	mv py532lib/quick2wire ./src
	rm -rf py532lib
else
	echo "Libs already installed locally"
fi
