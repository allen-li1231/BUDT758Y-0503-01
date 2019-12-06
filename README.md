# BUDT758Y-0503-01 Project Visualization Section
### This repo contains dynamic website for BUDT758Y-0503-01 team project
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
In Linux:
``` shell
cd ./BUDT758Y-0503-01 && python manage.py runserver 127.0.0.1:8000
```
In powershell:
``` shell
cd ./BUDT758Y-0503-01 ; python manage.py runserver 127.0.0.1:8000
```
4. open browser and get access to http://127.0.0.1:8000

### File tree
BUDT758Y-0503-01
> catalog
> > migrations
> > templates   # contains html templates for django to render
> > templatetags    # contains parse tools for html templates

+-- _config.yml
+-- _drafts
|   +-- begin-with-the-crazy-ideas.textile
|   +-- on-simplicity-in-technology.markdown
+-- _includes
|   +-- footer.html
|   +-- header.html
+-- _layouts
|   +-- default.html
|   +-- post.html
+-- _posts
|   +-- 2007-10-29-why-every-programmer-should-play-nethack.textile
|   +-- 2009-04-26-barcamp-boston-4-roundup.textile
+-- _data
|   +-- members.yml
+-- _site
+-- index.html
