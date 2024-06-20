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
pprint(wanted)


print(base64url_to_bytes('zdOJ-YrjWQySmvecCUZ2b1VyqCEGdfku-MDNoldmU6OtSIyE4AHLHOKwo2r6-qCD8ukG8ujObCuTDjxPW18Naw'))