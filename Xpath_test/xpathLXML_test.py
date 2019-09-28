import lxml.etree as le

with open('edu.html','r',encoding='utf-8') as f:
    html=f.read()
    #print(html)
    # convert html to lxml
    html_x=le.HTML(html)
    div_x_s=html_x.xpath('//div[contains(@class,"classify_cList")]')
    print(div_x_s)
    data_s=[]
    for div_x in div_x_s:
        category1=div_x.xpath('./h3/a/text()')#. 表示从当前节点开始查找 也就是div_x对应的节点
        #print(category1)#f返回的是一个列表 包裹所有一级分类
        category2_s=div_x.xpath('./div/span/a/text()')
        #print(category2_s)
        data_s.append(
            dict(
                category1=category1,
                category2_s=category2_s
            )
        )
        for data in data_s:
            print(data.get('category1'))
            for category2 in data.get('category2_s'):
                print('     ', category2)


