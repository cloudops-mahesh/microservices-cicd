FROM node:20-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm install --silent

COPY . .

ARG REACT_APP_API_URL=""
ENV REACT_APP_API_URL=$REACT_APP_API_URL

RUN npm run build

FROM nginx:1.25-alpine AS runtime

COPY --from=builder /app/build /usr/share/nginx/html
COPY nginx-spa.conf /etc/nginx/conf.d/default.conf

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD wget --quiet --tries=1 --spider http://localhost:3000 || exit 1

CMD ["nginx", "-g", "daemon off;"]