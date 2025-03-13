import json
import datetime

now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
data = json.load(open('./data/data.json', 'r', encoding='utf-8'))
content = f"""
# China GitHub Ranking

更新时间: {now}

|  Ranking   | Avatar  | Username  |
|  ----  | ----  | ----  |
"""
for i, item in enumerate(data):
    content += f"| {i+1} | ![{item['avatar']}]({item['avatar']}) | [{item['username']}]({item['url']}) |"
    if i != len(data) - 1:
        content += "\n"

with open('./README.md', 'w', encoding='utf-8') as f:
    f.write(content)

