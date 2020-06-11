import requests
import json

SEU_TOKEN = ''

if not SEU_TOKEN:
    input(f'Insert your token: {SEU_TOKEN}')

get_url = f'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token={SEU_TOKEN}'
post_url = f'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token={SEU_TOKEN}'

req = requests.get(get_url)
res = json.loads(req.text)

print(res)
