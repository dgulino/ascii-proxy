# Usage: mitmdump -s "modify_response_body.py mitmproxy bananas"
# (this script works best with --anticache)
from libmproxy.protocol.http import decoded
from libmproxy.script import concurrent
from bs4 import BeautifulSoup
from plumbum import local

convert = local['convert']
curl = local['curl']
jp2a = local['jp2a']

css="font-family: 'Courier New', Courier, 'Lucida Sans Typewriter', 'Lucida Typewriter', monospace; font-size: 14px; font-style: normal; font-variant: normal; font-weight: 400; line-height: 20px;"

def start(context, argv):
    pass

@concurrent
def response(context, flow):
    if flow.response.headers.get_first("content-type", "").startswith("text"):
        with decoded(flow.response):  # automatically decode gzipped responses.
            soup = BeautifulSoup(flow.response.content, 'lxml')
            for img in soup("img"):

                try:
                    src = img['src']
                    if src[0:4] != "http":
                        src = "http:" + img['src']
                    print src
                    if src.find(".jpg") > 0 or src.find(".jpeg") > 0:
                        chain = jp2a[src]
                    else:
                        chain = curl['-sS', src] | convert['-','jpg:-'] | jp2a['-']
                    ascii_paragraph = soup.new_tag("p")    
                    ascii_paragraph['style'] = css
                    ascii_paragraph.string = chain()
                    img.replace_with(ascii_paragraph)
                except:
                    img.replace_with("IMAGE")
            flow.response.content = str(soup)
