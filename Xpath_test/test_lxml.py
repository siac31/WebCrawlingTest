import lxml.etree as le

#with open('meiju.html','r',encoding='utf-8') as f:
#    html =f.read()
#    html_x =le.HTML(html)
#    title_s=html_x.xpath('//div[contains(@class,"threadlist_title pull_left j_th_tit")]/a/text()')
#    for title in title_s:
#        print(title)
        # nothing to print
        # 百度反扒取被注释了

# 使用正则表达式来反扒取
import re
with open('meiju.html','r',encoding='utf-8') as f:
    html =re.sub('\n','',f.read())
    print(html)
    title_pattern = '<div class="threadlist_title pull_left j_th_tit ">.*?<a.*?>(.*?)</a>'
    title_s = re.findall(title_pattern, html)
    print(len(title_s))
    for title in title_s:
        print(title)

