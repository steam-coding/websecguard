# from flask import Flask, request, render_template
# import sqlite3
# import os
# from datetime import datetime
#
# app = Flask(__name__)
#
# LOG_PATH = 'logs/attacks.log'
# os.makedirs('logs', exist_ok=True)
#
# # 模拟数据库（初始化）
# def init_db():
#     conn = sqlite3.connect('users.db')
#     cursor = conn.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS users (
#             username TEXT,
#             password TEXT
#         )
#     ''')
#     cursor.execute("INSERT INTO users VALUES ('admin', 'admin123')")
#     conn.commit()
#     conn.close()
# # ---------------------------------------不安全写法----------------------------------------------------------------
# @app.route('/', methods=['GET', 'POST'])
# def login():
#     message = ''
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         conn = sqlite3.connect('users.db')
#         cursor = conn.cursor()
#
#         # 这里是有意的 SQL 注入漏洞！
#         query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
#         print("[QUERY] →", query)
#
#         try:
#             cursor.execute(query)
#             result = cursor.fetchone()
#         except Exception as e:
#             result = None
#             message = '数据库错误'
#
#         if result:
#             message = f'✅ 登录成功，欢迎 {username}！'
#         else:
#             message = '❌ 登录失败，请检查账号密码'
#
#         # 日志记录
#         log_attack(username, password, query)
#
#     return render_template('login.html', message=message)
# # --------------------------------不安全写法-------------------------------------------------------------
# # ---------------------------------安全写法-----------------------------------------
# # @app.route('/', methods=['GET', 'POST'])
# # def login():
# #     message = ''
# #     if request.method == 'POST':
# #         username = request.form['username']
# #         password = request.form['password']
# #
# #         conn = sqlite3.connect('users.db')
# #         cursor = conn.cursor()
# #
# #         # 安全版本：参数化查询，防止 SQL 注入
# #         try:
# #             cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
# #             result = cursor.fetchone()
# #         except Exception as e:
# #             result = None
# #             message = '数据库错误'
# #
# #         if result:
# #             message = f'✅ 登录成功，欢迎 {username}！'
# #         else:
# #             message = '❌ 登录失败，请检查账号密码'
# #
# #         # 日志记录原始输入（不记录查询语句）
# #         log_attack(username, password, "参数化查询已启用")
# #
# #     return render_template('login.html', message=message)
# # ---------------------------------安全写法-----------------------------------------
#
# # 简单记录每次请求
# def log_attack(user, pw, query):
#     with open(LOG_PATH, 'a') as f:
#         f.write(f"{datetime.now()} | 用户名: {user} | 密码: {pw} | SQL: {query}\n")
#
# if __name__ == '__main__':
#     init_db()
#     # app.run(debug=True)
#     app.run(host="0.0.0.0", port=5000, debug=True)
#
# -------------------------------------------------------------------------------------------------------------------

from flask import Flask, request, render_template
import sqlite3
import os

app = Flask(__name__)

DB_PATH = 'users.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT,
            password TEXT
        )
    ''')
    cursor.execute("INSERT OR IGNORE INTO users VALUES ('admin', 'admin123')")
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # 安全写法：使用参数化查询防止注入
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        result = cursor.fetchone()

        if result:
            message = f'✅ 登录成功，欢迎 {username}！'
        else:
            message = '❌ 登录失败，请检查账号密码'

    return render_template('login.html', message=message)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
