import re

def cut(long_text, max_tokens=3000):
    # 分割文本为句子
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', long_text)
    
    # 合并句子为段落，每个段落长度不超过max_tokens
    segments = []
    current_segment = ""
    for sentence in sentences:
        if len(current_segment) + len(sentence) < max_tokens:
            current_segment += sentence + " "
        else:
            segments.append(current_segment.strip())
            current_segment = sentence + " "
    if current_segment:
        segments.append(current_segment.strip())
    
    # 构建包含段落和序号的字典
    segmented_text = {i+1: segment for i, segment in enumerate(segments)}
    
    return segmented_text



