from flask import Flask, render_template
import requests
from post import Post
app = Flask(__name__)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
response_data = response.json()
blog_posts = []
for data in response_data:
    new_post = Post(data)
    blog_posts.append(new_post)


@app.route('/')
def home():
    return render_template("index.html", blog_posts=blog_posts)


@app.route('/post/<num>')
def get_post(num):
    return render_template("post.html", post=blog_posts[int(num) - 1])


if __name__ == "__main__":
    app.run(debug=True)
