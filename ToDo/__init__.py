# FlaskからFlaskというクラスをインポート
from flask import Flask,render_template,request,redirect

# Flaskアプリのインスタンスを作成（クラスがたいやきの型ならインスタンスはたいやき）　ちなみに俺はたいやき割と好き（？） 
app = Flask(__name__)

# todosというリストを作成
todos = []

# rootを定義して(/)にアクセスがあったら以下の関数を呼び出す。
@app.route('/')
def index():
    # todos = []を削除
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add():
    todo = request.form.get("todo")
    if todo:
        todos.append(todo)
    return redirect("/")