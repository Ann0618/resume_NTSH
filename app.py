
from flask import Flask, render_template, request
import os

app = Flask(__name__)

# 問答對照表（你原本的字典，我保留並可以擴充）
questions_answers = {
    "蘋果": "apple",
    "apple": "蘋果",
    "香蕉": "banana",
    "banana": "香蕉",
    "貓": "cat",
    "cat": "貓",
    "狗": "dog",
    "dog": "狗",
    "書": "book",
    "book": "書",
    "桌子": "table",
    "table": "桌子",
    "椅子": "chair",
    "chair": "椅子",
    "房子": "house",
    "house": "房子",
    "汽車": "car",
    "car": "汽車",
    "學校": "school",
    "school": "學校",
    "老師": "teacher",
    "teacher": "老師",
    "學生": "student",
    "student": "學生",
    "咖啡": "coffee",
    "coffee": "咖啡",
    "sad": "難過",
    "難過": "sad"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/competition')
def competition():
    return render_template('competition.html')

@app.route('/activities')
def activities():
    return render_template('activities.html')

@app.route('/leadership')
def leadership():
    return render_template('leadership.html')

@app.route('/club')
def club():
    return render_template('club.html')

@app.route('/electives')
def electives():
    return render_template('electives.html')

@app.route('/ai')
def ai():
    return render_template('ai.html')

# /ask：處理中英問答查詢（GET 顯示空表單、POST 處理翻譯查詢）
@app.route('/ask', methods=['GET', 'POST'])
def ask():
    question = ""
    answer = ""
    if request.method == 'POST':
        question = request.form.get('question', '').strip()
        # 簡單比對：若 dictionary 有直接對應就回傳；沒有就顯示預設訊息
        if question in questions_answers:
            answer = questions_answers[question]
        else:
            answer = "抱歉，我還不知道這個單字的翻譯。"
    return render_template('ask.html', question=question, answer=answer)

if __name__ == '__main__':
    # 可在 Render 等平台用 PORT 環境變數啟動；本機測試也可使用預設 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

