import os
from openai import OpenAI

# 请替换成你的真实API Key
API_KEY ="sk-b03ee845ba714658bf9eb17b081a0803"  
BASE_URL = "https://api.deepseek.com"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

def polish_essay(text, target="留学申请"):
    """
    润色英语作文
    text: 用户输入的英文原文
    target: 用途（留学申请/雅思/考研英语）
    """
    system_prompt = """You are a professional native English editor with 10 years of experience in academic writing and留学文书修改.
Your task is to polish the text to make it sound natural, academic, and compelling.
Follow these rules strictly:
1. Correct all grammar, spelling, and punctuation errors.
2. Upgrade basic vocabulary to advanced, precise words (e.g., "good" -> "exemplary").
3. Improve sentence flow and coherence.
4. Keep the original meaning and style (formal or semi-formal).
5. Output in the following strict format:
   === POLISHED VERSION ===
   [The fully corrected English text here]
   === MAJOR CORRECTIONS ===
   [List 3-5 specific changes in Chinese, e.g., "1. 将 'very good' 改为 'exemplary' 以增强学术感"]
   === SUGGESTIONS ===
   [Give 1-2 overall suggestions in Chinese to improve the essay further]
"""

    user_prompt = f"目标用途：{target}\n\n原文内容：\n{text}"

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7,  # 润色可以稍微保守一点，不需要太天马行空
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("====== 英语作文/留学文书润色 ======")
    target = input("请输入目标用途（留学申请/雅思/考研英语）：")
    print("请粘贴你要润色的英文内容（按回车键结束输入，输入完成后按 Ctrl+Z 或 Ctrl+D 再按回车）：")
    
    lines = []
    while True:
        try:
            line = input()
            lines.append(line)
        except EOFError:
            break
    text = "\n".join(lines)
    
    result = polish_essay(text, target)
    print("\n" + "="*50)
    print(result)
    print("="*50)