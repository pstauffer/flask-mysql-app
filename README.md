# Flask Mysql Demo-App

This repo provides a demo-app for the [Ansible training](https://blog.confirm.ch/ansible-training/).


## Requirements

### Frontend

#### on all hosts
* Install this PIP packages: `flask`, `flask-mysql`, `markupsafe`
* Clone this repo -> `git clone https://github.com/pstauffer/flask-mysql-app.git`

#### Red Hat
* The epel channel is needed -> Install the `epel-release` package
* Install this yum packages: `python-devel`, `python-pip`, `MySQL-python`, `python-gunicorn`

#### Debian
* Install this apt/deb packages: `libmysqlclient-dev`, `python-dev`, `python-pip`, `gunicorn`

### Backend
* Install the `mysql-server` package
* Configure mysql to listen on the address `0.0.0.0` -> `bind-address = 0.0.0.0`
* Download the [mysqldump](https://raw.githubusercontent.com/pstauffer/flask-mysql-app/master/students.sql)
* Load the dump -> `mysql --user=root --password='' < /tmp/students.sql`


## Configuration
* Create a "version" file `/tmp/app-version.txt` with the tag/branch
* Create the dbhost file `/etc/dbhost.cfg` and configure your database host. [Example](dbhost.cfg)


## Run your application

### with python

```bash
cd <install-dir>
python app.py
```

### with gunicorn

```bash
gunicorn --pid /tmp/gunicorn.pid --chdir <install-dir> --bind 0.0.0.0:8000 --daemon wsgi:app
```


## Test URLs
* http://web1.[name].lab:8000/
* http://web2.[name].lab:8000/
