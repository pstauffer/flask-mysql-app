# Flask Mysql Demo-App

This repo provides a demo-app for the [Ansible training](https://blog.confirm.ch/ansible-training/).

## Requirements

### Frontend

#### Red Hat
* The epel channel is needed -> Install the `epel-release` package
* Install these yum packages: `python3-devel`, `python3-pip`, `MySQL-python`, `python3-gunicorn`
* Install PIP packages: `flask`, `flask-mysql`, `markupsafe`
* Clone this repo -> `git clone https://github.com/pstauffer/flask-mysql-app.git`

#### Debian
* Install this apt/deb packages: `pythoni3-dev`, `python3-pip`, `python3-gunicorn`, `gunicorn3`
* Install PIP packages: `flask`, `flask-mysql`, `markupsafe`
* Clone this repo -> `git clone https://github.com/pstauffer/flask-mysql-app.git`

### Backend
* Install the `mariadb-server` package
* Configure mysql to listen on the address `0.0.0.0` -> `bind-address = 0.0.0.0`
* Download the [mysqldump](https://raw.githubusercontent.com/pstauffer/flask-mysql-app/master/students.sql)
* Load the dump -> `mysql --user=root --password='' < /tmp/students.sql`

## Configuration
* Create a version file `/tmp/app-version.txt` and add the tag/branch as content
* Create the dbhost file `/etc/dbhost.cfg` and add your database host as content, [Example](dbhost.cfg)

## Run your application

### with python

```bash
cd <install-dir>
python3 app.py
```

### with gunicorn

```bash
# debian
gunicorn3 --pid /tmp/gunicorn.pid --chdir <install-dir> --bind 0.0.0.0:8000 --daemon wsgi:app

# redhat/centos
gunicorn-3 --pid /tmp/gunicorn.pid --chdir <install-dir> --bind 0.0.0.0:8000 --daemon wsgi:app
```

## Test URLs
* http://web1.[name].lab:8000/
* http://web2.[name].lab:8000/
