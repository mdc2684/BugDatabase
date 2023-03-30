# BugDatabase Repository
# 23조 토이프로젝트(2022.03.27~)

# 1. 프로젝트 명

버그 데이터베이스(Bug Database)

# 2. 소개

- 개발 중 발견한 버그를 작성해 저장하고 공유하는 게시판 커뮤니티 서비스
- 프로젝트 선정 이유 : 개발을 하는 우리가 실제로 유용하게 사용할 수 있는 서비스가 없을까 고민했고, 버그 추적 시스템이 간단하게 만든다면 현재 우리가 알고 있는 기술 스택으로도 충분히 만들 수 있을 거라고 생각이 들어서 선정했습니다.

# 3. 와이어 프레임

### 1) Login
<img width="743" alt="login_page" src="https://user-images.githubusercontent.com/111736036/228819763-b137e407-12e8-47cc-a13f-bcde3d3db54c.png">

### 2) Register
<img width="990" alt="Register_page" src="https://user-images.githubusercontent.com/111736036/228819838-46af719b-80f7-4d10-9b72-96c8a3e05a4d.png">

### 3) Main
<img width="990" alt="Register_page" src="https://user-images.githubusercontent.com/111736036/228819891-809ef76c-eb5e-46c9-bb3e-3926c6142552.png">


# 4. 개발해야 하는 기능들
<img width="967" alt="스크린샷 2023-03-30 오후 8 19 18" src="https://user-images.githubusercontent.com/111736036/228820209-a60857f7-1e2e-48b5-b3b4-7fad50e90ab0.png">


# 5. public Github repo

[https://github.com/mdc2684/BugDatabase](https://github.com/mdc2684/BugDatabase)

## 6. 영상 시연:

[항해99 14기 23조 토이 프로젝트 영상](https://youtu.be/OlAYpqw7iqk)

## 7. AWS 배포:

[버그 데이터베이스](http://bugdatabase.eba-648gegev.ap-northeast-2.elasticbeanstalk.com/)

# 8. KPT

---

## Keep

- API의 기능의 한계에 부딪혔을 때 새로운 로직으로 다시 갈아엎어서 새로운 기능들을 구현할 수 있는 집념이 있었다.
- 서로 만든 기능들을 모두가 테스트해서 진행자가 알아차리지 못한 버그를 알려주고 고쳐나갔다.
- Deadline을 지킬 수 있도록 하루일과 전, 후 2번 고정 미팅을 통해 현재의 상황을 브리핑하였다.
    - Notion에서 우선순위를 정하며 완성에 초점을 두었다.
- 협업 분위기
    - 팀 분위기가 좋아 모두 이번 프로젝트를 즐겼다. 새로운 기능 추가에 대한 의견들을 자유롭게 낼 수 있었다.

## Problem

- MyPage 기능 필요하다고 느꼈다.
- 스크립트공격 막기 ( 정규표현식을 이용한 XSS우회기법 )
- JWT를 이용한 회원가입
- 버그를 뒤늦게 발견해서 급하게 고친점이 제대로 못고친 것도 있고 해서 아쉬웠다.
- 버그 추적장치를 사용할 때 어떻게 하면 더 유용하게 사용할 수 있을지 고민해서 기능을 고도화시키면 좋을 것 같은데 그 과정을 하지 못해서 아쉬웠다.
- 데이터베이스에 넣는 데이터도 실제로 개발하면서 발생한 버그를 입력하고 싶었는데 테스트 용 데이터를 많이 채웠던 것 같다.
- 회원가입 시, 비밀번호 입력을 실수했을때 막을 수 없어 아쉬웠다. ( 비밀번호 확인 기능 필요)
- 버그의 카테고리를 서비스에서 정해놓은 것만 선택하는 게 아니라 입력하는 사람이 직접 만들어서 적을 수 있게 해야 좋을 것 같다.

## Try

- 기능 하나하나 만들때마다 여러가지 테스트를 바로바로 해봐야겠다.
- Mypage에서 이미지로 프로필을 변경하고자 할 때 이미지 파일을 업로드하는 방법보다 Link를 이용하는 방법도 있다.
- XSS 공격을 막기 위해 입력 값 제한이나 치환을 통해 <script>등의 태그를 막아야 한다.
- 회원가입 시, 비밀번호 체크 기능을 만들어야겠다.
- 기획과 관련해서 ‘왜?’ 라는 질문을 많이 했으면 좋았을 것 같다.
