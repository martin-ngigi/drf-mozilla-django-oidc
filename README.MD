## INSTALLATIONS
```
pip install django
pip install djangorestframework
pip install djangorestframework-simplejwt
pip install python-dotenv
pip install mozilla-django-oidc
pip install mysql-connector-python
```

- Link: 
- [Github](https://www.youtube.com/watch?v=d7OxfJZOIhQ&t=10s)
- [Youtube](https://github.com/CryceTruly/incomeexpensesapi)

- Enable Google credentials
- [Link](https://console.cloud.google.com/apis/credentials/consent?project=social-authentiaction)

- Create Meta App for facebook
- [Link](https://developers.facebook.com/apps)

- Twitter
- [Link](https://developer.twitter.com/en/portal/apps)

- Run server
```
source .venv/bin/activate
cd project
python3 manage.py runserver
```

- Run migration
```
source .venv/bin/activate
cd project
python3 manage.py makemigrations
python3 manage.py migrate
```

## Generating keys
- generate a private and public key pair using the following command:
```
openssl genrsa -out private_key.pem 2048
openssl rsa -in private_key.pem -outform PEM -pubout -out public_key.pem
```
