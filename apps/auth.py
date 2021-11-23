# -*- coding: utf-8 -*-
from flask import Blueprint, request, redirect, flash, url_for, session
from flask.templating import render_template
from werkzeug.security import check_password_hash, generate_password_hash
import functools
from apps.model import model
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

bp = Blueprint('auth', __name__, url_prefix='/auth')

def check(email):
  if(re.fullmatch(regex, email)):
    return True
  else:
    return False

def login_required(view):
  @functools.wraps(view)
  def wrapped_view(**kwargs):
    session_keys = session.keys()
    
    # 로그인 한 유저가 아닌 경우:
    # 아예 비어있는 경우
    if 'user' not in session_keys:
      return redirect(url_for('auth.login'))
    # user는 있으나 None인 경우 
    # (user가 다른 값으로 존재할 경우를 대비해 login 값을 false로 넣어준다)
    if 'user' in session_keys:
      session['login']=False
      return redirect(url_for('auth.login'))
    # login이 false인 경우
    if 'login' in session_keys and session['login']==False:
      return redirect(url_for('auth.login'))
    return view(**kwargs)
  return wrapped_view

@bp.route('/register', methods=('GET', 'POST'))
def register():
  """
  회원가입
  ---
  parameters:
  - name: 이메일(email)
    description: 이메일주소
    in: request
    type: string
    required: true
  - name: 비밀번호(passowrd)
    description: 비밀번호
    in: request
    type: string
    required: true
  responses:
    200:
      description : 회원가입 성공, '/' 로 리다이렉트 되어 가게부 목록 출력
    500:  
      description : 회원가입 실패, ' auth/register' 로 리다이렉트
  """
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
    error = None

    if not email:
      error = '이메일을 입력해주세요'
    elif not password:
      error = '비밀번호를 입력해주세요'
    if not check(email):
      error = '이메일 형식을 맞춰주세요.'

    try:
      data = model.MyUser(
        email= email,
        password = generate_password_hash(password),
      )
      select_user = model.MyUser.query.filter_by(email = request.form['email']).all()
      if len(select_user) > 0:
          error = "이미 사용 중인 이메일입니다."
      if error is None:
        model.db.session.add(data)
        model.db.session.commit()
        model.db.session.remove()
        return redirect(url_for('auth.login'))
    except Exception as e:
      return str(e)
    flash(error)
  return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
  """
  로그인
  ---
  parameters:
  - name: 이메일(email)
    description: 이메일주소
    in: request
    type: string
    required: true
  - name: 비밀번호(passowrd)
    description: 비밀번호
    in: request
    type: string
    required: true
  responses:
    200:
      description : 로그인 성공, '/' 로 리다이렉트 되어 가게부 목록 출력
    500:  
      description : 로그인 실패, ' auth/login' 로 리다이렉트
  """
  session_keys = session.keys()
  if 'login' in session_keys:
    if session['login']== True:
      return redirect(url_for('index'))

  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
    error = None

    user = model.MyUser.query.filter_by(email=email).one()
    if user is None:
      error = "이메일을 다시 확인해주세요"
    elif not check_password_hash(user.password, password):
      error = "비밀번호를 다시 확인해주세요"

    if error is None:
      session.clear()
      session['user_id'] = user.id
      session['email'] = user.email
      session['login'] = True
      return redirect(url_for('index'))
    flash(error)
  return render_template('auth/login.html')

@bp.route('/logout')
def logout():
  """
  로그아웃
  ---
  responses:
    200:
      description : 로그아웃 성공, '/' 로 리다이렉트
    500:  
      description : 로그아웃 실패, '/' 로 리다이렉트
  """
  session.clear()
  session['login'] = False
  return redirect(url_for('auth.login'))