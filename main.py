import requests

api_key = "3f465e6b8aab4494af8ac55ae4447f32"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-06-05&sortBy=publishedAt&apiKey=3f465e6b8aab4494af8ac55ae4447f32"

request = requests.get(url)
content = request.json()


# print(content["articles"]["titles"])

for article in content["articles"]:
    print(article["title"])
    print(article["description"])

