import os
from openai import OpenAI

API_KEY = "sk-b03ee845ba714658bf9eb17b081a0803"
BASE_URL = "https://api.deepseek.com"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

def fix_python_error(error_text, code_context=""):
    """
    诊断Python报错并给出修复方案
    error_text: 红色的报错信息
    code_context: 出错的代码片段（可选）
    """
    system_prompt = """你是一个资深Python工程师，擅长帮新手解决报错。
你的任务是：根据报错信息，给出**清晰、可操作、不吓人**的修复步骤。

输出格式必须严格遵循以下结构：
=== 问题诊断 ===
（用1句话大白话解释这个报错是什么意思，比如"你忘记安装某个库了"）

=== 修复步骤 ===
（列出具体操作，每步前面加序号，比如：
1. 打开终端
2. 输入以下命令：xxx
3. 按回车执行）

=== 完整代码示例（如果需要） ===
（如果报错涉及代码，给一段修正后的代码片段）

=== 预防建议 ===
（1句话告诉用户以后怎么避免这个报错）
"""

    user_prompt = f"""报错信息：
{error_text}

出错的代码（如果有）：
{code_context if code_context else "用户未提供代码片段"}
"""

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.3,  # 报错修复要精确，不要发挥
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("====== Python报错诊断助手 ======")
    print("请粘贴完整的红色报错信息（从 Traceback 到最后一行）：")
    lines = []
    while True:
        try:
            line = input()
            lines.append(line)
        except EOFError:
            break
    error_text = "\n".join(lines)
    
    print("\n如果方便，可以粘贴出错的代码片段（直接回车跳过）：")
    code_lines = []
    while True:
        try:
            line = input()
            if not line.strip():  # 空行表示结束
                break
            code_lines.append(line)
        except EOFError:
            break
    code_context = "\n".join(code_lines)
    
    result = fix_python_error(error_text, code_context)
    print("\n" + "="*50)
    print(result)
    print("="*50)