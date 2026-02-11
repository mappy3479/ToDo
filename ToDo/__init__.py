# FlaskからFlaskというクラスをインポート
from flask import Flask,render_template

# Flaskアプリのインスタンスを作成（クラスがたいやきの型ならインスタンスはたいやき）　ちなみに俺はたいやき割と好き（？） 
app = Flask(__name__)

# rootを定義して(/)にアクセスがあったら以下の関数を呼び出す。
@app.route('/')
def index():
    todos = [
        "sample task 1",
        "sample task 2",
    ]
    return render_template("index.html", todos=todos)