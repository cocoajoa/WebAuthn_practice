from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from .models import WebUser

from webauthn import (
    generate_registration_options,
    verify_registration_response,
    generate_authentication_options,
    verify_authentication_response,
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
    # 기존 있는 유저는 못만들게
    if WebUser.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=400)
    else:
        options = generate_registration_options(
        rp_id= 'localhost',
        rp_name= 'cocoajoa',
        user_name= username,
        )
        return Response(options_to_json(options))

@api_view(['POST'])
def RegisterCompleteView(request):
    username = request.data.get('username')
    credential = request.data.get('attestationResponse')
    origin_challenge = request.data.get('originChallenge')
    
    registration_verification = verify_registration_response(
        credential= credential,
        expected_challenge= base64url_to_bytes(origin_challenge),
        expected_rp_id= 'localhost',
        expected_origin= 'http://localhost:5173',
        require_user_verification=True,
    )
    # registration_verification이 맞다면 DB에 username과 같이 DB에 저장함, 그리고 잘갔다고 보내주기
    if registration_verification:
        user = WebUser.objects.create(username=username)
        user.credential_id = registration_verification.credential_id
        user.credential_public_key = registration_verification.credential_public_key
        user.sign_count = registration_verification.sign_count
        user.save()
        return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)
    # registration_verification이 틀리다고 말하면 오류뜬다고 보내주기
    else:
        return Response({'message': 'Registration failed'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def LoginBeginView(request):
    username = request.data.get('username')
    if WebUser.objects.filter(username=username).exists():
        user = WebUser.objects.get(username=username)
        authentication_options= generate_authentication_options(
            rp_id= 'localhost',
            allow_credentials=[PublicKeyCredentialDescriptor(id=user.credential_id)],
        )
        return Response(options_to_json(authentication_options))
    else:
        return Response({'message': '그런 유저 없어요'}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST'])
def LoginCompleteView(request):
    username = request.data.get('username')
    credential = request.data.get('assertionResponse')
    origin_challenge = request.data.get('originChallenge')
    user = WebUser.objects.get(username=username)
    login_verification= verify_authentication_response(
        credential= credential,
        expected_challenge= base64url_to_bytes(origin_challenge),
        expected_rp_id= 'localhost',
        expected_origin= 'http://localhost:5173',
        credential_public_key= user.credential_public_key,
        credential_current_sign_count= 0,
        require_user_verification=True,
    )
    if login_verification:
        # JWT 토큰 발급
        refresh = RefreshToken.for_user(user)

        # AccessToken과 RefreshToken을 JSON 형태로 응답
        return Response({
            'message': 'login successful',
            'username': username,
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
        }, status=status.HTTP_201_CREATED)
    else:
        return Response({'message': 'login failed'}, status=status.HTTP_400_BAD_REQUEST)


