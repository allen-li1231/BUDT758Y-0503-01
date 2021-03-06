# BUDT758Y-0503-01 Project Visualization Section
Dynamic website for leasing apartment around UMD
---
Contain: 
+ Source code of frontend-backend project website.

Library:
+ django, pyodbc, django-pyodbc-azure, numpy


### Installing and running
> :warning: Note: In order for this server to run properly, you will also need VPN to access UMD local network, a google API key to enable map Javascript service and configure database password in BUDT758Y-0503-01/locallibrary/settings.py. Please consult repo's author for more information.

1. git clone or download to your local driver
2. configure database keyword, google API key
3. launch server that can be accessed only on your computer
on Linux:
``` shell
cd ./BUDT758Y-0503-01 && python manage.py runserver 127.0.0.1:8000
```
Or in powershell:
``` shell
cd ./BUDT758Y-0503-01 ; python manage.py runserver 127.0.0.1:8000
```
4. open browser and get access to http://127.0.0.1:8000

### File tree
``` bash
.
├── catalog   # Django app directory
│   ├── migrations
│   ├── templates   # contains html templates to be rendered by django engine. Also a directory for static file source
│   └── templatetags    # contains parsing tools for html render
├── locallibrary    # contains settings.py, global configuration for Django
└── static    # static file directory
```
