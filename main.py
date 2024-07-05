import requests
from send_email import send_email


api_key = "3f465e6b8aab4494af8ac55ae4447f32"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-06-05&sortBy=publishedAt&apiKey=3f465e6b8aab4494af8ac55ae4447f32&language=en"

request = requests.get(url)
content = request.json()

body = ""
i = 0
for article in content["articles"][:20]:
    title = article.get("title", "No Title")
    description = article.get("description", "No Description")
    if i==0:
        body += "Subject: Today's news" + "\n" + f"{title}\n{description}" + "\n" + article["url"] + "\n\n"
        i=1
    else:
        body += f"{title}\n{description}" + "\n" + article["url"] + "\n\n"

body =body.encode("utf-8")
send_email(message = body)
