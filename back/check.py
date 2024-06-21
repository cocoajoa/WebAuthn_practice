## webauthn 라이브러리 테스트 용도

from webauthn import (
    generate_registration_options,
    verify_registration_response,
    options_to_json,
    base64url_to_bytes, 
)
from webauthn.helpers.cose import COSEAlgorithmIdentifier
from webauthn.helpers.structs import (
    AttestationConveyancePreference,
    AuthenticatorAttachment,
    AuthenticatorSelectionCriteria,
    PublicKeyCredentialDescriptor,
    ResidentKeyRequirement,
)



wanted = generate_registration_options(
    rp_id= 'cocoajoa.com',
    rp_name= 'cocoajoa',
    user_name= 'lee',
)
from pprint import pprint

op = options_to_json(wanted)
# pprint(wanted)


# print(base64url_to_bytes('zdOJ-YrjWQySmvecCUZ2b1VyqCEGdfku-MDNoldmU6OtSIyE4AHLHOKwo2r6-qCD8ukG8ujObCuTDjxPW18Naw'))
expected_challenge=base64url_to_bytes(
        "CeTWogmg0cchuiYuFrv8DXXdMZSIQRVZJOga_xayVVEcBj0Cw3y73yhD4FkGSe-RrP6hPJJAIm3LVien4hXELg"
    ),
expected_origin="http://localhost:5000"
expected_rp_id="localhost"
require_user_verification=True
expected= {
    'id': 'NhSZEM3wJ9trpnKsIKnf6bWMN00', 
    'rawId': 'NhSZEM3wJ9trpnKsIKnf6bWMN00', 
    'response': 
        {'attestationObject': 'o2NmbXRkbm9uZWdhdHRTdG10oGhhdXRoRGF0YViYSZYN5YgOjGh0NBcPZHZgW4_krrmihjLHmVzzuoMdl2NdAAAAAPv8MAcVTk7MjAtuAgVX170AFDYUmRDN8Cfba6ZyrCCp3-m1jDdNpQECAyYgASFYIODuOn9c7KrTbWvnsF-RXcbAIi8GRuOexd7Zr365BG23Ilggr9QZP1tZYSZIHf6tMEIFdkXOlvvHWZjtISzYKXMiqk8', 
            'clientDataJSON': 'eyJ0eXBlIjoid2ViYXV0aG4uY3JlYXRlIiwiY2hhbGxlbmdlIjoiQllPQno4RUx1M1V6ZjVtUnpqUG80V2RlVjZxVE5uYTYtY1ZRRU55bE1TSVBXV2U0ejVZNEpPRjNicHBxQjZMMVRKNXVodE92TVd3dXRKdFZDX1BDcHciLCJvcmlnaW4iOiJodHRwOi8vbG9jYWxob3N0OjUxNzMiLCJjcm9zc09yaWdpbiI6ZmFsc2V9',
            },
    "type": "public-key",

}
registration_verification = verify_registration_response(credential=expected, expected_challenge= expected_challenge, expected_origin=expected_origin, expected_rp_id=expected_rp_id,)
print(registration_verification)