# -*- coding: utf-8 -*-
from flask import ( Blueprint, flash, redirect, render_template, request, url_for, session )
from werkzeug.exceptions import abort
from . import auth
from apps.model import model
import datetime

bp = Blueprint('balance', __name__)

@bp.route('/')
@auth.login_required
def index():
  """
  가게부 목록 가져오기
  ---
  responses:
    200:
      description : 로그인 했을 때 해당 유저의 가게부 목록 가져오기 성공
    500:  
      description : 서버 통신 오류 
  """
  all_posts = model.Post.query.filter(model.Post.author_id==session['user_id'], model.Post.deleted==0).all()
  return render_template('balance/index.html', posts=all_posts)

@bp.route('/rollbacklist')
@auth.login_required
def rollbacklist():
  """
  삭제한 가게부 목록 가져오기
  ---
  responses:
    200:
      description : 로그인 했을 때 해당 유저가 삭제한 가게부 목록 가져오기 성공
    500:  
      description : 서버 통신 오류 
  """
  all_posts = model.Post.query.filter(model.Post.author_id==session['user_id'], model.Post.deleted==1).all()
  return render_template('balance/rollback.html', posts=all_posts)

@bp.route('/create', methods=('GET', 'POST'))
@auth.login_required
def create():
  """
  가게부 생성
  ---
  parameters:
  - name: 제목(title)
    description: 가게부 제목
    in: request
    type: string
    required: true
  - name: 금액(amount)
    description: 가게부 금액
    in: request
    type: number
    required: true
  - name: 상세내용(body)
    description: 가게부 상세내용
    in: request
    type: string
    required: false
  responses:
    200:
      description : 가게부 생성 성공, '/' 로 리다이렉트 되어 가게부 목록 출력
    500:  
      description : 가게부 생성 실패, 'balance/create' 로 리다이렉트
  """
  if request.method == 'POST':
    title = request.form['title']
    amount = request.form['amount']
    body = request.form['body']
    error = None

    if not title:
      error = '제목을 입력해주세요'
    if not amount:
      error = '금액을 입력해주세요'
    if not amount.isnumeric():
      error = '금액에 숫자를 입력해주세요'
    
    if error is not None:
      flash(error)
    else:
      print("title, amount, body",title, amount, body)
      data = model.Post(
        title = title,
        amount = amount,
        body = body,
        created_at=datetime.datetime.now().replace(tzinfo=None),
        author_id=session['user_id'],
        deleted=0
      )
      print("create data", data)
      model.db.session.add(data)
      model.db.session.commit()
      model.db.session.remove()
      return redirect(url_for('balance.index'))
  return render_template('balance/create.html')

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@auth.login_required
def update(id):
  """
  가게부 수정
  ---
  parameters:
  - name: 제목(title)
    description: 가게부 제목
    in: request
    type: string
    required: false
  - name: 금액(amount)
    description: 가게부 금액
    in: request
    type: number
    required: false
  - name: 상세내용(body)
    description: 가게부 상세내용
    in: request
    type: string
    required: false
  responses:
    200:
      description : 가게부 수정 성공, '/' 로 리다이렉트 되어 가게부 목록 출력
    500:  
      description : 가게부 수정 실패, 'balance/update' 로 리다이렉트
  """
  post = model.Post.query.filter_by(id=id).one()

  if request.method == 'POST':
    title = request.form['title']
    amount = request.form['amount']
    body = request.form['body']
    error = None

    if not title:
      error = '제목을 입력해주세요'
    if not amount:
      error = '금액을 입력해주세요'
    if not amount.isnumeric():
      error = '금액에 숫자를 입력해주세요'

    if error is not None:
      flash(error)
    else:
      print("title, amount, body",title, amount, body)
      model.Post.query.filter_by(id=id).update({
        "title": title,
        "amount": amount,
        "body": body
      })
      model.db.session.commit()
      model.db.session.remove()
      return redirect(url_for('balance.index'))
  return render_template('balance/update.html', post=post)

@bp.route('/<int:id>/delete', methods=('POST',))
@auth.login_required
def delete(id):
  """
  가게부 삭제
  ---
  parameters:
  - name: 가게부 id
    in: path
    type: number
    required: true
  responses:
    200:
      description : 가게부 삭제 성공, '/' 로 리다이렉트 되어 가게부 목록 출력
    500:  
      description : 가게부 삭제 실패, 404페이지로 abort
  """
  post = model.Post.query.filter_by(id=id).one()
  if post is None:
    abort(404, "Post id {0} doesn't exist.".format(id))
  else:
    model.Post.query.filter_by(id=id).update({
      "deleted": 1,
    })
    model.db.session.commit()
    model.db.session.remove()
  return redirect(url_for('index'))

@bp.route('/<int:id>/rollback', methods=('GET', 'POST'))
@auth.login_required
def rollback(id):
  """
  가게부 복구
  ---
  parameters:
  - name: 가게부 id
    in: path
    type: number
    required: true
  responses:
    200:
      description : 가게부 삭제 성공, '/' 로 리다이렉트 되어 가게부 목록 출력
    500:  
      description : 가게부 삭제 실패, 404페이지로 abort
  """
  post = model.Post.query.filter_by(id=id).one()
  if post is None:
    abort(404, "Post id {0} doesn't exist.".format(id))
  else:
    model.Post.query.filter_by(id=id).update({
      "deleted": 0,
    })
    model.db.session.commit()
    model.db.session.remove()
  return redirect(url_for('balance.rollbacklist'))