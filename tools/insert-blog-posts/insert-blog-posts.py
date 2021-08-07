import requests

MARK_START = "<!-- BLOGPOSTS_START -->"
MARK_END = "<!-- BLOGPOSTS_END -->"


def postUrl(post):
    return f"- [{post['title']}](https://blakerain.com/blog/{post['slug']})"


if __name__ == "__main__":
    res = requests.get("https://blakerain.com/blog/routeInfo.json").json()
    posts_markdown = '\n'.join([postUrl(post)
                               for post in res["data"]["posts"]])
    with open("README.md", "rt") as fp:
        content = fp.read()
    mark_start_ix = content.index(MARK_START) + len(MARK_START)
    mark_end_ix = content.index(MARK_END)
    new_content = content[:mark_start_ix] + "\n" + \
        posts_markdown + "\n" + content[mark_end_ix:]
    if new_content != content:
        with open("README.md", "wt") as fp:
            fp.write(new_content)
