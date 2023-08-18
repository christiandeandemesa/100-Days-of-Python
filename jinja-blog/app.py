from flask import Flask, render_template
import requests
from post import Post

posts = requests.get("https://api.npoint.io/b816686a3de82335626a").json()
post_objects = []

for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)

@app.route("/")
def get_all_posts():
    # Sends the posts into the HTML file.
    return render_template("index.html", all_posts=post_objects)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post

    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(0)