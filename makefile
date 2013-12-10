all:
	[ -e "hyde" ] || (git clone git@github.com:Psycojoker/hyde.git && cd hyde/ && virtualenv ve && ve/bin/pip install -r requirements.txt && ve/bin/python setup.py develop)
	hyde/ve/bin/hyde -g
