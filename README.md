# WebAuthn_practice(미완성 회원가입 1단계까지만) (회원가입 2단계, 로그인 2단계, 총 4단계)
패스키 찍먹

# 시용 라이브러리 (requirements.txt 참고)
- django
- webauthn (https://github.com/duo-labs/py_webauthn)

## webauthn 라이브러리를 쓴 이유
- 내가 찾아본 django에서 쓸 수 있는 webauthn 라이브러리 중 제일 fork 수가 많았다.
- 실제 웹페이지에서 체험이 가능해서 좋았다. (https://webauthn.io)

## how to install and setup
1. python -m venv venv
- 가상환경 설치

2. source venv/bin/activate(mac), source venv/scripts/activate(window)
- 가상환경 실행

3. pip install requirements
- django, djangorestframework, django-cors-headers, 그리고 [webauthn](https://github.com/duo-labs/py_webauthn/tree/master) 설치한 것들임

4. (백엔드) cd back, python manage.py migrate, python manage.py runserver
-  장고 돌릴 준비

5. (프론트엔드) cd front, npm install, npm run dev
- vue 실행

6. vue 로컬 서버로 회원가입, 로그인해보기

## 하면서 막혔던 부분들
### 장고
1. 파이썬 webauthn 라이브러리 generate_registration_options 매개변수인 rp_id는 임의로 짓는게 아님
    - 실제 브라우저 주소를 적어야 [MDN webauthn API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Authentication_API#examples)의 navigator.credentials.create()함수가 통과시켜준다. 
    - console.log(error) 내용
      ```
      DOMException: The relying party ID is not a registrable domain suffix of, nor equal to the current domain.
      ```

### vue
1. 받아오긴 json 형태로 받아오는데 navigator.credentials.create() 실행이 안됨..(두 가지 원인)
    - 파이썬 webauthn 라이브러리 generate_registration_options는 아주 친절하게 challenge와 user_id를 base64url로 인코딩해줌(create()에서 array버퍼형태로 받음) 그래서 뷰에서 그 부분은 디코딩 필요
    - 받아온 json 파싱을 안해서 ㅎ..
    - console.log(error) 내용
      ```
      TypeError: Failed to execute 'create' on 'CredentialsContainer': Failed to read the 'publicKey' property from 'CredentialCreationOptions': The provided value is not of type 'PublicKeyCredentialCreationOptions'.
      ```
