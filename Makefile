SRC_DIR = src
DOC_DIR = docs
PROJECT_DIR = pyhn
MAKE = make
PORT = 8080

all:
	make install
	make test
	make html
	make clean

install:
	pip install -r requirements/prod.txt -q
	pip install -r requirements/dev.txt -q
	pip install -r requirements/docs.txt -q
	pip install -r requirements/test.txt -q

lint:
	prospector $(SRC_DIR) -s veryhigh

test:
	python $(SRC_DIR)/manage.py test --failfast --nocapture --with-coverage --cover-package=$(PROJECT_DIR) --cover-erase --settings=pyhn.settings.test

html:
	cd $(DOC_DIR) && $(MAKE) html

clean:
	rm -rf *.egg-info
	rm -rf build/*
	rm -rf dist/*
	rm -rf src/*.egg-info
	find $(SRC_DIR) -name "*.pyc" | xargs rm

run:
	cd $(SRC_DIR) && python manage.py runserver 0.0.0.0:$(PORT)

score:
	python $(SRC_DIR)/manage.py score
