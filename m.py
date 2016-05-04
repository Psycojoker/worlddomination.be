import os

for i in filter(lambda x: x.endswith(".html") and not x.startswith("201"), os.listdir(".")):
    dir = i[:-len(".html")]
    os.makedirs(dir)

    content = open(i, "r").read()

    title = filter(lambda x: x.strip().startswith("title:"), content.split("\n"))[0].split(":")[1]

    date = filter(lambda x: x.strip().startswith("created:"), content.split("\n"))[0].split(":")[1]
    date.split(" ")[0]


    post = content.split("{% excerpt %}")[1].split("{% endexcerpt %}")[0]

    open("%s/contents.lr" % dir, "w").write("""\
title: %s
---
body:
%s
---
pub_date: %s
""" % (title, post, date))
