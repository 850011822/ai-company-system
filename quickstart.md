# 快速开始指南

## 5分钟快速部署

### 步骤1：准备环境

```bash
# 克隆或下载项目
cd ~/ai-company

# 复制环境配置
cp .env.example .env
```

### 步骤2：配置API

编辑`.env`文件，选择以下任一方式：

**方式A：使用OpenAI（推荐）**
```env
OPENAI_API_KEY=sk-xxx...
OPENAI_API_BASE=https://api.openai.com/v1
MODEL_NAME=gpt-4o-mini
```

**方式B：使用硅基流动（国内推荐）**
```env
OPENAI_API_KEY=your-silicon-key
OPENAI_API_BASE=https://api.siliconflow.cn/v1
MODEL_NAME=Qwen/Qwen2.5-7B-Instruct
```

**方式C：使用Ollama本地模型**
```env
OPENAI_API_KEY=dummy
OPENAI_API_BASE=http://localhost:11434/v1
MODEL_NAME=llama2
```

### 步骤3：一键部署

```bash
# 运行部署脚本
chmod +x setup.sh
./setup.sh
```

### 步骤4：启动系统

```bash
# 激活环境
source venv/bin/activate

# 运行主程序
python main.py
```

---

## Docker部署（可选）

### 快速启动

```bash
# 构建并运行
docker-compose up -d

# 查看日志
docker-compose logs -f
```

---

## 首次使用

系统启动后，输入数字选择功能：

```
1. 技术研究 - 让CTO研究特定技术
2. 市场分析 - 让CMO分析市场机会
3. 能力优化 - 让COO评估优化方向
```

示例：输入`1`后，输入研究主题如`AI Agent自动化`，系统将自动执行研究任务。

---

## 常见问题

| 问题 | 解决方案 |
|------|----------|
| API调用失败 | 检查`.env`中的API KEY是否正确 |
| 响应太慢 | 尝试使用更小的模型如`gpt-4o-mini` |
| 内存不足 | 关闭其他程序或使用更小的模型 |
| 网络超时 | 检查网络连接或使用国内API |

---

## 下一步

- 阅读完整教程：`教程.md`
- 查看配置说明：`config.yaml`
- 自定义Agent：修改`main.py`中的Agent定义
