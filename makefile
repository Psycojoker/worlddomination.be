.PHONY: deploy

all:
	[ -e "hyde" ] || (git clone git@github.com:Psycojoker/hyde.git && cd hyde/ && virtualenv ve && ve/bin/pip install -r requirements.txt && ve/bin/python setup.py develop)
	hyde/ve/bin/hyde -g

run:
	[ "$(dpkg -l | grep webfs)" ] || (sudo apt-get install webfs)
	[ "$(pgrep webfsd)" ] || (cd ./deploy/ && webfsd -p 3957)
	firefox 0.0.0.0:3957/index.html

stop:
	killall webfsd

deploy: all
	[ -e "/usr/local/bin/git-up" ] || (sudo pip install git-up)
	git up
	git add .
	git commit -am "update"
	rsync -r deploy/* bram@worlddomination.be:www/
	git push

loop:
	while true; do make; inotifywait -e modify content/**/*; done
