## 🎨 DIY! (실제 구동하는 서버입니다)
http://ec2-3-34-98-144.ap-northeast-2.compute.amazonaws.com:5000/

## Swagger로 API 정리
http://ec2-3-34-98-144.ap-northeast-2.compute.amazonaws.com:5000/apidocs/
* 수정이 필요한 부분: Http Method Delete와 Put(Update)를 제대로 적용시키지 못함

## 예시 실행 화면

https://user-images.githubusercontent.com/91591854/143060495-b6832933-68e0-42ca-9c83-0d03b4a2d63c.mp4




## 1. 과제정의

```
- 이메일과 비밀번호 입력을 통해서 회원 가입: register()
  이메일 형식 validation: check()
  이메일 주소 중복검사
  비밀번호는 암호화 한다.
  이메일과 비밀번호는 반드시 입력해야한다.: login()
  + 추가적으로 해볼 수 있는 모듈: JWT로 access token을 발급하는 방법

- 로그인과 로그아웃: login(), logout()
  이메일과 비밀번호 validation error를 보여준다.
  로그인 시 세션에 login True 값을 넣어 이후 login validation에 사용한다.

- 돈의 금액과 관련된 메모를 남기기: create()
  제목과 금액은 Not Null 해야한다.
  금액은 numeric한 값만 받는다.
  상세내역은 Null한 값도 받는다.

- 금액과 메모를 수정: update(id)

- 가계부에서 삭제: delete(id)
  삭제한 내역은 deleted 컬럼 값을 0에서 1로 바꾼다

- 삭제 내역 복구
  삭제한 내역을 복구하기에서 전체를 보여준다.: rollbacklist()
  삭제한 내역의 deleted 컬럼 값을 1에서 0로 바꾼다: rollback(id)

- 가계부 리스트, 상세한 세부 내역:
  유저가 작성한 글 중 deleted 칼럼 값이 0인 내용 전체를 보여준다.: index()
  로그인 하지 않은 유저가 '/'에 접근하는 경우 auth.login으로 redirect한다.

- 로그인하지 않은 고객 접근 제한 처리
  @login_required 데코레이터를 만들어서 로그인을 해야하는 서비스에 적용한다.

- Docker를 기반으로 서버를 실행
- DDL 파일을 소스: apps/model/payhere.sql
- 테스트 케이스:
  pytest로 auth 테스트
```


## 2. 사용한 기술

```
Flask
mysql:5.7 (AWS RDS)
Docker
Swagger
JINJA2
```


## 3. 배포, 실행

```
도커: 
$ docker pull ej00923/payhere_homework
이후 브라우저 localhost:{포트번호} 로 접근

깃헙:

$ git clone https://github.com/erie0210/payhere
$ cd payhere
$ pip install -r requirements.txt
$ python -m venv venv
$ source venv/Scripts/activate
$ export FLASK_APP=apps
$ export FLASK_ENV=development
$ flask run
```


## 4. DB-erd

* FK로 연결해 이후 유저정보를 더 반영할 필요가 있을 경우 사용한다.
* create 정보를 이용해 날짜를 확인할 수 있게 한다.
* author_id로 작성한 유저에 따라 다른 내역을 보여준다.
* 상세내용을 적을 수 있는 Body를 제외한 다른 경우는 모두 길이 제한.
* Body는 Null한 값을 허용한다.
* deleted 컬럼을 이용해 복구 기능을 만든다.

```
CREATE TABLE user (
  id INTEGER(11) PRIMARY KEY AUTOINCREMENT,
  email VARCHAR(100) UNIQUE NOT NULL,
  password VARCHAR(100) NOT NULL
);

CREATE TABLE post (
  id INTEGER(11) PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER(11) NOT NULL,
  amount INTEGER(11) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title VARCHAR(32) NOT NULL,
  body TEXT,
  deleted INTEGER(11),
  FOREIGN KEY (author_id) REFERENCES user (id)
);
```









