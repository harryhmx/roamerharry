# Startup project demo

To startup this demo website, the things below you may want to cover:

### Requirements

* Python ( 3.7 )
* Django ( 2.2 )
* MySQL ( 8.0 )

Firstly, you should make sure Python ( 3.7 ) and MySQL ( 8.0 ) are successfully installed.

Then, following the steps below

### Install pip & django & markdown

  `$ wget https://bootstrap.pypa.io/get-pip.py`

  `$ sudo python3 get-pip.py`

  `$ sudo pip3 install django==2.2`

### Download Codes

  `$ git clone https://github.com/harryhmx/roamerharry.git`

  `$ cd roamerharry`

### Run Server

  `$ python3 manage.py runserver`

  Then enter address `http://localhost:8000` or `http://127.0.0.1:8000` on browser,
  you can see the webpage, `127.0.0.1 ( localhost )` and `8000` are the default ip and port.

  If you wanna declare the ip and port, for example like `192.168.1.123 ( ip )` and `8452 ( port )`,
  you can run command below,

  `$ python3 manage.py runserver 192.168.1.123:8452`

  Then enter address `http://192.168.1.123:8452` on browser, you can see the webpage as well.
