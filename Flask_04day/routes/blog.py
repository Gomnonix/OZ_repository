from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from db import db
from models import Blog

blog_blp = Blueprint('blogs', 'blogs', url_prefix='/blogs')

@blog_blp.route('/')
class BlogList(MethodView):
    def get(self):
        blogs = Blog.query.all()
        return jsonify([{
                         "id": blog.id,
                         "title": blog.title, 
                         "content": blog.content, 
                         } for blog in blogs])

    def post(self):
        data = request.json
        new_blog = Blog(title=data['title'], content=data['content'])
        db.session.add(new_blog)
        db.session.commit()
        return jsonify({"message": "Blog created"}), 201

@blog_blp.route('/<int:blog_id>')
class BlogResource(MethodView):
    def get(self, blog_id):
        blog = Blog.query.get_or_404(blog_id)
        return jsonify({"title": blog.title, "content": blog.content})

    def put(self, blog_id):
        blog = Blog.query.get_or_404(blog_id)
        data = request.json
        blog.title = data['title']
        blog.content = data['content']
        db.session.commit()
        return jsonify({"message": "Blog updated"})

    def delete(self, blog_id):
        blog = Blog.query.get_or_404(blog_id)
        db.session.delete(blog)
        db.session.commit()
        return jsonify({"message": "Blog deleted"})