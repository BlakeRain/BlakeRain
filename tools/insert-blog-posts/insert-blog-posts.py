import json
import requests
from bs4 import BeautifulSoup

MARK_START = "<!-- BLOGPOSTS_START -->"
MARK_END = "<!-- BLOGPOSTS_END -->"


def postUrl(post):
    return f"- [{post['title']}](https://blakerain.com/blog/{post['slug']})"


if __name__ == "__main__":
    html = requests.get("https://blakerain.com")
    soup = BeautifulSoup(html.text, "html.parser")
    src = soup.find(id="__NEXT_DATA__").string
    obj = json.loads(src)
    posts = obj["props"]["pageProps"]["posts"]
    print(f"Found {len(posts)} blog post(s)")
    posts_markdown = '\n'.join([postUrl(post)
                               for post in res["data"]["posts"]])
    with open("README.md", "rt") as fp:
        content = fp.read()
    mark_start_ix = content.index(MARK_START) + len(MARK_START)
    mark_end_ix = content.index(MARK_END)
    new_content = content[:mark_start_ix] + "\n" + \
        posts_markdown + "\n" + content[mark_end_ix:]
    if new_content != content:
        print("Updating README.md")
        with open("README.md", "wt") as fp:
            fp.write(new_content)
    else:
        print("No new blog posts to add to README")
