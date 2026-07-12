import os
from openai import OpenAI

API_KEY = "sk-b03ee845ba714658bf9eb17b081a0803"
BASE_URL = "https://api.deepseek.com"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

def generate_amazon_listing(product_name, features, target_platform="Amazon"):
    """
    生成跨境电商产品文案
    product_name: 中文产品名（如：便携式无线充电宝）
    features: 核心卖点（如：超薄、快充、大容量）
    target_platform: Amazon / Shopee / Temu
    """
    system_prompt = """You are a professional e-commerce copywriter specializing in Amazon and cross-border listings.
Your task is to write a compelling, SEO-friendly product title and bullet points in BOTH English and Chinese.

Output format must be strictly as follows:

=== ENGLISH VERSION ===
TITLE: [English title, optimized for Amazon search, 80-150 characters]
BULLET POINTS:
1. [Bullet point 1 in English]
2. [Bullet point 2 in English]
3. [Bullet point 3 in English]
4. [Bullet point 4 in English]
5. [Bullet point 5 in English]

=== 中文版本 ===
标题：[中文标题，含核心关键词]
卖点描述：
1. [中文卖点1]
2. [中文卖点2]
3. [中文卖点3]
4. [中文卖点4]
5. [中文卖点5]

=== PRODUCT FEATURES (Extracted) ===
[3-5 key feature keywords in English, comma separated]

=== TARGET KEYWORDS ===
[10-15 search keywords in English, comma separated]
"""
    user_prompt = f"""Product Name: {product_name}
Core Features: {features}
Target Platform: {target_platform}
Please generate a complete listing in the required format."""
    
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
    print("====== 跨境电商产品文案生成器 ======")
    product = input("请输入产品中文名称（如：便携式无线充电宝）：")
    features = input("请输入核心卖点（如：超薄、快充、大容量）：")
    platform = input("目标平台（Amazon/Shopee/Temu，默认Amazon）：") or "Amazon"
    
    result = generate_amazon_listing(product, features, platform)
    print("\n" + "="*50)
    print(result)
    print("="*50)