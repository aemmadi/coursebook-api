import requests
import json

url = "https://coursebook.utdallas.edu/clips/clip-section-v2.zog"

# headers = {
#     "content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
#     "DNT": "1",
#     "Origin": "https://coursebook.utdallas.edu",
#     "Referer": "https://coursebook.utdallas.edu/cs4337/term_20f?"
# }

head = {
    "Host": "coursebook.utdallas.edu",
    "Connection": "keep-alive",
    "Content-Length": "257",
    "Accept": "text/html, */*, q=0.01",
    "DNT": "1",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://coursebook.utdallas.edu",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://coursebook.utdallas.edu/search/cs4337.001.20f",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cookie": "__cfduid=d2cd069d0c50b3d808c699908efc6d1001559934992; PTGSESSID=467351c11ca0e73957cc58eb1dc74a86"
}

# data = {
#     "action": 'update-actions',
#     "id": 'data',
#     "data": ["cs4337.001.20f", "cs4337.501.20f"]
# }
data2 = {
    "id": "cs4337.001.2f",
    "div": "r-1childcontent",
}
# # print(json.dumps(data))
# response = requests.post(
#     url, data=json.dumps(data), headers=head, timeout=10)
# print(response.text)

with requests.Session() as session:
    session.get('https://coursebook.utdallas.edu/search/cs4337.001.20f')
    r = session.post('https://coursebook.utdallas.edu/clips/clip-section-v2.zog',
                     data=json.dumps(data2), headers=head)
    print(r.content)
