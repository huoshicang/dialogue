FROM node:21.0.0-alpine as frontend-builder

RUN npm config set registry https://registry.npm.taobao.org/

WORKDIR /app

COPY frontend-vue/package.json /app/
COPY frontend-vue/package-lock.json /app/

RUN npm i

COPY frontend-vue/. /app/

RUN npm run build

EXPOSE 8080


FROM python:3.12.3-alpine

RUN apk add --update caddy gcc musl-dev libffi-dev

WORKDIR /app

COPY backend/requirements.txt /app/

RUN pip3 config set global.index-url https://mirrors.aliyun.com/pypi/simple/

RUN pip install -r requirements.txt

RUN pip install redis

COPY backend/. /app/

COPY Caddyfile /app/Caddyfile

COPY --from=frontend-builder /app/dist /app/backend/dist

EXPOSE 80

COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

CMD ["/app/start.sh"]