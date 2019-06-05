from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello!'


@app.route('/setting/basic/')
def setting():
    return 'Setting Page'


@app.route('/profile/')
def profile():
    return render_template('profile.html')  # 模板渲染，图像传递


@app.route('/parameter/pass/')
def parameter_pass():
    name = request.args.get('name')
    age = request.args.get('age')
    return '%s, %s' % (name, age)


if __name__ == '__main__':
    app.run()
