import os
from openai import OpenAI

API_KEY = "sk-b03ee845ba714658bf9eb17b081a0803"
BASE_URL = "https://api.deepseek.com"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

def generate_ppt_outline(topic, audience="大学生", duration=10):
    """
    生成PPT提纲
    topic: 演讲主题
    audience: 听众对象（大学生/老师/企业）
    duration: 演讲时长（分钟）
    """
    system_prompt = """你是一个专业的PPT结构设计师和演讲教练。
你的任务是根据用户提供的主题，生成一份**逻辑清晰、结构完整、可直接使用的PPT提纲**。

输出格式必须严格遵循以下结构：
=== 封面页 ===
主标题：xxx
副标题：xxx

=== 目录页 ===
1. xxx
2. xxx
3. xxx
4. xxx
5. xxx（总结/问答）

=== 内容页（共N页） ===
【第X页】
标题：xxx
要点：
• 要点1
• 要点2
• 要点3
备注/过渡句：xxx

【第X+1页】
...（以此类推）

=== 结束页 ===
总结：xxx
金句/金句：xxx
Q&A提示：xxx

=== 演讲备注 ===
（给演讲者的建议，比如：哪页需要停顿、哪页需要互动、时间分配建议）
"""
    user_prompt = f"""主题：{topic}
听众对象：{audience}
演讲时长：{duration}分钟
请生成一份完整的PPT提纲。"""
    
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("====== PPT/演讲稿提纲生成器 ======")
    topic = input("请输入演讲/PPT主题：")
    audience = input("请输入听众对象（如：大学生/老师/企业）：")
    duration = input("请输入演讲时长（分钟，如10）：")
    
    result = generate_ppt_outline(topic, audience, duration)
    print("\n" + "="*50)
    print(result)
    print("="*50)