# BUDT758Y-0503-01 Project Visualization section
### This repo contains dynamic nice-looking website for BUDT758Y-0503-01 team project
---
Contain: 
+ Source code of frontend-backend project website.

Library:
+ django, pyodbc, django-pyodbc-azure, numpy


### Installing and running 
> :warning: Note: In order this server to run properly, you will also need VPN to access UMD local network, a google API key to enable map Javascript service and configure database password in BUDT758Y-0503-01/locallibrary/settings.py. Please consult  [zhonghao.li@rhsmith.umd.edu](mailto:zhonghao.li@rhsmith.umd.edu) for more information.

1. git clone to your local driver
2. configure database keyword, google API key
3. launch server that can be accessed only on your computer
``` shell
cd ./BUDT758Y-0503-01 && python manage.py runserver 127.0.0.1:8000
```
4. open browser and get access to http://127.0.0.1:8000
