# search_gpt2.0强势来袭!

## 简介
这是一个接入google 的chatgpt. 可以访问互联网

灵感来源于newbing

## 依赖

- Python 3.x
- BeautifulSoup
- googlesearch-python
- openai

## 安装

```bash
pip install beautifulsoup4 googlesearch-python openai
```
## 运行截图

![image](https://github.com/daishuge/search_gpt/assets/122254868/a74c00dd-ae33-4fcf-813f-f4f722c22cfb)

为数不多的成功运行(

## 文件说明
gethtml.py: 用于获取网页HTML内容和鉴别输入中的url

geturl.py: google搜索得到排名第一url

main.py: 主程序文件,包含ai调用,输入处理

## 目前问题

不知为何,"访问"的指令一直报错

```
请求出现问题: No connection adapters were found for "['https://openai.com/']"
访问时有错误发生
```

有时也会出现离谱情况:
![image](https://github.com/daishuge/search_gpt/assets/122254868/647e5d20-59ec-4181-8838-876e29e5b12b)

"search"_gpt

![image](https://github.com/daishuge/search_gpt/assets/122254868/e6fd59c7-71a0-4dc7-8be2-3772d8e80c82)


欢迎提出issue,提出解决方案或发起提问,大家一起进步（*＾-＾*）
