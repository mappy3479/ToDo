# FlaskからFlaskというクラスをインポート
from flask import Flask

# Flaskアプリのインスタンスを作成（クラスがたいやきの型ならインスタンスはたいやき）　ちなみに俺はたいやき割と好き（？） 
app = Flask(__name__)

# rootを定義して(/)にアクセスがあったら以下の関数を呼び出す。
@app.route('/')
def hello():
    return 'hello,flask'

# スクリプトとして実行された場合にサーバーを起動
if __name__ == '__main__':
    app.run(debug=True)