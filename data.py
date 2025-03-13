import os
import httpx
import json

token = os.getenv('GITHUB_TOKEN')
if not token:
    raise ValueError('GITHUB_TOKEN is not set')
headers = {
    'Authorization': f'Bearer {token}',
    'Accept': 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2022-11-28'
}
result = []

for i in range(1, 11):
    print(f'正在爬取第{i}页')
    r = httpx.get(f'https://api.github.com/search/users?q=location:China&per_page=100&page={i}', headers=headers)
    data = r.json()
    for item in data['items']:
        result.append({
            'avatar': item['avatar_url'],
            'username': item['login'],
            'url': item['html_url']
        })
    print(f'第{i}页爬取完成')
json.dump(result, open('./data/data.json', 'w', encoding='utf-8'), ensure_ascii=False)
print('爬取完成')
