# deploy setup

## pre.git-push
  - set `PRODUCTION=1`, `*_production`, `UPLOAD_PATH=..` urls, @/flaskapi/.env, lines: 3, 10, 30, 56
  - set `PRODUCTION$ = true`, `*_production` paths, @/nuxtapp/config/vars.env.ts, lines: 4, 9
  - for static generation (nuxtConfig.ssr = false), set `BASE_DIR = /app/path`, @/nuxtapp/.env, lines: 2
  - set `NUXTAPP_HOST=..` @/scp-config.sh, lines: 2

## deploy
  - @host: mkdir -p /root/app; cd /root/app; git clone _repository_
  - @home: . scp-config.sh
  - @host: . deploy-env.sh; . deploy.sh
