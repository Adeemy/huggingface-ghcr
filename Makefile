install:
	pip install --upgrade pip &&\
		pip install black[jupyter] pytest pylint

format:
	black .

test:	
	pytest -vvv

debug:
	pytest -vvv --pdb

lint:
	pylint --disable=R,C,E0401,E0110,I1101 ./webapp

all: install format test lint