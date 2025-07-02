from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '이것이 보인다면 수정사항이 정상적으로 반영된 것'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
