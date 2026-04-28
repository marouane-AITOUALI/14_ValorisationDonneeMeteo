ARG NODE_BASE_IMAGE=node:24-alpine

FROM ${NODE_BASE_IMAGE} AS build

WORKDIR /app

COPY package*.json .

RUN npm ci --legacy-peer-deps

RUN npm rebuild esbuild

COPY . .

RUN npm run build

ARG NODE_BASE_IMAGE=node:24-alpine

FROM ${NODE_BASE_IMAGE} AS prod

WORKDIR /app

COPY --from=build /app/.output /app/.output

ENV NODE_ENV=production

EXPOSE 3000

CMD [ "node", ".output/server/index.mjs" ]
