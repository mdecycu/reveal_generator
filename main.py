from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 儲存簡報內容的字典
presentations = {}

# 首頁路由,顯示編輯器
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 取得使用者輸入的簡報內容
        content = request.form['content']
        # 將簡報內容儲存在 presentations 字典中,key 為簡報名稱
        presentations['my_presentation'] = content
        # 重新導向到預覽頁面
        return redirect(url_for('preview', name='my_presentation'))
    # 在 GET 請求時,回傳編輯器頁面
    return render_template('editor.html')

# 預覽頁面路由
@app.route('/preview/<name>')
def preview(name):
    # 從 presentations 字典中取得指定簡報的內容
    content = presentations.get(name, '')
    # 回傳預覽頁面,並將簡報內容傳遞給模板
    return render_template('preview.html', content=content)

if __name__ == '__main__':
    app.run(debug=True)
