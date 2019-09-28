import re
with open('index.html','r',encoding='utf-8') as f:
    html=re.sub('\n','',f.read())
    print(html)
    section_pattern = '<section class="main_section">(.*?)</section>'
    sections=re.findall(section_pattern,html)
    category_pattern ='<h1>(.*?)</h1>'
    course_pattern ='<span class="course_name">(.*?)</span>'
    data_s=[] #定义一个空的列表
    for section in sections:
        category= re.findall(category_pattern,section)[0]
        courses=re.findall(course_pattern,section)
        data_s.append( #此列表为字典列表
            {
                'category':category,
                'courses':courses
            }
        )
    # print the result that human readable
    # pint 输出自动化行
    for data in data_s:
        print(data.get('category'))
        for course in data.get('courses'):
            print('     ',course)
