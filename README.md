# web_love
config_location:
include /etc/nginx/conf.d/*.conf;
include /etc/nginx/sites-enabled/*;

config:
server {
  charset utf-8;
  listen 80;
  server_name 106.14.215.109;  # 改成你的公网 IP
 
  location /static {
    alias /root/baopanpan/web_love/login/static;
  }
 
  location / {
    proxy_set_header Host $host;
    proxy_pass http://unix:/tmp/106.14.215.109.socket;  # 改成你的 公网IP
  }
}

start_command:
sudo nginx -s reload
gunicorn --bind unix:/tmp/106.14.215.109.socket web_love.wsgi:application


error_log:
access_log /var/log/nginx/access.log;
error_log /var/log/nginx/error.log;
