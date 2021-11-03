FROM nginxinc/nginx-unprivileged:1.20-alpine

COPY ./run.sh /run.sh
COPY ./default.conf.tpl /etc/nginx/default.conf.tpl

ENV LISTEN_PORT=8000
ENV APP_HOST=app
ENV APP_LISTEN=8000

USER root

RUN mkdir -p /vol/static && \
    chmod 755 /vol/static && \
    touch /etc/nginx/conf.d/default.conf && \
    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
    chmod +x run.sh

VOLUME /vol/static

USER nginx


CMD ["./run.sh"]
