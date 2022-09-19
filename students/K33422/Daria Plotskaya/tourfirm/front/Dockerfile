FROM node:lts-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /front

COPY package*.json ./

RUN npm install

COPY . .

# RUN npm run build

EXPOSE 8080

CMD ["npm", "run", "serve"]