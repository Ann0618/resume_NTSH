
from flask import Flask, render_template,request

app = Flask(__name__)
# 建立問答集 Store questions and answers in a simple list for demonstration purposes
questions_answers = {
    “蘋果”: “apple”,
    “apple”: “蘋果”,
    “香蕉”: “banana”,
    “banana”: “香蕉”,
    “貓”: “cat”,
    “cat”: “貓”,
    “狗”: “dog”,
    “dog”: “狗”,
    “書”: “book”,
    “book”: “書”,
    “桌子”: “table”,
    “table”: “桌子”,
    “椅子”: “chair”,
    “chair”: “椅子”,
    “房子”: “house”,
    “house”: “房子”,
    “汽車”: “car”,
    “car”: “汽車”,
    “學校”: “school”,
    “school”: “學校”,
    “老師”: “teacher”,
    “teacher”: “老師”,
    “學生”: “student”,
    “student”: “學生”,
    “咖啡”: “coffee”,
    “coffee”: “咖啡”,
    “茶”: “tea”,
    “tea”: “茶”,
    “醫生”: “doctor”,
    “doctor”: “醫生”,
    “護士”: “nurse”,
    “sad”: “難過”
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

@app.route('/electives')
def electives():
    return render_template('electives.html')

@app.route('/ai')
def ai():
    return render_template('ai.html')

if __name__ == '__main__':
    app.run(debug=True)
