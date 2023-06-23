# fin-app

To help personal finance.


## Create `.env` file

**[required]** Add _FOREX_API_KEY_ from [provider](https://apilayer.com/marketplace/exchangerates_data-api) into `.env` file
  
```.env
FOREX_API_KEY="<your_key>"
```

## Usage
```
python3 -m pip install -r requirements.txt
sh migration.sh
python3 manage.py runserver   
```
