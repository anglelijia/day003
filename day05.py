import requests
url = 'http://www.baidu.com/s?'
URLS = []
def baidu(wds):
    count = 1
    for wd in wds:
        res = requests.get(url,params={'wd':wd})
        path = 'res%d.txt'%count
        with open(path,'w',encoding='utf8') as f:
            f.write(res.text)
        count +=1
    print(wds)
if __name__ == "__main__":
    wds = ('哈哈','嘻嘻','美女')
    baidu(wds)
lines = res.split('\n')
for line in lines:
    if '(http' in line:
        split_ line.split('(http=')
        for i in split_:
            if 'http' in i or 'https' in i:
                res = i.split('png)')[1]
                if 'png' in res:
                    URLS.append(res)

for res in URLS:
    response = request.get(res)
    content = response.content
    name = res.split('/')[-1]
    with open(name,'wb')as f:
        f.write(conent)



















import requests
url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808'
response = requests.get(url)
HTML = response.text
print(HTML)
lines = HTML.split('\r\n')
print(lines)
for url in lines:
   name = url.split(/')[-1].strip('\r)
   print(name) 
   try:
        response = requests.get(url,timeout=3)
        content = response.content
        content2 = str(content)
        if '\\x' in content2: 
          with open(name,'wb') as f:
              f.write(Connect)
              break
    except Exception as e:
        pass




