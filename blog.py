import os
import argh

from urllib2 import urlopen
from datetime import datetime
from bs4 import BeautifulSoup
from slugify import slugify

post_template = """\
{%% extends "_post.html" %%}

{%% hyde
    title: "%(title)s"
    created: %(date)s
%%}

{%% block article %%}
{%% article %%}
{%% excerpt %%}

<center>%(content)s</center>



{%% endexcerpt %%}
{%% endarticle %%}
{%% endblock %%}"""

vimeo_iframe_template = """
<iframe src="//player.vimeo.com/video/%(video_id)s" width="500" height="281" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe> <p><a href="http://vimeo.com/98639067">Garrett Smith - Why The Cool Kids Don't Use Erlang</a> from <a href="http://vimeo.com/erlang">Erlang Solutions</a> on <a href="https://vimeo.com">Vimeo</a>.</p>
"""

def _vimeo(url):
    soup = BeautifulSoup(urlopen(url))
    video_id = filter(None, url.split("/")[-1])
    title = soup.h1.text
    iframe_code = vimeo_iframe_template % {"video_id": video_id}

    post_content = post_template % {
        "content": iframe_code,
        "title": "Review: " + title,
        "date": datetime.now().strftime("%F %X"),
    }

    file_name = "%s.html" % (slugify(title))
    file_path = os.path.join("./content/reviews/talks/", file_name)

    if os.path.exists(file_path):
        raise Exception("File already exist: %s" % file_path)

    open(file_path, "w").write(post_content)
    os.system("vi %s +16" % file_path)


def review(url):
    if "vimeo.com" in url:
        _vimeo(url)

    else:
        raise Exception("I don't have a method for this website :(")


parser = argh.ArghParser()
parser.add_commands([review])

if __name__ == '__main__':
    parser.dispatch()
