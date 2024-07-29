# POSTされたパラメータを大きく表示するだけのサーバ
from datetime import datetime
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from flask import Flask, request, jsonify
from tkinter import font

import threading
import queue


# Flaskアプリケーションの設定
app = Flask(__name__)

@app.route('/', methods=['POST'])
def post_data():
    """
    データがPOSTされたら、キューに追加
    """
    data = request.get_json()
    json_data = jsonify(data)
    app.queue.put(str(data))
    return {'server_time': datetime.now().isoformat()}


class FlaskThread(threading.Thread):
    """
    Flask実行用スレッド
    """

    def __init__(self, app):
        threading.Thread.__init__(self)
        self.app = app
        self.daemon = True

    def run(self):
        self.app.run(debug=False, use_reloader=False, host='0.0.0.0')  # ここを修正


class Application(tk.Tk):
    """
    表示されるUI
    """
    def __init__(self):
        super().__init__()
        self.title("Tkinter Flask Server")
        self.geometry("1024x600")

        self.text_area = ScrolledText(self, wrap=tk.WORD, width=100, height=40)

        text_font = font.Font(family="Helvetica", size=24)
        self.text_area.configure(font=text_font)

        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.queue = app.queue = queue.Queue()
        self.after(100, self.process_queue)

    def process_queue(self):
        while not self.queue.empty():
            data = self.queue.get()
            data = datetime.now().strftime('%H:%M:%S') + ' ' + data
            self.text_area.insert(tk.END, data + "\n")
            self.text_area.see(tk.END)
        self.after(100, self.process_queue)


if __name__ == "__main__":
    tk_app = Application()
    flask_thread = FlaskThread(app)
    flask_thread.start()
    tk_app.mainloop()

