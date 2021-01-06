# I ALWAYS FORGET EVERYTHING
![iafe](iafe.png)

application bundle to manage my **adult** life. most of us know that budgeting and tracking expenses helps to manage €€€, but not many do it. **iafe.expenses** allows easy and consistent tracking after you set your payments/locations/labels up. 

future extensions:

**iafe.journal** will allow you to create daily notes and upload files that you want to remember. one textarea and unlimited file uploads per day. reminders are sent to your email. see what you did a year ago and track your boring existence via buggy django project. 

**iafe.spyware** will collect data from various 3rd party services like last.fm, wakatime, telegram, discord, activitywatch and even your firefox/chromium browser to collect that sweet data. if it is generated, why not scrape and store it for yourself? looking at graphs and looking up your browser history seems sane. many of the scrapers are already created in my previous attempts at data collection from data collection services. stay tuned.

## IAFE.EXPENSES
track your expenses in a simple way. i basically made 90s looking excel-vba-whatever to log your expenses on the fly.
you can open a bookmark on i-consumer smartphone, spend 30s adding info and snap a picture of that spicy toilet paper with detailed log of your purchases before throwing it away. all that useful data will be stored on your personal server. 

how dows it compare to other services?
### ADVANTAGES
1. you own your data.
2. possibility to do some personal analytics with your 🔥hardcoded sql queries🔥.
3. shame yourself for wasting cash.
4. upload your pdf or take a picture of the kassenbohn for later ocr/whatever parsing.

### DISADVANTAGES
1. € is the only currency.
2. hardcoded countries and timezones.
3. have to add payment/location/label before you can use it in expense... inline-formset is a new field for me.


---

## INSTALL
### MANUAL DEV
make sure you have `pipenv` installed.
1. `make setup`
2. change `ALLOWED_HOSTS` lan address to your ipv4 address. this exposes it to lan and you can test iafe on your i-consumer smartphone.


### MANUAL PRODUCTION
1. todo pipenv things with stuff like `pipenv run make run`
1. if you want to run it as production, rename `settings_dev.py` to `settings.py` in website/. **do not forget to generate a secure key, change domain to yours, makemigrations/migrate, create superuser...**

2. configure nginx as reverse proxy and also handle static files.
do not forget to change `server_name`, `proxy_set_header` and `alias`. then you should setup https. the easiest way is to use certbot for nginx. you can install it with `sudo pip3 install certbot` to have it globally. launch it as `sudo certbot --nginx` and follow the steps given by certbot itself.
example configuration below
    ```nginx
    server {
    
            # change me
            server_name iafe.example.org www.iafe.example.org;
            location / {
                    proxy_pass http://localhost:8000;
                    # change me
                    proxy_set_header Host iafe.example.org;
                    proxy_set_header X-FORWARDED-PROTO https;
            }
    
            location /static {
                autoindex on;
                # change me
                alias <your-path>/iafe/static/;
            }
    }
    ```
1. *do not forget to back up your database frequently!*

---

## TODO
check out [todo](todo) for *comming soon tm* features 🥰
