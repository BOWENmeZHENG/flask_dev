from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from AnnoApp.db import get_db
from AnnoApp.pyutils import split_para

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, segment, created'
        ' FROM post p'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)

@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        segment = ', '.join(["'" + w + "'" for w in split_para(body)])

        if not title:
            flash('Title is required.')
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, segment)'
                ' VALUES (?, ?, ?)',
                (title, body, segment)
            )
            db.commit()
            flash(f"Record '{title}' has been saved!")
            posts = db.execute(
                'SELECT p.id, title, body, segment, created'
                ' FROM post p'
                ' ORDER BY created DESC'
            ).fetchall()
            return render_template('blog/index.html', posts=posts)

    return render_template('blog/create.html')

def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, segment, created'
        ' FROM post p'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    return post

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
def update(id):
    post = get_post(id)
    db = get_db()
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        segment = ', '.join(["'" + w + "'" for w in split_para(body)])
        if not title:
            flash('Title is required.')
        else:           
            db.execute(
                'UPDATE post SET title = ?, body = ?, segment = ?'
                ' WHERE id = ?',
                (title, body, segment, id)
            )
            db.commit()
            flash(f"Record '{title}' has been updated!")
            posts = db.execute(
                'SELECT p.id, title, body, segment, created'
                ' FROM post p'
                ' ORDER BY created DESC'
            ).fetchall()
            return render_template('blog/index.html', posts=posts)

    return render_template('blog/update.html', post=post)

@bp.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    flash(f"Record has been deleted!")
    posts = db.execute(
        'SELECT p.id, title, body, segment, created'
        ' FROM post p'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)
