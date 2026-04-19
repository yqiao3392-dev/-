import streamlit as st
import os
import time

# ================= 1. 页面全局配置 =================
st.set_page_config(page_title="硅基陪伴 | 具身智能选型决策中枢", layout="wide", initial_sidebar_state="expanded")

# ================= 2. 深度定制精致 UI =================
st.markdown("""
    <style>
    /* 引入渐变背景与专业字体 */
    .main { background: linear-gradient(180deg, #F0F4F8 0%, #F7F9FB 100%); }
    
    /* 大厂风 Hero Section 标题 */
    .hero-title {
        font-family: 'Inter', sans-serif;
        font-size: 48px;
        font-weight: 800;
        color: #0F172A;
        text-align: center;
        margin-top: 40px;
        letter-spacing: -1px;
    }
    .hero-subtitle {
        font-size: 18px;
        color: #64748B;
        text-align: center;
        margin-bottom: 40px;
    }

    /* 核心选型卡片 */
    .st-card {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        padding: 30px;
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05);
        margin-bottom: 30px;
    }

    /* 醒目的 Hero 按钮 */
    .big-button-container {
        display: flex;
        justify-content: center;
        margin-bottom: 60px;
    }
    
    /* 强制覆盖 Streamlit 按钮样式使其更“大” */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #1E3A8A 0%, #3B82F6 100%) !important;
        color: white !important;
        padding: 20px 60px !important;
        font-size: 24px !important;
        font-weight: 700 !important;
        border-radius: 50px !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(30, 58, 138, 0.3) !important;
        transition: all 0.3s ease !important;
        height: auto !important;
        width: auto !important;
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 25px rgba(30, 58, 138, 0.4) !important;
    }

    /* 产品矩阵微调 */
    .product-caption {
        font-weight: 600;
        color: #1E293B;
        margin-top: 10px;
        text-align: center;
    }
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

# ================= 3. 页面逻辑 =================

# --- 3.1 首页展示：公司视角的选型入口 ---
if st.session_state.step == "概念导入":
    # Hero 头部
    st.markdown('<div class="hero-title">寻找最契合您的硅基伴侣</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">基于多维需求建模的数字化具身智能选型决策平台</div>', unsafe_allow_html=True)
    
    # 醒目按钮
    col_btn_l, col_btn_m, col_btn_r = st.columns([1, 2, 1])
    with col_btn_m:
        st.button("立即开启数字化选型测评 ⚡", on_click=set_step, args=("智能测评",))

    # 平台价值说明
    st.markdown("""
        <div class="st-card" style="text-align: center;">
            <p style="color: #475569; font-size: 16px;">
                <b>公司视角建议：</b> 在购入昂贵的具身智能产品前，建议您预先进行此测评。<br>
                我们将通过科学的算法逻辑，对比您的隐私阈值、家庭结构及情感需求，为您推荐最合适的硬件形态与服务方案。
            </p>
        </div>
    """, unsafe_allow_html=True)

    # 纵向流动内容：视频展示
    st.markdown("### 📽️ 技术演示与愿景")
    col_v_l, col_v_m, col_v_r = st.columns([1, 4, 1])
    with col_v_m:
        st.markdown("""
        <iframe src="//player.bilibili.com/player.html?bvid=BV1mNdfBJEfT&page=1&autoplay=0" 
                style="width:100%; height:450px; border-radius:16px; box-shadow: 0 20px 50px rgba(0,0,0,0.1);" 
                frameborder="no" scrolling="no"></iframe>
        """, unsafe_allow_html=True)

    # 纵向流动内容：产品矩阵
    st.write("\n\n")
    st.markdown("### 🌐 核心推荐矩阵（持续更新中）")
    st.markdown("<p style='color: #64748B;'>以下为您展示平台当前已接入的具身智能旗舰型号：</p>", unsafe_allow_html=True)
    
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

# --- 3.2 智能需求测评 ---
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

        if st.form_submit_button("生成专属分析报告 🚀"):
            # 匹配逻辑
            if "儿童" in q_func or "有孩" in q_living: persona = "亲子伴学派"
            elif "老人" in q_func or "多代" in q_living or "要求纯物理" in q_privacy: persona = "传统保守派"
            elif ("独居" in q_living or "非常频繁" in q_lonely) and ("15000" in q_price): persona = "高知尝鲜派"
            else: persona = "普惠务实派"
            
            st.session_state.user_responses = {"persona": persona, "privacy": q_privacy, "price": q_price, "func": q_func}
            set_step("结论分析")
            st.rerun()

# --- 3.3 结论分析 ---
elif st.session_state.step == "结论分析":
    if not st.session_state.user_responses:
        st.warning("请先完成测评。")
        st.button("前往测评", on_click=set_step, args=("智能测评",))
    else:
        resp = st.session_state.user_responses
        persona = resp.get("persona")
        
        st.title(f"📊 选型分析结论：{persona}")
        
        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric("精准画像", persona)
        with m2:
            st.metric("隐私安全等级", resp['privacy'])
        with m3:
            st.metric("匹配方案建议", "建议购入")

        st.write("\n")
        # 结构化输出
        col_rec_l, col_rec_r = st.columns([1, 1.5])
        with col_rec_l:
            if persona == "高知尝鲜派": display_product_image("optimus.jpg", "推荐方案：Tesla Optimus")
            elif persona == "亲子伴学派": display_product_image("ebox.jpg", "推荐方案：EBO X")
            elif persona == "普惠务实派": display_product_image("ropet.jpg", "推荐方案：Ropet")
            else: display_product_image("ebox.jpg", "推荐方案：适老看护版")
        
        with col_rec_r:
            st.markdown(f"""
                <div class="st-card">
                    <h4>💼 专家级配置单 (PRD)</h4>
                    <ul style="line-height: 2;">
                        <li><b>推荐型号：</b> {persona}适配款</li>
                        <li><b>主打卖点：</b> 解决 {resp['func']} 的核心痛点</li>
                        <li><b>隐私建议：</b> 强制执行 {resp['privacy']} 模式</li>
                        <li><b>价格参考：</b> 符合您的预算区间</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)
            st.button("查看全天候模拟演示 🎬", on_click=set_step, args=("场景演练",))

# --- 3.4 场景演练 ---
elif st.session_state.step == "场景演练":
    st.title("🎬 模拟体验中心")
    st.info("基于选型建议，为您模拟真实的一天...")
    # (此部分逻辑与之前保持一致，可按需填充文字卡片)
    st.button("↺ 返回首页", on_click=set_step, args=("概念导入",))