# IAFE
**I Always Forget Everything**

## IAFE.EXPENSES
Track your expenses in a simple way. I basically made 90s looking Excel VBA-whatever to log your expenses on the fly.
What is the purpose of such application when countless other, 1000x better projects exist? 
I can open a bookmark on my iConsumer smartphone, spend 30s adding info and snap a picture of that spicy toilet paper with detailed log of my purchases before throwing it away. That data will be stored on my personal server, will be analyzed with my queries and stored in my basement.

### FEATURES
1. You own your data.
2. Possibility to do some personal analytics.
3. Shame yourself for wasting cash.
4. Upload your PDF or take a picture of the Kassenbohn for later OCR/whatever.

### ANTI-FEATURES
1. € is the only currency.
2. Want a new country? Need to make a pull request. Not in Eurozone? Sad emoji.
3. One image and document per expense. (Should be fixed in the future.)

## IAFE.JOURNAL
Coming soon...

### FEATURES
1. Will beat creating today.txt or giving up your depression log to Goomazonbook dudes.

### ANTI-FEATURES
1. Does not exist yet.

## INSTALL
### MANUAL DEV
1. `make setup`
2. Change `ALLOWED_HOSTS` LAN address to your ipv4 address. Exposes IAFE to LAN, allows testing on other devices or just running it locally as production :^)
2. `make run`


### MANUAL PRODUCTION
1. TODO pipenv things with stuff like `pipenv run make run`
1. If you want to run it as production, move settings_dev.py to settings.py in website/. Do not forget to generate a secure key and change domain. Also migrate and create superuser...

2. You also need to configure NGINX as reverse proxy and also handle static files.
Do not forget to change server_name, proxy_set_header and alias. Then you should setup https. Easiest way is to use certbot for nginx. You can install it with `sudo pip3 install certbot` to have it globally. Launch it as `sudo certbot --nginx` and follow the steps given by certbot itself.
Example configuration below
    ```nginx
    server {
    
            server_name iafe.example.org www.iafe.example.org;
            location / {
                    proxy_pass http://localhost:8000;
                    proxy_set_header Host iafe.example.org;
                    proxy_set_header X-FORWARDED-PROTO https;
            }
    
            location /static {
                autoindex on;
                alias <your-path>/iafe/static/;
            }
    }
    ```
1. Do not forget to backup your database frequently!

## ROADMAP FEATURES
- [ ] merge scrappers from lil_spy into journal application, see daily stats from Firefox, Chromium, Discord, LastFM and etc.
- [ ] docker-compose and Dockerfile for app releases.
- [ ] map to see red points where you spent cash -> django mapbox
- [ ] survey creator for custom journal/survey which you can fill out daily
- [x] nginx reverse proxy for production
- [ ] cronjob example for db/staticfiles backups to b2
- [ ] improve makefile to handle complete setup for production!