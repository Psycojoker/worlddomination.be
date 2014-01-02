.PHONY: deploy

all: _check_dependancies
	hyde/ve/bin/hyde -g

run: _check_dependancies
	hyde/ve/bin/hyde -w || (hyde/ve/bin/pip install -r hyde/requirements.txt && hyde/ve/bin/hyde -w)

deploy:
	[ -e "/usr/local/bin/git-up" ] || (sudo pip install git-up)
	git up
	git add .
	git commit -am "update"
	make all
	rsync -r deploy/* bram@worlddomination.be:www/
	git push

loop: _check_dependancies
	hyde/ve/bin/hyde -g -k -w || (hyde/ve/bin/pip install -r hyde/requirements.txt && hyde/ve/bin/hyde -g -k -w)

push:
	git up
	git add .
	git commit -am "update"
	git push

_check_dependancies:
	[ -e "hyde" ] || (git clone git@github.com:Psycojoker/hyde.git && cd hyde/ && virtualenv ve && ve/bin/pip install -r requirements.txt && ve/bin/python setup.py develop)
