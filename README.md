<!-- ## ๐จ DIY! (์ค์  ๊ตฌ๋ํ๋ ์๋ฒ์๋๋ค)
http://ec2-3-34-98-144.ap-northeast-2.compute.amazonaws.com:5000/ -->

## Swagger๋ก API ์ ๋ฆฌ
ec2-54-180-105-148.ap-northeast-2.compute.amazonaws.com:5000/apidocs/
* ์์ ์ด ํ์ํ ๋ถ๋ถ: Http Method Delete์ Put(Update)๋ฅผ ์ ๋๋ก ์ ์ฉ์ํค์ง ๋ชปํจ

## ์์ ์คํ ํ๋ฉด

https://user-images.githubusercontent.com/91591854/143060495-b6832933-68e0-42ca-9c83-0d03b4a2d63c.mp4




## 1. 

```
- ์ด๋ฉ์ผ๊ณผ ๋น๋ฐ๋ฒํธ ์๋ ฅ์ ํตํด์ ํ์ ๊ฐ์: register()
  ์ด๋ฉ์ผ ํ์ validation: check()
  ์ด๋ฉ์ผ ์ฃผ์ ์ค๋ณต๊ฒ์ฌ
  ๋น๋ฐ๋ฒํธ๋ ์ํธํ ํ๋ค.
  ์ด๋ฉ์ผ๊ณผ ๋น๋ฐ๋ฒํธ๋ ๋ฐ๋์ ์๋ ฅํด์ผํ๋ค.: login()
  + ์ถ๊ฐ์ ์ผ๋ก ํด๋ณผ ์ ์๋ ๋ชจ๋: JWT๋ก access token์ ๋ฐ๊ธํ๋ ๋ฐฉ๋ฒ

- ๋ก๊ทธ์ธ๊ณผ ๋ก๊ทธ์์: login(), logout()
  ์ด๋ฉ์ผ๊ณผ ๋น๋ฐ๋ฒํธ validation error๋ฅผ ๋ณด์ฌ์ค๋ค.
  ๋ก๊ทธ์ธ ์ ์ธ์์ login True ๊ฐ์ ๋ฃ์ด ์ดํ login validation์ ์ฌ์ฉํ๋ค.

- ๋์ ๊ธ์ก๊ณผ ๊ด๋ จ๋ ๋ฉ๋ชจ๋ฅผ ๋จ๊ธฐ๊ธฐ: create()
  ์ ๋ชฉ๊ณผ ๊ธ์ก์ Not Null ํด์ผํ๋ค.
  ๊ธ์ก์ numericํ ๊ฐ๋ง ๋ฐ๋๋ค.
  ์์ธ๋ด์ญ์ Nullํ ๊ฐ๋ ๋ฐ๋๋ค.

- ๊ธ์ก๊ณผ ๋ฉ๋ชจ๋ฅผ ์์ : update(id)

- ๊ฐ๊ณ๋ถ์์ ์ญ์ : delete(id)
  ์ญ์ ํ ๋ด์ญ์ deleted ์ปฌ๋ผ ๊ฐ์ 0์์ 1๋ก ๋ฐ๊พผ๋ค

- ์ญ์  ๋ด์ญ ๋ณต๊ตฌ
  ์ญ์ ํ ๋ด์ญ์ ๋ณต๊ตฌํ๊ธฐ์์ ์ ์ฒด๋ฅผ ๋ณด์ฌ์ค๋ค.: rollbacklist()
  ์ญ์ ํ ๋ด์ญ์ deleted ์ปฌ๋ผ ๊ฐ์ 1์์ 0๋ก ๋ฐ๊พผ๋ค: rollback(id)

- ๊ฐ๊ณ๋ถ ๋ฆฌ์คํธ, ์์ธํ ์ธ๋ถ ๋ด์ญ:
  ์ ์ ๊ฐ ์์ฑํ ๊ธ ์ค deleted ์นผ๋ผ ๊ฐ์ด 0์ธ ๋ด์ฉ ์ ์ฒด๋ฅผ ๋ณด์ฌ์ค๋ค.: index()
  ๋ก๊ทธ์ธ ํ์ง ์์ ์ ์ ๊ฐ '/'์ ์ ๊ทผํ๋ ๊ฒฝ์ฐ auth.login์ผ๋ก redirectํ๋ค.

- ๋ก๊ทธ์ธํ์ง ์์ ๊ณ ๊ฐ ์ ๊ทผ ์ ํ ์ฒ๋ฆฌ
  @login_required ๋ฐ์ฝ๋ ์ดํฐ๋ฅผ ๋ง๋ค์ด์ ๋ก๊ทธ์ธ์ ํด์ผํ๋ ์๋น์ค์ ์ ์ฉํ๋ค.

- Docker๋ฅผ ๊ธฐ๋ฐ์ผ๋ก ์๋ฒ๋ฅผ ์คํ
- DDL ํ์ผ์ ์์ค: apps/model/payhere.sql
- ํ์คํธ ์ผ์ด์ค:
  pytest๋ก auth ํ์คํธ
```


## 2. ์ฌ์ฉํ ๊ธฐ์ 

```
Flask
mysql:5.7 (AWS RDS)
Docker
Swagger
JINJA2
```


## 3. ๋ฐฐํฌ, ์คํ

```
๋์ปค: 
$ docker pull ej00923/payhere_homework
์ดํ ๋ธ๋ผ์ฐ์  localhost:{ํฌํธ๋ฒํธ} ๋ก ์ ๊ทผ

๊นํ:

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

* FK๋ก ์ฐ๊ฒฐํด ์ดํ ์ ์ ์ ๋ณด๋ฅผ ๋ ๋ฐ์ํ  ํ์๊ฐ ์์ ๊ฒฝ์ฐ ์ฌ์ฉํ๋ค.
* create ์ ๋ณด๋ฅผ ์ด์ฉํด ๋ ์ง๋ฅผ ํ์ธํ  ์ ์๊ฒ ํ๋ค.
* author_id๋ก ์์ฑํ ์ ์ ์ ๋ฐ๋ผ ๋ค๋ฅธ ๋ด์ญ์ ๋ณด์ฌ์ค๋ค.
* ์์ธ๋ด์ฉ์ ์ ์ ์ ์๋ Body๋ฅผ ์ ์ธํ ๋ค๋ฅธ ๊ฒฝ์ฐ๋ ๋ชจ๋ ๊ธธ์ด ์ ํ.
* Body๋ Nullํ ๊ฐ์ ํ์ฉํ๋ค.
* deleted ์ปฌ๋ผ์ ์ด์ฉํด ๋ณต๊ตฌ ๊ธฐ๋ฅ์ ๋ง๋ ๋ค.

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









