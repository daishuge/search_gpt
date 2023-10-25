import requests
from bs4 import BeautifulSoup

def find_url(text):
    # 定义用于匹配URL的正则表达式
    url_pattern = re.compile(r'https?://[^\s/$.?#].[^\s]*', re.IGNORECASE)
    
    # 使用findall方法查找所有匹配项
    urls = url_pattern.findall(text)
    
    return urls

def gethtml(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查是否请求成功
        html = response.text
        
        soup = BeautifulSoup(html, 'html.parser')
        
        # 移除脚本和样式标签
        for script in soup(['script', 'style']):
            script.extract()
        
        # 获取纯文本内容
        text_content = soup.get_text()
        
        # 去除首尾的空白字符和空行
        lines = (line.strip() for line in text_content.splitlines())
        non_empty_lines = (line for line in lines if line)  # 过滤掉空行
        cleaned_content = '\n'.join(non_empty_lines)
        
        return cleaned_content
    except requests.exceptions.RequestException as e:
        print("请求出现问题:", e)
        return None

