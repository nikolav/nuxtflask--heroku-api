# deploy setup

## pre.git-push
  - db.host: https://github.com/nikolav/dbpg.git
  - set `PRODUCTION=1`, `*_production`, `UPLOAD_PATH=..` urls, @/.env, lines: 3, 10, 30, 56
  - set `NUXTAPP_HOST=..` @/scp-config.sh, lines: 2

## deploy
  - @home: `$ git push heroku main `
