SRC_DIR = src
DOC_DIR = docs
PROJECT_DIR = pyhn
MAKE = make

all:
	make lint
	make test
	make html
	make clean

lint:
	pylint --rcfile=.pylintrc --load-plugins pylint_django -E $(SRC_DIR)/$(PROJECT_DIR)

lintall:
	pylint --rcfile=.pylintrc --load-plugins pylint_django $(SRC_DIR)/$(PROJECT_DIR)

test:
	cd $(SRC_DIR) && python manage.py test --nocapture --with-coverage --cover-package=$(PROJECT_DIR)

html:
	cd $(DOC_DIR) && $(MAKE) html

clean:
	find $(SRC_DIR) -name "*.pyc" | xargs rm

run:
	cd $(SRC_DIR) && python manage.py runserver 0.0.0.0:$(PORT) --settings=pyhn.settings_dev
