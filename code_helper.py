import os
from openai import OpenAI

API_KEY = "sk-b03ee845ba714658bf9eb17b081a0803"
BASE_URL = "https://api.deepseek.com"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

def generate_code(requirement, extra_notes=""):
    system_prompt = """你是一个资深Python工程师，擅长编写清晰、规范的脚本代码。
你的任务是根据用户需求生成可直接运行的Python代码。

输出格式严格遵循以下结构：
=== 代码 ===
[完整的Python代码，带中文注释，没有语法错误]

=== 使用说明 ===
[1-2句话告诉用户怎么运行这个脚本，需要安装什么库]

=== 注意事项 ===
[如果有特殊情况需要提醒，比如：文件路径要改成自己的、需要联网等]
"""
    user_prompt = f"""需求：{requirement}
额外要求：{extra_notes if extra_notes else "无"}
请生成完整可运行的代码。"""
    
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.3,  # 代码生成要精确，不要发挥
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("====== Python代码生成助手（自己用） ======")
    req = input("请输入客户的需求描述：")
    result = generate_code(req)
    print("\n" + "="*50)
    print(result)
    print("="*50)