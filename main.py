import openai 
import time 
import re
import geturl
import gethtml

history = []  # 用于保存历史记录

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

    user_input = input("You: ")
    history.append("user: "+ user_input)
    query = "".join(history)


    if '搜索' in query or 'search' in query:
        search=fake_api("为用户输入制定搜索关键词,你只会返回一个关键词,无需其它说明: "+query,150,True,0.5)
        history.append("chatgpt搜索了:"+search)
        print("\n")

        url=geturl.geturl(search)
        html=gethtml.gethtml(url)

        try:
            require=fake_api("概括为100~200字的中文,只提取关键信息: "+html,1500,True,0.5)
            history.append("chatgpt:"+require)
            print("\n")
        except:
            print("搜索时有错误发生")
    
    elif '访问' in query or 'visit' in query:
        url=gethtml.find_url(query)

        html=gethtml.gethtml(url)

        try:
            require=fake_api("概括为100~200字的中文,只提取关键信息: "+html,1500,True,0.5)
            history.append("chatgpt:"+require)
            print("\n")
        except:
            print("访问时有错误发生")

    else:
        require=fake_api(query,1500,True,0.5)
        history.append("chatgpt:"+require)
        print("\n")

while True:
    main()