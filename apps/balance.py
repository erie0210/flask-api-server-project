# -*- coding: utf-8 -*-
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)
from werkzeug.exceptions import abort

from . import auth


from apps.model import model
import datetime

bp = Blueprint('balance', __name__)


@bp.route('/')
@auth.login_required
def index():
  all_posts = model.Post.query.filter(model.Post.author_id==session['user_id'], model.Post.deleted==0).all()
  return render_template('balance/index.html', posts=all_posts)

@bp.route('/rollbacklist')
@auth.login_required
def rollbacklist():
  all_posts = model.Post.query.filter(model.Post.author_id==session['user_id'], model.Post.deleted==1).all()
  return render_template('balance/rollback.html', posts=all_posts)


@bp.route('/create', methods=('GET', 'POST'))
@auth.login_required
def create():
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


@bp.route('/<int:id>/delete', methods=('GET', 'POST'))
@auth.login_required
def delete(id):
  post = model.Post.query.filter_by(id=id).one()
  if post is None:
    abort(404, "Post id {0} doesn't exist.".format(id))
  else:
    model.Post.query.filter_by(id=id).update({
      "deleted": 1,
    })
    model.db.session.commit()
    model.db.session.remove()
  return redirect(url_for('balance.index'))


@bp.route('/<int:id>/rollback', methods=('GET', 'POST'))
@auth.login_required
def rollback(id):
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