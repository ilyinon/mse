FROM nginx:stable

ADD nginx.conf_docker /etc/nginx/nginx.conf
ADD uwsgi_params /etc/nginx/uwsgi_params

EXPOSE 80 443
CMD ["nginx", "-g", "daemon off;"]
