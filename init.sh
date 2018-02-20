sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo gunicorn -c /home/box/web/etc/heloo.py hello:wsgi_application
sudo gunicorn -c /home/box/web/etc/django.py ask.wsgi:application
