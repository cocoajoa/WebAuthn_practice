from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import WebUser
from .serializers import WebUserSerializer

from webauthn import (
    generate_registration_options,
    verify_registration_response,
    options_to_json,
    base64url_to_bytes, 
)
from webauthn.helpers.structs import (
    PublicKeyCredentialDescriptor,
    UserVerificationRequirement,
)


@api_view(['POST'])
def RegisterBeginView(request):
    username = request.data.get('username')
    options = generate_registration_options(
    rp_id= 'localhost',
    rp_name= 'cocoajoa',
    user_name= username,
)
    return Response(options_to_json(options))


def RegisterCompleteView():
    pass

def LoginBeginView():
    pass
def LoginCompleteView():
    pass
