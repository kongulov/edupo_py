# for static files serve 
location /static {
    root /var/data;
}
# for media files serve
location /media {
    root /var/data;
}
