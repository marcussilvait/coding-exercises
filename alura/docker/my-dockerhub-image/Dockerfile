FROM node:latest
MAINTAINER Marcus Vinicius Laurindo da Silva
ENV NODE_ENV=development
ENV PORT=3000
COPY . /var/www
WORKDIR /var/www
RUN npm install
ENTRYPOINT [ "npm", "start" ]
EXPOSE $PORT