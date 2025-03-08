from flask import Flask, render_template, jsonify
import pandas as pd
import random

app = Flask(__name__)


# 读取名字数据
def load_names():
    return pd.read_csv('boy_names.csv')


@app.route('/')
def index():
    return render_template('index_js.html')


@app.route('/get_names')
def get_names():
    names_df = load_names()
    if names_df.empty:
        return jsonify({'error': 'Data not found'}), 404

    # 随机选择5个名字
    selected_names = names_df.sample(5).to_dict(orient='records')

    return jsonify(selected_names)


if __name__ == '__main__':
    app.run(debug=True)