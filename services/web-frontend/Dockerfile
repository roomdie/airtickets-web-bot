FROM node:19-alpine as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
RUN npm i @vue/cli-service
COPY ./ .
CMD ["npm", "run", "serve"]

#FROM nginx as production-stage
#RUN mkdir /app
#COPY --from=build-stage /app/dist /app
#COPY nginx/nginx.conf /etc/nginx/nginx.conf
#COPY nginx/security.conf /etc/nginx/security.conf
#COPY nginx/ssl_certs/ /etc/nginx/ssl_certs/