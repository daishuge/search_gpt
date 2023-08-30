import openai
from geturl import geturl
from gethtml import gethtml
from cut import cut
import time
#导入必要模块

openai.api_key = 'YOUR_OPENAI_KEY'

def ai(user_input,max_tokens):
    history = [{"role": "system", "content": 'you are a ai called chatgpt-4'}]

    history.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=history,
        max_tokens=max_tokens  # 设置较小的 max_tokens 值，以适应模型的要求
    )
    reply = response['choices'][0]['message']['content']    #虽然我也看不懂，但官方文档就这样写的
    time.sleep(10)
    return reply

def main(user_input):

    #清空1.txt
    with open('1.txt','w',encoding='utf-8')as f:
        f.write('')
    
    user_input_for_ai='Please formulate search keywords according to what users want you to search for.remember:only output the key word!you can only reply at most 6 words:'+user_input
#合并内容    

    search_key_word=str(ai(user_input_for_ai,7))    #ai思考搜索关键词
    
    print(str('我将搜索: '+search_key_word))    #返回给用户
    
    #调用geturl.geturl爬取网站文本内容
    url=geturl(search_key_word)
    print('成功获得链接: '+url)    #返回给用户
    
    try:
        html=str(gethtml(url))
    except:
        html('没有在网页上找到合适信息')
        
    a=0    #定义计数变量a    
    
    length=len(cut(html))
    for number,text in cut(html).items():
        reply=ai('概括成至多100个英文单词：'+text,110)    #ai概括一段内容
        
        with open('1.txt','a',encoding='utf-8')as f:
            a=a+1
            f.write(reply+'\n')    #写入每一段的内容
            print('成功理解第 '+str(a)+' 段文字并写入，共 '+str(length)+' 段')    #返回给用户
            
    with open('1.txt','r',encoding='utf-8')as f:
        last =ai('请用中文概括这些的有用内容'+f.read(),2000)    #总结
        
    print('最后结果: '+last)    #返回最后结果
    
    #向文件中写入最后结果
    with open('1.txt','w',encoding='utf-8')as f:
        f.write(last)
        
    print('你可以在1.txt中找到这个回答内容')


main(str(input('input:')))
