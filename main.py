"""
AI 公司系统 - 主程序入口
基于CrewAI框架的多Agent协作系统
"""
import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from crewai.tools import tool
from langchain_community.tools import DuckDuckGoSearchResultsTool

# 加载环境变量
load_dotenv()

# ==================== 工具定义 ====================

@tool("web_search")
def web_search(query: str) -> str:
    """使用DuckDuckGo搜索最新信息"""
    search = DuckDuckGoSearchResultsTool()
    return search.run(query)

# ==================== Agent 工厂 ====================

def create_cto_agent():
    """创建 CTO Agent - 首席技术官"""
    return Agent(
        role="首席技术官 (CTO)",
        goal="持续追踪AI领域前沿技术，将新技术转化为公司能力",
        backstory="""
        您是公司的首席技术官，拥有深厚的技术背景和敏锐的技术洞察力。
        您的职责是确保公司始终掌握最新技术，保持竞争优势。
        您擅长技术调研、知识转化和技术路线规划。
        """,
        tools=[web_search],
        verbose=True,
        allow_delegation=False
    )

def create_coo_agent():
    """创建 COO Agent - 首席运营官"""
    return Agent(
        role="首席运营官 (COO)",
        goal="优化公司运营效率，持续提升系统能力",
        backstory="""
        您是公司的首席运营官，精通系统优化和流程改进。
        您的职责是评估现有能力，找出差距，制定并执行优化方案。
        您擅长数据分析、流程优化和质量控制。
        """,
        tools=[web_search],
        verbose=True,
        allow_delegation=False
    )

def create_cmo_agent():
    """创建 CMO Agent - 首席市场官"""
    return Agent(
        role="首席市场官 (CMO)",
        goal="敏锐洞察市场机会，识别商业变现可能",
        backstory="""
        您是公司的首席市场官，拥有敏锐的商业嗅觉和出色的分析能力。
        您的职责是扫描市场动态，发现机会，评估可行性。
        您擅长市场分析、竞争分析和商业策划。
        """,
        tools=[web_search],
        verbose=True,
        allow_delegation=False
    )

def create_cpo_agent():
    """创建 CPO Agent - 首席产品官"""
    return Agent(
        role="首席产品官 (CPO)",
        goal="将商业想法转化为可交付的产品和服务",
        backstory="""
        您是公司的首席产品官，拥有出色的产品开发和项目管理能力。
        您的职责是执行项目，开发产品，确保交付质量。
        您擅长产品设计、代码开发和项目管理。
        """,
        tools=[web_search],
        verbose=True,
        allow_delegation=False
    )

# ==================== 任务工厂 ====================

def create_research_task(agent, topic):
    """创建技术研究任务"""
    return Task(
        description=f"""
        请深入研究以下技术主题：{topic}

        要求：
        1. 搜索最新的技术发展和行业动态
        2. 分析该技术的核心原理和应用场景
        3. 评估该技术对公司能力的提升价值
        4. 提出具体的技术应用建议
        """,
        agent=agent,
        expected_output="详细的技术调研报告，包含核心发现、应用建议和实施计划"
    )

def create_market_task(agent, focus_area):
    """创建市场分析任务"""
    return Task(
        description=f"""
        请分析以下市场的商业机会：{focus_area}

        要求：
        1. 扫描市场现状和趋势
        2. 识别潜在客户群体和需求
        3. 评估竞争格局和机会
        4. 提出可行的商业模式建议
        """,
        agent=agent,
        expected_output="市场分析报告，包含机会评估和商业建议"
    )

def create_optimization_task(agent, focus_area):
    """创建优化任务"""
    return Task(
        description=f"""
        请分析并优化以下领域：{focus_area}

        要求：
        1. 评估当前能力水平
        2. 对比行业最佳实践
        3. 识别差距和改进点
        4. 制定优化方案
        """,
        agent=agent,
        expected_output="优化方案报告，包含差距分析和实施计划"
    )

# ==================== 工作流 ====================

def run_tech_research(topic):
    """运行技术研究工作流"""
    cto = create_cto_agent()
    task = create_research_task(cto, topic)

    crew = Crew(
        agents=[cto],
        tasks=[task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()
    return result

def run_market_analysis(focus_area):
    """运行市场分析工作流"""
    cmo = create_cmo_agent()
    task = create_market_task(cmo, focus_area)

    crew = Crew(
        agents=[cmo],
        tasks=[task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()
    return result

def run_optimization(focus_area):
    """运行优化工作流"""
    coo = create_coo_agent()
    task = create_optimization_task(coo, focus_area)

    crew = Crew(
        agents=[coo],
        tasks=[task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()
    return result

# ==================== 主程序 ====================

if __name__ == "__main__":
    print("=" * 60)
    print("       AI 公司系统 - 自主运营平台")
    print("=" * 60)
    print()
    print("请选择运行模式：")
    print("1. 技术研究 (CTO)")
    print("2. 市场分析 (CMO)")
    print("3. 能力优化 (COO)")
    print("4. 退出")
    print()

    choice = input("请输入选项 (1-4): ")

    if choice == "1":
        topic = input("请输入研究主题: ")
        print("\n正在启动技术研究...\n")
        result = run_tech_research(topic)
        print("\n" + "=" * 60)
        print("研究结果：")
        print("=" * 60)
        print(result)

    elif choice == "2":
        focus = input("请输入分析领域: ")
        print("\n正在启动市场分析...\n")
        result = run_market_analysis(focus)
        print("\n" + "=" * 60)
        print("分析结果：")
        print("=" * 60)
        print(result)

    elif choice == "3":
        focus = input("请输入优化领域: ")
        print("\n正在启动优化分析...\n")
        result = run_optimization(focus)
        print("\n" + "=" * 60)
        print("优化建议：")
        print("=" * 60)
        print(result)

    else:
        print("感谢使用！")
