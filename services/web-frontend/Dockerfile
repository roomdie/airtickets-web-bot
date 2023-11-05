FROM node:18 as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY ./ .
RUN npm run build

FROM nginx as production-stage
RUN mkdir /app
COPY --from=build-stage /app/dist /app
COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/security.conf /etc/nginx/security.conf
COPY nginx/ssl_certs/ /etc/nginx/ssl_certs/