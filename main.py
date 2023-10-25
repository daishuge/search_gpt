import openai 
import time 
import re

ask='''
你是一个有用的帮手,你现在被赋予了google搜索和访问互联网的功能.
如果你想搜索google,你可以把你想搜索的内容放入"<>"中.
像这样:
<history of google>
如果你想获得一个url指向的网站信息,请把url放入"[]"中.
像这样:
[http://github.com/xxx]
你在一次对话中只能进行一种操作
以下是用户的输入,包含历史记录
'''

#调用示例: full_result = fake_api(query,1500,True,1)
def fake_api(query,max,a,tem):     #用户输入，最大token，是否流式打印，温度
     openai.api_key = "fk-FCHVDJh1X-2HeS24Yla_Ejg03qJBdWaDOd-Jzy3PKTk"  # 使用假的 API 密钥 
     openai.api_base = "https://ai.fakeopen.com/v1/" 
     start_time = time.time()  # 记录开始时间 
  
     response = openai.ChatCompletion.create( 
         model='gpt-3.5-turbo', 
         messages=[ 
             {'role': 'user', 'content': query} 
         ], 
         temperature=tem, 
         max_tokens=max, 
         stream=True  # 开启流式输出 
     ) 
  
     result = ""  # 创建一个空字符串来保存流式输出的结果 
  
     for chunk in response: 
         # 确保字段存在 
         if 'choices' in chunk and 'delta' in chunk['choices'][0]: 
             chunk_msg = chunk['choices'][0]['delta'].get('content', '') 
             result += chunk_msg  # 将输出内容附加到结果字符串上 
  
             if a: 
                 print(chunk_msg, end='', flush=True) 
                 time.sleep(0.05) 
  
     return result  # 返回流式输出的完整结果 

def main():

    query = input("You: ")
    if '搜索' in query or 'search' in query:
        search=fake_api("为用户输入制定搜索关键词,你只会返回一个关键词,无需其它说明: "+query,150,True,0.5)

while True:
    main()