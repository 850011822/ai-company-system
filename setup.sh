#!/bin/bash
# AI公司系统 - 快速启动脚本

echo "========================================"
echo "  AI公司系统 - 快速部署脚本"
echo "========================================"
echo ""

# 检查Python版本
echo "[1/5] 检查Python环境..."
if ! command -v python3 &> /dev/null; then
    echo "错误: 未找到Python3，请先安装Python 3.11+"
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "当前Python版本: $PYTHON_VERSION"

# 创建虚拟环境
echo ""
echo "[2/5] 创建虚拟环境..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "虚拟环境已创建"
else
    echo "虚拟环境已存在"
fi

# 激活虚拟环境
echo ""
echo "[3/5] 安装依赖..."
source venv/bin/activate

# 升级pip
pip install --upgrade pip

# 安装依赖
pip install -r requirements.txt

# 创建必要目录
echo ""
echo "[4/5] 初始化目录结构..."
mkdir -p memory logs output data

# 配置检查
echo ""
echo "[5/5] 环境配置..."
if [ ! -f ".env" ]; then
    echo "请在以下选项中选择API配置:"
    echo "1. OpenAI API"
    echo "2. 硅基流动 API"
    echo "3. Ollama 本地模型"
    echo "4. 跳过（稍后手动配置）"

    read -p "请输入选项 (1-4): " choice

    case $choice in
        1)
            echo "请在 .env 文件中配置以下内容:"
            echo "OPENAI_API_KEY=your_key_here"
            echo "OPENAI_API_BASE=https://api.openai.com/v1"
            echo "MODEL_NAME=gpt-4o-mini"
            ;;
        2)
            echo "请在 .env 文件中配置以下内容:"
            echo "OPENAI_API_KEY=your_silicon_key"
            echo "OPENAI_API_BASE=https://api.siliconflow.cn/v1"
            echo "MODEL_NAME=Qwen/Qwen2.5-7B-Instruct"
            ;;
        3)
            echo "请在 .env 文件中配置以下内容:"
            echo "OPENAI_API_KEY=dummy"
            echo "OPENAI_API_BASE=http://localhost:11434/v1"
            echo "MODEL_NAME=llama2"
            ;;
        *)
            echo "跳过配置，请在运行前创建 .env 文件"
            ;;
    esac

    # 创建示例.env文件
    cat > .env.example << 'EOF'
# OpenAI配置
OPENAI_API_KEY=your_api_key_here
OPENAI_API_BASE=https://api.openai.com/v1
MODEL_NAME=gpt-4o-mini

# 可选：硅基流动配置
# OPENAI_API_KEY=your_silicon_key
# OPENAI_API_BASE=https://api.siliconflow.cn/v1
# MODEL_NAME=Qwen/Qwen2.5-7B-Instruct

# 可选：Ollama本地配置
# OPENAI_API_KEY=dummy
# OPENAI_API_BASE=http://localhost:11434/v1
# MODEL_NAME=llama2
EOF

    echo ""
    echo "示例配置已保存到 .env.example"
fi

echo ""
echo "========================================"
echo "  部署完成！"
echo "========================================"
echo ""
echo "下一步操作："
echo "1. 复制 .env.example 为 .env 并配置API密钥"
echo "2. 运行: source venv/bin/activate"
echo "3. 运行: python main.py"
echo ""
echo "或使用Docker运行:"
echo "  docker build -t ai-company ."
echo "  docker run -it ai-company"
echo ""
