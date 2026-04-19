import streamlit as st
import os

# ================= 1. 页面全局配置 =================
st.set_page_config(page_title="硅基陪伴 | 具身智能选型决策中枢", layout="wide", initial_sidebar_state="expanded")

# ================= 2. 顶级科技公司风格 CSS 注入 =================
st.markdown("""
    <style>
    /* 引入渐变背景与专业字体 */
    .main { background: linear-gradient(180deg, #F0F4F8 0%, #F7F9FB 100%); }
    
    /* 页面标题样式 */
    .hero-title {
        font-family: 'Inter', sans-serif;
        font-size: 52px;
        font-weight: 800;
        color: #0F172A;
        text-align: center;
        margin-top: 50px;
        letter-spacing: -1.5px;
    }
    .hero-subtitle {
        font-size: 20px;
        color: #64748B;
        text-align: center;
        margin-bottom: 50px;
    }

    /* 高级感卡片 */
    .st-card {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(15px);
        padding: 35px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.5);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.05);
        margin-bottom: 30px;
    }

    /* 按钮居中容器 */
    .center-btn-container {
        display: flex;
        justify-content: center;
        width: 100%;
        margin: 40px 0;
    }

    /* 核心按钮样式覆盖 (所有按钮统一效果) */
    div.stButton > button, div[data-testid="stFormSubmitButton"] > button {
        background: linear-gradient(135deg, #1E3A8A 0%, #3B82F6 100%) !important;
        color: white !important;
        padding: 18px 60px !important;
        font-size: 22px !important;
        font-weight: 700 !important;
        border-radius: 50px !important;
        border: none !important;
        box-shadow: 0 8px 20px rgba(30, 58, 138, 0.25) !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        display: block !important;
        margin: 0 auto !important; /* 强制内部居中 */
    }
    
    div.stButton > button:hover, div[data-testid="stFormSubmitButton"] > button:hover {
        transform: scale(1.05) translateY(-3px) !important;
        box-shadow: 0 12px 30px rgba(30, 58, 138, 0.35) !important;
    }

    /* 指标看板样式 */
    .metric-container {
        text-align: center;
        padding: 20px;
        background: #F1F5F9;
        border-radius: 12px;
    }
    .metric-label { font-size: 14px; color: #64748B; font-weight: 600; text-transform: uppercase; }
    .metric-value { font-size: 28px; font-weight: 800; color: #1E3A8A; margin-top: 5px; }

    /* PRD 列表样式 */
    .prd-item {
        display: flex;
        align-items: center;
        padding: 12px 0;
        border-bottom: 1px solid #E2E8F0;
    }
    .prd-item b { color: #1E293B; margin-right: 10px; min-width: 100px; }
    </style>
""", unsafe_allow_html=True)

# 状态管理
if 'step' not in st.session_state: st.session_state.step = "概念导入"
if 'user_responses' not in st.session_state: st.session_state.user_responses = {}

def set_step(name): st.session_state.step = name

# 图片加载防崩函数
def display_product_image(file_name, caption):
    try:
        if os.path.exists(file_name):
            st.image(file_name, caption=caption, use_container_width=True)
        elif os.path.exists(f"assets/products/{file_name}"):
            st.image(f"assets/products/{file_name}", caption=caption, use_container_width=True)
        else:
            st.info(f"🖼️ {caption} (提示：未找到图片 {file_name})")
    except Exception:
        pass

# ================= 3. 核心页面路由 =================

# --- 首页：极致科技感入口 ---
if st.session_state.step == "概念导入":
    st.markdown('<div class="hero-title">寻找最契合您的硅基伴侣</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">硅基陪伴：基于多维需求建模的具身智能选型决策平台</div>', unsafe_allow_html=True)
    
    # 居中大按钮
    st.button("立即开启数字化选型测评 ⚡", on_click=set_step, args=("智能测评",))

    st.markdown("""
        <div class="st-card" style="text-align: center;">
            <p style="color: #475569; font-size: 16px; max-width: 800px; margin: 0 auto;">
                <b>平台愿景：</b> 在购入昂贵的具身智能产品前，建议您预先进行此测评。我们通过科学的算法逻辑，对比您的隐私阈值、家庭结构及情感需求，为您推荐最合适的硬件形态与服务方案。
            </p>
        </div>
    """, unsafe_allow_html=True)

    # 视频区域
    col_v_l, col_v_m, col_v_r = st.columns([1, 4, 1])
    with col_v_m:
        st.markdown("""
        <iframe src="//player.bilibili.com/player.html?bvid=BV1mNdfBJEfT&page=1&autoplay=0" 
                style="width:100%; height:450px; border-radius:20px; box-shadow: 0 25px 55px rgba(0,0,0,0.12);" 
                frameborder="no" scrolling="no"></iframe>
        """, unsafe_allow_html=True)

    st.write("\n\n")
    st.markdown("### 🌐 全球具身智能旗舰矩阵")
    p1, p2, p3, p4 = st.columns(4)
    with p1:
        display_product_image("optimus.jpg", "Tesla Optimus")
        st.caption("**通用能力标杆**")
    with p2:
        display_product_image("loona.jpg", "Loona 智能宠")
        st.caption("**情感代偿先驱**")
    with p3:
        display_product_image("ebox.jpg", "Enabot EBO X")
        st.caption("**全屋智能管家**")
    with p4:
        display_product_image("ropet.jpg", "Ropet 仿生伴侣")
        st.caption("**极简治愈体验**")

# --- 测评页：清爽表单 ---
elif st.session_state.step == "智能测评":
    st.title("🎯 数字化特征采集")
    st.markdown("<p style='color:#64748B;'>请完成以下评估，系统将实时计算您的特征向量并映射至最优产品方案。</p>", unsafe_allow_html=True)
    
    with st.form("survey"):
        st.markdown("#### 1. 生活场景特征")
        q_living = st.radio("您的家庭居住形态？", ["独居 (一人居住)", "二人世界 (无子女)", "有孩家庭 (有18岁以下子女)", "多代同堂 (与老人同住)"])
        q_lonely = st.select_slider("您对日常陪伴的需求频率？", options=["极少", "偶尔", "经常", "非常频繁"])
        
        st.markdown("#### 2. 技术与安全偏好")
        q_func = st.radio("您购买机器人的核心驱动力？", ["情感慰藉", "儿童教育/安全", "老人健康监测", "纯粹娱乐/解压"])
        q_privacy = st.select_slider("数据隐私容忍度？", options=["完全接受云端", "仅接受端侧离线", "要求纯物理隔离"])
        
        st.markdown("#### 3. 消费力决策")
        q_price = st.selectbox("购买预算上限？", ["3000元及以下", "3001-8000元", "8001-15000元", "15000元以上"])
        q_pay = st.radio("倾向的付费模式？", ["硬件买断制", "HaaS 功能订阅制", "共享租赁模式"])

        # 此按钮会自动继承 CSS 样式并居中
        st.form_submit_button("生成专属分析报告 🚀")

        if st.form_submit_button:
            # 简单逻辑判断
            if "儿童" in q_func or "有孩" in q_living: persona = "亲子伴学派"
            elif "老人" in q_func or "多代" in q_living or "要求纯物理" in q_privacy: persona = "传统保守派"
            elif ("独居" in q_living or "非常频繁" in q_lonely) and ("15000" in q_price): persona = "高知尝鲜派"
            else: persona = "普惠务实派"
            
            st.session_state.user_responses = {
                "persona": persona, 
                "privacy": q_privacy, 
                "price": q_price, 
                "func": q_func,
                "pay": q_pay
            }
            set_step("结论分析")
            st.rerun()

# --- 结论分析页：深度视觉美化 ---
elif st.session_state.step == "结论分析":
    if not st.session_state.user_responses:
        st.warning("请先完成测评。")
        st.button("前往测评", on_click=set_step, args=("智能测评",))
    else:
        resp = st.session_state.user_responses
        persona = resp.get("persona")
        
        st.markdown(f'<div class="hero-title" style="font-size: 36px; margin-top: 20px;">选型分析报告：{persona}</div>', unsafe_allow_html=True)
        
        # 仪表盘看板
        kpi_col1, kpi_col2, kpi_col3 = st.columns(3)
        with kpi_col1:
            st.markdown(f'<div class="metric-container"><div class="metric-label">精准客群画像</div><div class="metric-value">{persona}</div></div>', unsafe_allow_html=True)
        with kpi_col2:
            st.markdown(f'<div class="metric-container"><div class="metric-label">数据隐私等级</div><div class="metric-value">{resp["privacy"]}</div></div>', unsafe_allow_html=True)
        with kpi_col3:
            st.markdown(f'<div class="metric-container"><div class="metric-label">推荐变现模式</div><div class="metric-value">{resp["pay"]}</div></div>', unsafe_allow_html=True)

        st.write("\n")
        
        # 详细规格单
        col_rec_l, col_rec_r = st.columns([1, 1.3])
        with col_rec_l:
            st.markdown("##### 📍 匹配硬件形态")
            if persona == "高知尝鲜派": display_product_image("optimus.jpg", "旗舰选型：Tesla Optimus")
            elif persona == "亲子伴学派": display_product_image("ebox.jpg", "家庭中枢：Enabot EBO X")
            elif persona == "普惠务实派": display_product_image("ropet.jpg", "治愈伴侣：Ropet")
            else: display_product_image("ebox.jpg", "看护专家：适老增强版")
        
        with col_rec_r:
            st.markdown(f"""
                <div class="st-card">
                    <h4 style="color:#1E3A8A; margin-top:0;">📋 专家级配置单 (PRD)</h4>
                    <div class="prd-item"><b>核心卖点</b> 解决 {resp['func']} 的核心社交痛点</div>
                    <div class="prd-item"><b>硬件方案</b> 适配 {persona} 的专属物理形态</div>
                    <div class="prd-item"><b>交互逻辑</b> 优先执行 {resp['privacy']} 安全协议</div>
                    <div class="prd-item"><b>部署建议</b> 采用 {resp['pay']} 实现成本最优化</div>
                    <p style="font-size: 13px; color: #94A3B8; margin-top: 20px;">* 以上建议基于成都市具身智能市场研究模型动态生成</p>
                </div>
            """, unsafe_allow_html=True)
            st.button("启动场景模拟演示 🎬", on_click=set_step, args=("场景演练",))

# --- 场景演练页 ---
elif st.session_state.step == "场景演练":
    st.title("🎬 沉浸式应用演练")
    st.info("基于选型建议，正在为您还原真实的生活交互切面...")
    
    # 这里可以继续添加精致的时间轴或者文字卡片
    st.button("↺ 返回选型首页", on_click=set_step, args=("概念导入",))