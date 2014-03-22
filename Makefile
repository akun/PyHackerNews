SRC_DIR = ./pyhn
DOC_DIR = ./docs
MAKE = make

all:
	make lint
	make test
	make html
	make clean

lint:
	pylint --rcfile=.pylintrc --load-plugins pylint_django -E $(SRC_DIR)/news

lintall:
	pylint --rcfile=.pylintrc --load-plugins pylint_django $(SRC_DIR)/news

test:
	cd $(SRC_DIR) && python manage.py test --with-coverage --cover-package=news,pyhn

html:
	cd $(DOC_DIR) && $(MAKE) html

clean:
	find $(SRC_DIR) -name "*.pyc" | xargs rm
