import streamlit as st

# ================= 页面全局配置 =================
st.set_page_config(page_title="硅基陪伴 | 项目执行摘要", layout="wide")
import streamlit as st

# 1. 页面配置
# st.set_page_config(page_title="...", layout="wide")

# 2. 读取并注入外部 CSS 样式的标准函数
def load_css(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"未能找到样式文件: {file_name}，请检查路径。")

# 调用该函数，路径需要根据你的实际目录结构调整
# 如果你在 pages 文件夹下的脚本中调用，路径可能是 "../style/custom.css"
load_css("style/custom.css") 

# ================= 下面是你原本的业务代码 =================
# st.title("...")








# ================= 注入高级商务与学术风 CSS =================
st.markdown("""
    <style>
    /* 全局背景色调优化 */
    .main { background-color: #FAFAFA; }
    
    /* 核心标题区样式 */
    .hero-title {
        font-family: 'Helvetica Neue', 'Arial', sans-serif;
        font-size: 42px;
        font-weight: 700;
        color: #1A2B4C;
        margin-bottom: 10px;
        letter-spacing: 1px;
    }
    .hero-subtitle {
        font-size: 18px;
        color: #555555;
        font-weight: 300;
        margin-bottom: 30px;
        line-height: 1.6;
    }
    
    /* 数据指标卡片样式 */
    .metric-container {
        background-color: #FFFFFF;
        border-radius: 8px;
        padding: 20px;
        border-top: 4px solid #1E3A8A;
        box-shadow: 0 4px 12px rgba(0,0,0,0.04);
        text-align: center;
        margin-bottom: 20px;
    }
    .metric-value { font-size: 32px; font-weight: 700; color: #1E3A8A; }
    .metric-label { font-size: 14px; color: #666666; margin-top: 8px; font-weight: 500; }
    
    /* 痛点与解决方案卡片 */
    .feature-card {
        background-color: #FFFFFF;
        padding: 24px;
        border-radius: 6px;
        border: 1px solid #EBEBEB;
        box-shadow: 0 2px 6px rgba(0,0,0,0.02);
        height: 100%;
        transition: transform 0.2s;
    }
    .feature-card:hover { transform: translateY(-5px); box-shadow: 0 6px 15px rgba(0,0,0,0.08); }
    .feature-title { font-size: 18px; font-weight: 600; color: #1A2B4C; margin-bottom: 12px; }
    .feature-text { font-size: 14px; color: #555555; line-height: 1.6; }
    
    /* 占位符样式 */
    .video-placeholder {
        background-color: #EAEAEA;
        border-radius: 8px;
        height: 320px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #888888;
        font-weight: 500;
        border: 1px dashed #B0B0B0;
    }
    </style>
""", unsafe_allow_html=True)

# ================= Hero Section (顶部视觉冲击区) =================
col_text, col_media = st.columns([1.2, 1])

with col_text:
    st.markdown('<div class="hero-title">硅基陪伴 Project</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">成都市具身智能陪伴机器人消费需求与市场潜力分析<br>—— 基于“体验前置”理念的市场转化落地演示平台</div>', unsafe_allow_html=True)
    
    st.markdown("""
    **项目背景与目标：** 在“人工智能+”与“孤独经济”背景下，具身智能陪伴机器人作为融合大语言模型与物理实体的新型终端，正处于创新扩散的关键跨越期。针对当前市场**“认知热、转化冷”**的现实困境，本项目融合了 12,000 余条全网文本的 NLP 情感分析与 693 份成都市中心城区实地调研样本。
    
    依托 **XGBoost 归因模型** 与 **K-means 聚类算法**，本平台致力于将抽象的市场研究结论转化为可视化的商业应用工具，为破解技术落地难、消费激活弱的问题提供数字化解决方案。
    """)
    
    st.write("") # 留白
    
    # 引导按钮
    try:
        st.page_link("pages/2_🤖_智能选型.py", label="进入消费者智能选型评测系统 ➡", icon="🎯")
    except:
        st.info("👈 请通过左侧导航栏进入【智能选型】模块体验核心功能。")

with col_media:
    # 强烈建议答辩时替换为真实的场景宣发视频或你们团队去线下实体店调研的照片
    st.markdown("""
        <div class="video-placeholder">
            [封面多媒体预留区]<br>建议嵌入团队实地调研过程的高清照片拼图，<br>或目标竞品（如Loona/Ebo X）的概念演示视频。
        </div>
    """, unsafe_allow_html=True)
    # 实际应用时替换为：st.video("assets/videos/intro_video.mp4") 或 st.image("assets/images/hero_image.jpg")

st.divider()

# ================= 数据资产展示区 (展现专业壁垒) =================
st.markdown("<h3 style='color: #1A2B4C; font-size: 20px; margin-bottom: 20px;'>核心研究数据支撑</h3>", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown('<div class="metric-container"><div class="metric-value">12,000+</div><div class="metric-label">全网舆情文本采集量</div></div>', unsafe_allow_html=True)
with m2:
    st.markdown('<div class="metric-container"><div class="metric-value">693 份</div><div class="metric-label">成都市有效实地样本</div></div>', unsafe_allow_html=True)
with m3:
    st.markdown('<div class="metric-container"><div class="metric-value">84.5%</div><div class="metric-label">XGBoost模型预测准确率</div></div>', unsafe_allow_html=True)
with m4:
    st.markdown('<div class="metric-container"><div class="metric-value">4 大类</div><div class="metric-label">聚类识别核心消费客群</div></div>', unsafe_allow_html=True)

st.divider()

# ================= 核心商业逻辑展示区 =================
st.markdown("<h3 style='color: #1A2B4C; font-size: 20px; margin-bottom: 20px;'>全链路数字化解决方案</h3>", unsafe_allow_html=True)

f1, f2, f3 = st.columns(3)

with f1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">01 现实困境诊断与应对</div>
        <div class="feature-text">
            <b>痛点剖析：</b>当前市场存在明显的“认知—转化”断层，消费者对机器人的物理亲和力与隐私安全仍保有较高防御心理。<br><br>
            <b>策略建议：</b>企业需采取更务实的市场进入策略。通过“做减法”剥离冗余的昂贵算力，回归“情感慰藉”与“社交代偿”的核心产品诉求。
        </div>
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">02 客群动态聚类分层</div>
        <div class="feature-text">
            <b>模型引入：</b>突破传统人口统计学的单一维度，本平台整合了消费特征、技术准备度及隐私让渡意愿等多维变量。<br><br>
            <b>市场定位：</b>通过算法动态刻画“高知尝鲜派”、“亲子伴学派”、“普惠务实派”与“传统保守派”四大群体，助力企业明确早期消费主力。
        </div>
    </div>
    """, unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">03 研究成果落地转化</div>
        <div class="feature-text">
            <b>工具沉淀：</b>避免调研结论停留在纸面。本系统将复杂的购买意愿影响机制，提炼为直观的消费者交互工具。<br><br>
            <b>触点拓宽：</b>依据不同人群心理结构，精准匹配“高阶交互型”或“基础养成型”产品，以真实场景的沉浸体验有效瓦解大众观望壁垒。
        </div>
    </div>
    """, unsafe_allow_html=True)

st.write("\n")
st.markdown("<p style='text-align: center; color: #888; font-size: 13px; margin-top: 40px;'>Copyright © 2026 硅基陪伴项目组（全国大学生市场调查与分析大赛） | 核心研究成果展示平台</p>", unsafe_allow_html=True)