SRC_DIR = pyhn
DOC_DIR = docs
MAKE = make

all:
	make lint
	make test
	make html
	make clean

lint:
	pylint --rcfile=.pylintrc --load-plugins pylint_django -E $(SRC_DIR)

lintall:
	pylint --rcfile=.pylintrc --load-plugins pylint_django $(SRC_DIR)

test:
	python $(SRC_DIR)/manage.py test --nocapture --with-coverage --cover-package=$(SRC_DIR)

html:
	cd $(DOC_DIR) && $(MAKE) html

clean:
	find $(SRC_DIR) -name "*.pyc" | xargs rm

run:
	python $(SRC_DIR)/manage.py runserver 0.0.0.0:$(PORT) --settings=pyhn.ui.settings_dev
