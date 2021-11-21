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
  print("session", session)
  all_posts = model.Post.query.all()
  return render_template('balance/index.html', posts=all_posts)



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
    print(session)
    if error is not None:
      flash(error)
    else:
      data = model.Post(
        title = title,
        amount = amount,
        body = body,
        created_at=datetime.datetime.now().replace(tzinfo=None),
        updated_at=datetime.datetime.now().replace(tzinfo=None),
        author_id=session['user_id']
      )
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

    if error is not None:
      flash(error)
    else:
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
  id = id['id']

  post = model.Post.query.filter_by(id=id).one()
  if post is None:
    abort(404, "Post id {0} doesn't exist.".format(id))
  else:
    model.db.session.delete(post)
    model.db.session.commit()
    model.db.session.remove()
  return redirect(url_for('balance.index'))