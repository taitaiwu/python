from PyQt5 import QtWidgets, QtGui, QtCore, QtMultimedia, QtMultimediaWidgets
import sys
import pandas
from flask import Flask, request, jsonify
import openai
import pyttsx3
import threading
import requests
import speech_recognition as sr

# 初始化 PyQt 應用程式
qt_app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle("羅伯特")
Form.resize(800, 400)
# Form.setStyleSheet('''background: rgba(223, 245, 229, 0.97);''')

# 設置相機背景
camera_viewfinder = QtMultimediaWidgets.QCameraViewfinder(Form)
camera_viewfinder.setGeometry(0, 0, 800, 400)

camera = QtMultimedia.QCamera()
camera.setViewfinder(camera_viewfinder)
camera.start()

# 標籤與歡迎訊息
label1 = QtWidgets.QLabel(Form)
label1.setText("歡迎使用 金門大學資工系 聊天機器人")
label1.move(70, 50) 
label1.setStyleSheet('''
    font-size: 40px;
    font-family: "微軟正黑體";
''')

# 聊天介面
chat_display = QtWidgets.QTextEdit(Form)
chat_display.setReadOnly(True)
chat_display.setGeometry(50, 120, 700, 180)
chat_display.setStyleSheet('''
    background-color: rgba(255, 255, 255, 0.7);
    font-size: 16px;
    font-family: "微軟正黑體";
    border: 1px solid #ccc;
    padding: 5px;
''')

user_input = QtWidgets.QLineEdit(Form)
user_input.setPlaceholderText("請輸入您的問題...")
user_input.setGeometry(50, 310, 500, 40)
user_input.setStyleSheet('''
    background-color: rgba(255,255,255, 0.8);
    font-size: 16px;
    font-family: "微軟正黑體";
    padding: 5px;
    border: 1px solid #ccc;
    border-radius: 5px;
''')

send_button = QtWidgets.QPushButton(Form)
send_button.setText('送出')
send_button.setGeometry(570, 310, 80, 40)
send_button.setStyleSheet('''
    background: #4CAF50;
    color: white;
    font-size: 16px;
    border-radius: 5px;
''')

voice_button = QtWidgets.QPushButton(Form)
voice_button.setText('語音輸入')
voice_button.setGeometry(670, 310, 80, 40)
voice_button.setStyleSheet('''
    background: #2196F3;
    color: white;
    font-size: 16px;
    border-radius: 5px;
''')

# AI 聊天機器人後端
app = Flask(__name__)

# 替換為你自己的 OpenAI API 密鑰
openai.api_key =""

def speak_text(text):
    """ 每次调用时重新初始化 pyttsx3 引擎，并朗读文本 """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

@app.route('/magic_mirror', methods=['POST'])
def magic_mirror():
    user_input = request.json.get('question')

    if not user_input:
        return jsonify({'error': '问题未提供'}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "你是一个有用的助手。"},
                {"role": "user", "content": user_input}
            ],
            max_tokens=100
        )
        answer = response['choices'][0]['message']['content'].strip()

        # 在单独的线程中朗读答案
        threading.Thread(target=speak_text, args=(answer,)).start()

        return jsonify({'answer': answer})
    except Exception as e:
        return jsonify({'error': '发生错误', 'details': str(e)}), 500

def chat_with_api(question):
    url = "http://localhost:5000/magic_mirror"
    headers = {"Content-Type": "application/json"}
    payload = {"question": question}

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data['answer']
        else:
            return f"錯誤: 狀態碼 {response.status_code}"
    except Exception as e:
        return f"請求失敗: {e}"

# 按鈕行為
send_button.clicked.connect(lambda: handle_user_input())

voice_button.clicked.connect(lambda: handle_voice_input())

def handle_user_input():
    question = user_input.text().strip()
    if question:
        chat_display.append(f"<b>您:</b> {question}")
        user_input.clear()
        answer = chat_with_api(question)
        chat_display.append(f"<b>機器人:</b> {answer}")

def handle_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        chat_display.append("<b>系統:</b> 正在聆聽... 請說話")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            question = recognizer.recognize_google(audio, language="zh-TW")
            chat_display.append(f"<b>您:</b> {question}")
            answer = chat_with_api(question)
            chat_display.append(f"<b>機器人:</b> {answer}")
        except sr.WaitTimeoutError:
            chat_display.append("<b>系統:</b> 聆聽超時，請再試一次！")
        except sr.UnknownValueError:
            chat_display.append("<b>系統:</b> 無法辨識語音，請再試一次！")
        except Exception as e:
            chat_display.append(f"<b>系統:</b> 發生錯誤: {e}")

table = pandas.read_csv("https://data.moenv.gov.tw/api/v2/aqx_p_432?language=zh&format=csv&offset=0&limit=100&api_key=434207d8-d408-46b8-9784-5a6241739a9c")

# 啟動 Flask 和 PyQt 的主循環
def run_flask():
    app.run(host='0.0.0.0', port=5000, debug=False)

t = threading.Thread(target=run_flask)
t.setDaemon(True)
t.start()

Form.show()
sys.exit(qt_app.exec_())
