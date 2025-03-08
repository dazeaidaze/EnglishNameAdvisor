from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import random

app = Flask(__name__)

# 加载名字数据
names_df = pd.read_csv('boy_names.csv')
names_df.head()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 获取用户请求中的名字长度
        length = int(request.form.get('length'))

        # 过滤出符合条件的名字
        filtered_names = names_df[names_df['lenth'] == length]

        if filtered_names.empty:
            return render_template('index.html', error='Sorry,未找到指定长度的名字')

        # 随机选择5个名字（或少于5个，如果不足的话）
        recommended_names = filtered_names.sample(min(len(filtered_names), 20)).to_dict(orient='records')
        return render_template('index.html', nameList=recommended_names)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(port='8000',debug=True)