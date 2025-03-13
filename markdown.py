import json
import datetime

now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
data = json.load(open('./data/data.json', 'r', encoding='utf-8'))
content = f"""
# China GitHub Ranking

> [!NOTE]
> 更新时间: {now}

|  `#`   | 用户名  | 头像  |
|  :----:  | :----:  | :----:  |
"""
for i, item in enumerate(data):
    content += f"| {i+1} | [{item['username']}]({item['url']}) | ![{item['username']}](https://wsrv.nl/?url={item['avatar']}&w=30&h=30) |"
    if i != len(data) - 1:
        content += "\n"

with open('./README.md', 'w', encoding='utf-8') as f:
    f.write(content)

