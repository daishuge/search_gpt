from googlesearch import search

def geturl(query):
    # 进行Google搜索并获取搜索结果链接
    search_results = search(query, num_results=1, lang="en")
    
    # 获取生成器的第一个结果并返回
    first_result = next(search_results, None)
    return first_result
