# 🛡️ WebSecGuard：SQL 注入检测演示系统

一个基于 Flask 的 SQL 注入防护项目，结合 Docker 实现本地安全演示部署。用户可在登录页面测试常见注入 Payload，系统通过参数化查询实现有效防御。

---

## 🚀 项目亮点

- 模拟 SQL 注入漏洞 + 演示如何修复
- 使用参数化查询防御注入攻击
- 使用 Docker 完成项目容器化部署
- 提供登录页面，可输入 payload 测试注入
- 安装简单，运行快速，适合教学/练习/展示

---

## 📦 技术栈

| 技术 | 用途 |
|------|------|
| Python | 项目开发语言 |
| Flask | Web 框架 |
| SQLite | 简单用户数据库 |
| Docker | 容器化部署 |
| HTML | 登录页面界面 |

---

## 📂 项目结构

```bash
WebSecGuard/
├── app.py                 # Flask 应用主文件
├── templates/
│   └── login.html         # 登录页面（有注入点）
├── requirements.txt       # 依赖文件
├── Dockerfile             # 容器化配置
├── .dockerignore          # 构建忽略项
└── README.md              # 项目说明文档
