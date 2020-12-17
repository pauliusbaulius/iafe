# IAFE
**I Always Forget Everything**

Application to log imporatant metadata of my existence. Expenses? Essential to track your finances, this makes it quick, which increases the probability of me using it daily. Journal? Nag me to log my mood and thoughts. Doing it on paper lasts a week. Clicking on happy/sad/angry emoji? Can do.

### TECHNOLOGY


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

### DOCKER
1. Someone pls make docker-config.yml with proper permissions.
2. `docker-compose up --build -d`

## ROADMAP FEATURES
- [ ] merge scrappers from lil_spy into journal application, see daily stats from Firefox, Chromium, Discord, LastFM and etc.
- [ ] docker-compose and Dockerfile for app releases.
- [ ] map to see red points where you spent cash
- [ ] survey creator for custom journal/survey which you can fill out daily
- [ ] email reminder to fill out journal
- [ ] nginx reverse proxy for production
- [ ] migrate to postgre