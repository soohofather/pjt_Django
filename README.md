# 개인프로젝트

### 1. 개발환경

- 리드미 파일 생성
    - touch README.md
- 깃 이그노어 생성
    - touch .gitignore
    - .txt를 붙이니 인식이 안되었음
    - https://www.toptal.com/developers/gitignore
    - python, Django, windows, MACOS, VScode
- 가상환경 설치 및 실행
    - python -m venv venv
    - source venv/scrirpt/activate
- pip 설치
    - pip install
    - django==3.2.13
    - django-bootstrap5
    - black
- pip 설치 목록 텍스트 파일로 저장    
    - pip freeze > requirements.txt
- 프로젝트 시작
    - django-admin startproject pjt_django
- 리뷰 앱 만들기 시작
    - django-admin startapp reviews
    - 첫 페이지(index.html)
    - 글 쓰기 페이지(create.html) - CREATE
    - index에 글 내용 보이게하기 - READ
    - 글 삭제 - DELETE
    - 글 수정 - UPDATE
- 회원가입 앱(accounts) 만들기 시작
    - 회원가입 페이지
    - 로그인 페이지
    - 로그아웃 기능
    - 회원정보 페이지 (로그인시만 접근가능)
    - 로그인이면 네브바 회원정보, 로그아웃, user정보
    - 로그인중 아니면 네브바 회원가입
    - 비밀번호 변경, 완료 후 인덱스 페이지로
    - 회원탈퇴 기능
    - 각 글에 글쓴이 기능 (로그인 한사람만 글쓰기)
- 댓글기능 


