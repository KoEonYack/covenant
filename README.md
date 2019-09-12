# Covenant - 정직한 교육이 세상을 바꿉니다.
------------

### 일정
- 개발 기간: 2017년 7월 20일 ~ 2017년 8월 14일
- 서비스 발표: 2017년 9월 
- 서비스 운영기간:2017년 10월 1일 ~ 2017년 12월 20일
- 서비스 대상: 2017년 2학기 파이썬 튜터세션을 이용하는 학생  


### 프로젝트 내용
 Covenant는 한동대학교 TA가 학생들에게 강의을 제공하는 강의 플랫폼입니다. 두 가지 문제 의식으로 만들었습니다. 현재 한동대학교 TA는 극히 일부만 TA세션 녹화를 하고, TA세션에 참석하는 학우들만 TA의 설명을 들을 수 있었습니다. 또한 교수님께서 Pizza같은 타 사이트 질문 게시판을 운영하지 않는 경우에는 TA에게 직접 메일을 보내서 질문 사항을 해결하곤 했습니다. 이는 다른 학우들과 질문내용이 공유 되지 않으며, 답변을 위해서 TA가 일일이 메일을 확인하여 답을 해야 하는 문제점이 있었습니다. 

 이 두 가지 문재를 해결 하기 위해서 YouTube에 TA가 강의를 올리고, 본 홈페이지에 강의를 올릴수가 있습니다. 또한 질문계시판을 만들어 수강생의 질문이 다른 학우들과 질문이 공유 될 수 있게 하였으며, 수업 수강생도 덧글을 달 수 있게 해서 서로 질문을 공유하고, 토의하며 답을 구하는 서비스를 제공하였습니다. 질문 게시판에 DISCUSSION 댓글 서비스를 이용하여 댓글에서도 사진 첨부가 가능합니다. 이를 통해 자세한 답변을 할 수있게 만들었습니다.


### 구현 결과

![main](https://github.com/KoEonYack/covenant/blob/master/img/main.png)
- Covenant를 소개하는 메인페이지입니다. 


![lectureList](https://github.com/KoEonYack/covenant/blob/master/img/lecturelist.png)
- 강의 목록을 확인할 수 있는 페이지입니다. 


![login](https://github.com/KoEonYack/covenant/blob/master/img/login.png)
- 로그인 페이지입니다.


![profile]](https://github.com/KoEonYack/covenant/blob/master/img/profile.png)
- 유저의 프로필 정보를 볼 수 있는 페이지입니다. 


![question](https://github.com/KoEonYack/covenant/blob/master/img/question.png)
- 질문을 올릴 수 있는 페이지입니다. 



### 향후 계발 계획
- 지금은 TA가 강의를 제공하고, 수강생들이 서로 질문과 답변을 하는 강의 플랫폼이지만 차후 다음과 같은 방향으로 발전시킬 것입니다.

**1) 모두가 가르치고 배우는 사이트**

**2) 한동 TED : 배워서 남주는 교육**
   한동의 기본 가치인 Study for others, 배워서 남주는 가치를 실현하기를 바랍니다. 이러한 가치는 온라인에서 이루기 쉬워진다고 생각합니다. 누구나 공간의 제약 없이 배움의 기회를 얻을 수 있는 사이트가 될 것입니다. 

### 디자인 철학
- 한동대학교의 색깔인 파란색 계열을 사용했습니다. 그리고 깔끔함을 주기 위해서 옅은 회색을 메뉴바로 깔끔함을 주었습니다. 


### 사용 기술
- HTML5 CSS, Bootstrap(3.4ver), JavaScript, 
    *  전반적인 프론트 영역은 부트스트랩을 이용하여 디자인 하였습니다.
- Django(1.10ver)
- SQLiite
    *  Django를 사용하여 백의 토대를 만들었습니다. 기본적인 함수형 뷰로 제작하였습니다. 모든 DB를 Django에서 기본 제공하는 SQLite를 사용하였습니다. 다중 사용자에 SQLite는 안정적이지 못하여 향후 문제가 생길 경우 MySQL로 변경할 계획입니다. 
- amazonAWS EC2, apache2
    * amazonAWS EC2에 apache2와 django를 연결하여 서버를 구축하였습니다. 성능 면이 부족하지만 일단 무료라는 점에서 초기 사이트 운영시에 적합하다고 생각하여 이렇게 구성하였습니다.  