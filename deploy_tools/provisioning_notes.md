Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3.6
* virtualenv + pip
* Git

eg, on Ubuntu:

    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install nginx git python3.6 python3.6-venv

## Nginx Virtual Host config

* see nginx.template.
* replace Domain with, e.g. staging.my-domain.com

## Systemd service

* see gunicorn-systemd.template.service
* replace DOMAIN with, e.g. staging.my-domain.com
* Systemd logs: sudo journalctl -u gunicorn-superlists-staging.ottg.eu.
* systemd-analyze verify /path/to/my.service
* sudo systemctl daemon-reload
* sudo systemctl start gunicorn-my-domain.com

## Folder structure:

Assume we have a user account at /home/username

/home/username
└── sites
    ├── DOMAIN1
    │    ├── .env
    │    ├── db.sqlite3
    │    ├── env
    │    ├── manage.py etc
    │    └──  static
    └── DOMAIN2
         ├── .env
         ├── db.sqlite3
         ├── etc