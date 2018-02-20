sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo gunicorn -c /etc/gunicorn.d/hello.py hello:application
sudo gunicorn -c /etc/gunicorn.d/django.py ask.wsgi:application
sudo /etc/init.d/gunicorn restart
sudo unlink /etc/gunicorn.d/django
sudo ln -s /home/box/web/etc/django /etc/gunicorn.d/django
sudo /etc/init.d/gunicorn restart
