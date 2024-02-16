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

# To solve Error 400: redirect_uri_mismatch[ Add  url accordingly]
- Dont forget to add "Authorized JavaScript origins" in [Link](https://console.cloud.google.com/apis/credentials/) 
```
http://127.0.0.1:8000
```
- Also add "Authorized redirect URI"s in google console
```
http://127.0.0.1:8000
http://127.0.0.1:8000/oidc/callback/
http://127.0.0.1:8000/accounts/user-infor/
```
## Authentication flow: 
- Login with endpoint http://127.0.0.1:8000/oidc/authenticate/. This will trigger google authentication
- After google authentication was successful, Google will hit the callback endpoint "http://127.0.0.1:8000/oidc/callback/",  then afterwards, will redirect the user to http://127.0.0.1:8000/accounts/user-infor/, where we have defined the logic for creating the user,