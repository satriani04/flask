# flask

## how to use

create virtualenv for project
```
$ virtualenv blogenv
```
install all package
```
$ pip install -r requirements.txt
```
do config for your database on model.py
then run
```
$ python model.py db init
$ python model.py db migrate
$ python model.py db upgrade
```

run application
```
$ python app.py
```

open your browser on port 5000
