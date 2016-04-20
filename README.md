# Flask Mysql Demo-App

This repo provides a demo-app for the [Ansible training](https://blog.confirm.ch/ansible-training/).


## Requirements

### Frontend

#### on all hosts
* PIP packages: `flask`, `flask-mysql`
* Clone this repo -> `git clone https://github.com/pstauffer/flask-mysql-app.git`

#### Red Hat
* `epel-release` package
* `python-devel`, `python-pip`, `MySQL-python`, `python-gunicorn` packages

#### Debian
* `libmysqlclient-dev`, `python-dev`, `python-pip`, `gunicorn` packages

### Backend
* `mysql-server` package
* `bind-address = 0.0.0.0`
* Download the [mysqldump](https://raw.githubusercontent.com/pstauffer/flask-mysql-app/master/students.sql)
* Load the dump -> `mysql --user=root --password='' < /tmp/students.sql`


## Configuration
* create a "version" file `/tmp/app-version.txt` with the tag/branch
* create the dbhost file `/etc/dbhost.cfg` and configure your database host. [Example](dbhost.cfg)


## Run your application

### with python

```bash
cd <install-dir>
python app.py
```

### with gunicorn

```bash
gunicorn --chdir <install-dir> --bind 0.0.0.0:8000 --daemon wsgi:app
```


## Test URLs
* http://web1.[name].lab:8000/
* http://web2.[name].lab:8000/
