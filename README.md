# Startup project demo

To startup this demo website, `Linux (Ubuntu)` system is recommended,

and the things below you may want to cover

### Requirements

* Python ( 3.7 )
* MySQL ( 8.0 )
* Django ( 2.2 )
* PyMySQL

Firstly, you should make sure `Python ( 3.7 )` and `MySQL ( 8.0 )` are successfully installed,

then following the steps below

* Install PIP

`$ wget https://bootstrap.pypa.io/get-pip.py`

`$ sudo python3 get-pip.py`

* Install Django

`$ sudo pip3 install django==2.2`

* Install PyMySQL

`$ sudo pip3 install pymysql`

### Download Codes

`$ git clone https://github.com/harryhmx/roamerharry.git`

`$ cd roamerharry`

### Databases Configuration

`$ vim /path-to-python3.7-lib/site-packages/django/db/backends/mysql/operations.py`

```py
# Check line 140 ~ 147
def last_executed_query(self, cursor, sql, params):
    # With MySQLdb, cursor objects have an (undocumented) "_executed"
    # attribute where the exact query sent to the database is saved.
    # See MySQLdb/cursors.py in the source distribution.
    query = getattr(cursor, '_executed', None)
    if query is not None:
        # query = query.decode(errors='replace')
        query = query.encode(errors='replace')  # decode -> encode
    return query
```

`$ cp roamerharry/custom.py.example roamerharry/custom.py`

`$ vim roamerharry/custom.py`

```py
# Make configuration as below
ENGINE = 'django.db.backends.mysql'
NAME = 'roamerharry'
USER = 'root'
PASSWORD = 'your_password'
HOST = 'localhost'
PORT = 3306
```

`$ python3 manage.py makemigrations`

`$ python3 manage.py migrate`

### Run Server

* Default Mode

`$ python3 manage.py runserver`

Then enter address `http://localhost:8000` or `http://127.0.0.1:8000` on browser.

* With `ip` and `port`

`$ python3 manage.py runserver [ip]:[port]`

Then enter address `http://[ip]:[port]` on browser, you can see the webpage as well.

* For multiple systems (devices) under common network

`$ python3 manage.py runserver 0.0.0.0:[port]`
