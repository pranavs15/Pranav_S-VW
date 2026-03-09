from flask import Flask, request, jsonify
from models import db, Book

def setup_routes(app):
    @app.route("/books", methods=["POST"])
    def add_book():
        data = request.get_json()
        title = data.get("title")
        author = data.get("author")
        copies = data.get("copies")
        if not title or not author or copies is None:
            return jsonify({"error": "All fields are required"}), 400
        book = Book(title=title, author=author, copies=copies)
        db.session.add(book)
        db.session.commit()
        return jsonify({"message": "Book added", "book_id": book.id}), 201

    @app.route("/books", methods=["GET"])
    def list_books():
        books = Book.query.all()
        result = [{"id": b.id, "title": b.title, "author": b.author, "copies": b.copies} for b in books]
        return jsonify(result)

    @app.route("/books/borrow/<int:book_id>", methods=["POST"])
    def borrow_book(book_id):
        book = Book.query.get(book_id)
        if not book:
            return jsonify({"error": "Book not found"}), 404
        if book.copies == 0:
            return jsonify({"error": "No copies available"}), 400
        book.copies -= 1
        db.session.commit()
        return jsonify({"message": f"You borrowed '{book.title}'", "remaining_copies": book.copies})

    @app.route("/books/unavailable", methods=["GET"])
    def unavailable_books():
        books = Book.query.filter_by(copies=0).all()
        result = [{"id": b.id, "title": b.title, "author": b.author} for b in books]
        return jsonify(result)