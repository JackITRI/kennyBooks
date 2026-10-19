from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from extensions import db
from models import Book
from forms import BookForm

books_bp = Blueprint('books', __name__)

@books_bp.route('/')
@login_required
def index():
    query = request.args.get('q', '').strip()
    if query:
        # 搜尋書名或作者包含關鍵字的書籍
        books = Book.query.filter(
            (Book.title.ilike(f'%{query}%')) | (Book.author.ilike(f'%{query}%'))
        ).all()
    else:
        books = Book.query.all()
    return render_template('books/index.html', books=books, query=query)

@books_bp.route('/book/new', methods=['GET', 'POST'])
@login_required
def create_book():
    form = BookForm()
    if form.validate_on_submit():
        book = Book(
            title=form.title.data,
            author=form.author.data,
            isbn=form.isbn.data,
            publisher=form.publisher.data,
            user_id=current_user.id
        )
        db.session.add(book)
        db.session.commit()
        flash('書籍已成功新增！', 'success')
        return redirect(url_for('books.index'))
    return render_template('books/book_form.html', form=form, title='新增書籍')

@books_bp.route('/book/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_book(id):
    book = Book.query.get_or_404(id)
    form = BookForm(obj=book)
    if form.validate_on_submit():
        book.title = form.title.data
        book.author = form.author.data
        book.isbn = form.isbn.data
        book.publisher = form.publisher.data
        db.session.commit()
        flash('書籍資訊已更新！', 'success')
        return redirect(url_for('books.index'))
    return render_template('books/book_form.html', form=form, title='編輯書籍')

@books_bp.route('/book/<int:id>/delete', methods=['POST'])
@login_required
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    flash('書籍已刪除。', 'info')
    return redirect(url_for('books.index'))