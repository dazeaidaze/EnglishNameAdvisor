from flask import Flask, render_template, request, jsonify
import pandas as pd
import random

app = Flask(__name__)

# 加载名字数据
names_df = pd.read_csv('boy_names.csv')

print(names_df.head())

@app.route('/')
def index():
    # 渲染首页，提供选择名字长度的表单
    return render_template('index_lenth.html')


@app.route('/recommend', methods=['POST'])
def recommend_names():
    # 获取用户请求中的名字长度
    length = int(request.form.get('length'))

    # 过滤出符合条件的名字
    filtered_names = names_df[names_df['lenth'] == length]

    if filtered_names.empty:
        return jsonify({'error': 'No names of the specified length were found.'}), 404

    # 随机选择5个名字（或少于5个，如果不足的话）
    recommended_names = filtered_names.sample(min(len(filtered_names), 5))

    # 返回选中的名字列表
    return jsonify(recommended_names.to_dict(orient='records'))


if __name__ == '__main__':
    app.run(debug=True)