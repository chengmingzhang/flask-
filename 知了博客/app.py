from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_blog/', methods=['GET', 'POST'])
def add_blog():
    if request.method == 'GET':
        return render_template('add_blog.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        print(title)
        print(content)
        return '日志提交成功'

@app.route('/blog_detail/')
def blog_detail():
    return  render_template('blog_detail.html')


if __name__ == '__main__':
    app.run()
