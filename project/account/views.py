from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Customer
from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import serialize_user
from rest_framework.renderers import JSONRenderer
import json
from mozilla_django_oidc.auth import OIDCAuthenticationBackend

# views.py
from django.views import View
from mozilla_django_oidc.views import OIDCAuthenticationRequestView

class OIDCLoginView(OIDCAuthenticationRequestView):
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)

        # If the user is authenticated, store the data in the database
        if request.user.is_authenticated:
            user = request.user
            # Check if a Customer instance already exists for this user
            customer, created = Customer.objects.get_or_create(user=user)

            # If the user is authenticated, store the data in the database
            customer.save()

            serialized_user = serialize_user(user)
            # return Response(data=serialized_user)
            
            # Convert the serialized_user to JSON
            json_data = json.dumps(serialized_user)
            
            # Return an HttpResponse with JSON content
            return HttpResponse(json_data, content_type='application/json')

        return response

class MyOIDCAB(OIDCAuthenticationBackend):
    def create_user(self, claims):
        user = super(MyOIDCAB, self).create_user(claims)

        user.first_name = claims.get('given_name', '')
        user.last_name = claims.get('family_name', '')
        user.save()

        return user

    def update_user(self, user, claims):
        user.first_name = claims.get('given_name', '')
        user.last_name = claims.get('family_name', '')
        user.save()
    
    def get(user, claims):
        given_name = claims.get('given_name', '')
        serialized_user = serialize_user(user)
        
        # Convert the serialized_user to JSON
        json_data = json.dumps(serialized_user)
        return HttpResponse(json_data, content_type='application/json')



class CustomLogoutView(View):
    def get(self, request, *args, **kwargs):

        # Redirect to the OIDC logout endpoint
        return redirect('oidc_logout')
