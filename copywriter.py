import os
from openai import OpenAI

# 请替换成你的真实API Key
API_KEY = "sk-b03ee845ba714658bf9eb17b081a0803"  
BASE_URL = "https://api.deepseek.com"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

def generate_copy(product, selling_points, style="朋友圈"):
    """
    生成文案
    product: 产品名，如"手工曲奇"
    selling_points: 卖点，如"纯天然、酥脆"
    style: 可选"朋友圈"或"小红书"
    """
    if style == "朋友圈":
        system_prompt = "你是一个朋友圈带货文案专家，风格：短句、口语化、带emoji、激发购买欲。"
        user_prompt = f"为产品「{product}」写3条朋友圈文案，突出卖点「{selling_points}」，每条不超过80字，用序号1.2.3.分隔。"
    else:  # 小红书
        system_prompt = "你是一个小红书爆款文案专家，风格：标题党、分段、加tag、情绪化。"
        user_prompt = f"为产品「{product}」写一篇小红书种草笔记，突出卖点「{selling_points}」，含标题和正文，加相关话题标签。"
    
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.8,  # 调高一点更有创意
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("====== AI文案生成器 ======")
    product = input("请输入产品名（如：手工曲奇）：")
    points = input("请输入卖点（如：纯天然、酥脆）：")
    style = input("选择风格（朋友圈/小红书）：")
    
    result = generate_copy(product, points, style)
    print("\n" + "="*40)
    print(result)
    print("="*40)