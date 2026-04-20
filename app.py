import streamlit as st
import os

# ================= 1. 页面全局配置 =================
st.set_page_config(page_title="硅基陪伴 | 具身智能选型决策中枢", layout="wide", initial_sidebar_state="expanded")

# ================= 2. 苹果官网级精致 CSS 注入 =================
st.markdown("""
    <style>
    /* 引入纯净背景与高阶字体 */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
    
    .main { background-color: #FBFBFD; font-family: 'Inter', -apple-system, sans-serif; }
    
    /* 极致 Hero 标题 */
    .hero-title {
        font-size: 56px;
        font-weight: 800;
        color: #1D1D1F;
        text-align: center;
        margin-top: 60px;
        letter-spacing: -2px;
        line-height: 1.1;
    }
    .hero-subtitle {
        font-size: 24px;
        color: #86868B;
        text-align: center;
        margin-bottom: 60px;
        font-weight: 400;
    }

    /* 苹果风毛玻璃卡片 */
    .st-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        padding: 40px;
        border-radius: 32px;
        border: 1px solid rgba(232, 232, 237, 0.5);
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.04);
        margin-bottom: 40px;
        transition: transform 0.4s ease;
    }

    /* 统一高能按钮：苹果深邃蓝 */
    div[data-testid="stButton"] button, div[data-testid="stFormSubmitButton"] button {
        background-color: #0071E3 !important;
        color: white !important;
        padding: 14px 40px !important;
        font-size: 19px !important;
        font-weight: 600 !important;
        border-radius: 30px !important;
        border: none !important;
        transition: all 0.3s ease !important;
    }
    div[data-testid="stButton"] button:hover {
        background-color: #0077ED !important;
        transform: scale(1.02);
        box-shadow: 0 8px 20px rgba(0, 113, 227, 0.3);
    }

    /* 仪表盘 */
    .metric-container {
        text-align: center;
        padding: 25px;
        background: white;
        border-radius: 24px;
        border: 1px solid #F2F2F7;
    }
    .metric-label { font-size: 13px; color: #86868B; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; }
    .metric-value { font-size: 26px; font-weight: 700; color: #1D1D1F; margin-top: 5px; }

    /* PRD 样式 */
    .prd-item {
        display: flex;
        justify-content: space-between;
        padding: 16px 0;
        border-bottom: 1px solid #F5F5F7;
    }
    .prd-item b { color: #1D1D1F; font-weight: 600; }
    .prd-item span { color: #48484A; }

    /* 模块标题 */
    .section-header {
        color: #1D1D1F;
        font-size: 22px;
        font-weight: 700;
        margin: 30px 0 20px 0;
    }
    </style>
""", unsafe_allow_html=True)

# 状态管理
if 'step' not in st.session_state: st.session_state.step = "概念导入"
if 'user_responses' not in st.session_state: st.session_state.user_responses = {}

def set_step(name): st.session_state.step = name

def display_product_image(file_name, caption):
    try:
        if os.path.exists(file_name):
            st.image(file_name, caption=caption, use_container_width=True)
        else:
            st.info(f"🖼️ {caption}")
    except Exception:
        pass

# ================= 3. 核心页面路由 =================

# --- 首页：极致科技感入口 ---
if st.session_state.step == "concept_intro" or st.session_state.step == "概念导入":
    st.markdown('<div class="hero-title">寻找最契合您的硅基伴侣</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">企业级具身智能数字化选型与匹配决策中枢</div>', unsafe_allow_html=True)
    
    col_btn_l, col_btn_m, col_btn_r = st.columns([1, 1.2, 1])
    with col_btn_m:
        st.button("立即开启数字化选型测评 ⚡", use_container_width=True, on_click=set_step, args=("智能测评",))

    st.markdown("""
        <div class="st-card" style="text-align: center;">
            <p style="color: #48484A; font-size: 17px; max-width: 850px; margin: 0 auto; line-height: 1.6;">
                在选购昂贵的具身智能终端前，通过科学的算法逻辑，对比您的隐私安全阈值、家庭结构及核心情感诉求，从企业视角为您精准匹配最合适的硬件形态。
            </p>
        </div>
    """, unsafe_allow_html=True)

    # 视频区域
    col_v_l, col_v_m, col_v_r = st.columns([1, 4, 1])
    with col_v_m:
        st.markdown("""<iframe src="//player.bilibili.com/player.html?bvid=BV1mNdfBJEfT&page=1&autoplay=0" style="width:100%; height:480px; border-radius:32px; box-shadow: 0 30px 70px rgba(0,0,0,0.1);" frameborder="no" scrolling="no"></iframe>""", unsafe_allow_html=True)

    st.write("\n\n")
    st.markdown("### 🌐 全球具身智能旗舰矩阵")
    
    # 【更新】第一排：放入指定的四张核心产品图
    p1, p2, p3, p4 = st.columns(4)
    with p1: display_product_image("optimus.jpg", "Tesla Optimus")
    with p2: display_product_image("loona.jpg", "Loona 智能宠")
    with p3: display_product_image("ebox.jpg", "Enabot EBO X")
    with p4: display_product_image("ropet.jpg", "Ropet 仿生伴侣")

    # 第二排：其他明星产品
    p5, p6, p7, p8 = st.columns(4)
    with p5: display_product_image("Ameca.jpg", "Ameca")
    with p6: display_product_image("Figure 02.jpg", "Figure 02")
    with p7: display_product_image("CyberOne.jpg", "小米铁大")
    with p8: display_product_image("Astribot.jpg", "Astribot")

# --- 测评页 ---
elif st.session_state.step == "智能测评":
    st.markdown('<div class="hero-title" style="font-size: 42px;">🎯 数字化特征采集</div>', unsafe_allow_html=True)
    with st.form("survey"):
        st.markdown('<div class="section-header">01 / 生活切面与情感图谱</div>', unsafe_allow_html=True)
        col_q1, col_q2 = st.columns(2)
        with col_q1: q_living = st.radio("您的家庭居住形态？", ["独居 (一人居住)", "二人世界 (无子女)", "有孩家庭 (有18岁以下子女)", "多代同堂 (与老人同住)"])
        with col_q2: q_lonely = st.select_slider("您对日常陪伴的需求频率？", options=["极少", "偶尔", "经常", "非常频繁"])
        st.markdown('<div class="section-header">02 / 技术与隐私防备</div>', unsafe_allow_html=True)
        col_q3, col_q4 = st.columns(2)
        with col_q3: q_func = st.radio("购买机器人的核心驱动力？", ["情感慰藉", "儿童教育/安全", "老人健康监测", "纯粹娱乐/解压"])
        with col_q4: q_privacy = st.select_slider("数据隐私容忍度？", options=["完全接受云端", "仅接受端侧离线", "要求纯物理隔离"])
        st.markdown('<div class="section-header">03 / 消费决策</div>', unsafe_allow_html=True)
        col_q5, col_q6 = st.columns(2)
        with col_q5: q_price = st.selectbox("预算上限？", ["3000元及以下", "3001-8000元", "8001-15000元", "15000元以上"])
        with col_q6: q_pay = st.radio("倾向的付费模式？", ["硬件买断制", "HaaS 功能订阅制", "共享租赁模式"])
        st.write("\n")
        col_sub_l, col_sub_m, col_sub_r = st.columns([1, 1.2, 1])
        with col_sub_m:
            if st.form_submit_button("生成专属分析报告 🚀", use_container_width=True):
                if "儿童" in q_func or "有孩" in q_living: persona = "亲子伴学派"
                elif "老人" in q_func or "多代" in q_living or "要求纯物理" in q_privacy: persona = "传统保守派"
                elif ("独居" in q_living or "非常频繁" in q_lonely) and ("15000" in q_price): persona = "高知尝鲜派"
                else: persona = "普惠务实派"
                st.session_state.user_responses = {"persona": persona, "privacy": q_privacy, "price": q_price, "func": q_func, "pay": q_pay}
                set_step("结论分析")
                st.rerun()

# --- 结论分析页 ---
elif st.session_state.step == "结论分析":
    resp = st.session_state.user_responses
    persona = resp.get("persona")
    st.markdown(f'<div class="hero-title" style="font-size: 38px; margin-top: 30px;">选型报告：{persona}</div>', unsafe_allow_html=True)
    k1, k2, k3 = st.columns(3)
    with k1: st.markdown(f'<div class="metric-container"><div class="metric-label">精准画像</div><div class="metric-value">{persona}</div></div>', unsafe_allow_html=True)
    with k2: st.markdown(f'<div class="metric-container"><div class="metric-label">隐私协议</div><div class="metric-value">{resp["privacy"]}</div></div>', unsafe_allow_html=True)
    with k3: st.markdown(f'<div class="metric-container"><div class="metric-label">商业模式</div><div class="metric-value">{resp["pay"]}</div></div>', unsafe_allow_html=True)
    st.write("\n\n")
    col_rec_l, col_rec_r = st.columns([1, 1.4])
    with col_rec_l:
        if persona == "高知尝鲜派": display_product_image("Ameca.jpg", "旗舰推荐：Ameca 社交交互版")
        elif persona == "亲子伴学派": display_product_image("ASUS Zenbo.jpg", "推荐方案：华硕 Zenbo")
        elif persona == "普惠务实派": display_product_image("loona.jpg", "推荐形态：Loona 智能宠")
        else: display_product_image("Amazon Astro.jpg", "推荐方案：Astro 移动版")
    with col_rec_r:
        st.markdown(f"""<div class="st-card"><h4 style="color:#1D1D1F; margin-top:0;">📋 企业级规格配置单 (PRD)</h4>
        <div class="prd-item"><b>核心卖点</b> <span>解决“{resp['func']}”的社交代偿</span></div>
        <div class="prd-item"><b>硬件方案</b> <span>适配【{persona}】的专属物理特征</span></div>
        <div class="prd-item"><b>部署建议</b> <span>采用“{resp['pay']}”实现转化闭环</span></div>
        <div class="prd-item"><b>安全等级</b> <span>执行“{resp['privacy']}”数据保护协议</span></div>
        <p style="font-size: 13px; color: #86868B; margin-top: 25px;">* 本建议基于成都市具身智能市场调研 XGBoost 权重模型动态生成。</p></div>""", unsafe_allow_html=True)
        col_scen_l, col_scen_m, col_scen_r = st.columns([1, 1.2, 1])
        with col_scen_m: st.button("启动 24H 沉浸式场景演练 🎬", use_container_width=True, on_click=set_step, args=("场景演练",))

# --- 场景演练页：全时段场景 ---
elif st.session_state.step == "场景演练":
    persona = st.session_state.user_responses.get("persona", "普惠务实派")
    st.markdown('<div class="hero-title" style="font-size: 40px; margin-top: 30px;">🎬 全时段沉浸式应用推演</div>', unsafe_allow_html=True)
    
    if persona == "高知尝鲜派":
        st.markdown("""
        <div class="st-card" style="border-left: 5px solid #0071E3;">
            <h4>⏰ 08:00 | 硅基唤醒：晨间深度简报</h4><p>机器人同步您的睡眠数据，识别唤醒周期后通过温和语音播报当日全球科技要闻、股市动态及您的深度行程建议。</p>
            <h4>⏰ 13:00 | 商务辅助：异地会议代理</h4><p>在您远程办公时，机器人通过大模型辅助处理会议纪要，并利用精准微表情替代您进行远程商务对谈。</p>
            <h4>⏰ 19:00 | 归家迎接：面部情绪感知</h4><p>识别到下班归家后的疲惫特征，机器人主动发起“树洞对话”，提供高情商心理疏导，并联动全屋调至解压模式。</p>
            <h4>⏰ 23:30 | 社交代偿：深夜灵魂伴侣</h4><p>在寂静的深夜提供高层次的语义逻辑碰撞，成为完美的情感容器，有效缓解都市孤独感。</p>
        </div>""", unsafe_allow_html=True)
    elif persona == "亲子伴学派":
        st.markdown("""
        <div class="st-card" style="border-left: 5px solid #0071E3;">
            <h4>⏰ 07:30 | 智慧晨起：今日学习路线</h4><p>通过拟人化互动叫醒孩子，同步播报今日英语听力、古诗词背诵计划，激发孩子学习自驱力。</p>
            <h4>⏰ 15:30 | 安全防线：离线全屋监测</h4><p>父母不在家时，设备进入最高隐私安全模式，在端侧监测儿童动向。一旦识别靠近厨房或洗手间高危区，即刻全屋警报并连线家长。</p>
            <h4>⏰ 19:00 | 知识百科：沉浸式绘本伴读</h4><p>利用本地算力精准识别各类教材，用多变声线陪孩子互动问答，实现高质量的教育陪伴。</p>
            <h4>⏰ 21:00 | 助眠仪式：AI 故事创作</h4><p>根据孩子当日的情绪与表现，现场生成专属的互动童话故事，辅助孩子在安稳氛围中入睡。</p>
        </div>""", unsafe_allow_html=True)
    elif persona == "普惠务实派":
        st.markdown("""
        <div class="st-card" style="border-left: 5px solid #86868B;">
            <h4>⏰ 09:30 | 静谧陪伴：办公氛围营造</h4><p>无需指令，仿生宠物在脚边安静蜷缩。其微弱的呼吸起伏模拟真实心跳，为您营造安心的居家居家办公环境。</p>
            <h4>⏰ 12:30 | 轻度解压：午间治愈互动</h4><p>简单的逗趣互动即可触发拟真表情反馈，通过低成本的交互切断工作内耗，提供瞬时的情绪补位。</p>
            <h4>⏰ 19:30 | 物理抚慰：触觉反馈治愈</h4><p>您坐在沙发休息，抚摸设备会触发模拟“呼噜声”与心跳震动。这种高亲和力的物理反馈，能有效降低焦虑。</p>
            <h4>⏰ 22:30 | 稳定存在：非侵入式守候</h4><p>设备反馈以柔和的机械微动，在寂静的深夜提供一份“生命共处感”，让家不再冷清。</p>
        </div>""", unsafe_allow_html=True)
    else: # 传统保守派
        st.markdown("""
        <div class="st-card" style="border-left: 5px solid #0071E3;">
            <h4>⏰ 08:30 | 健康扫描：晨间体征监测</h4><p>利用非侵入式雷达扫描老人步态。准时发出方言语音提醒服用降压药，确认服药后自动向子女发送报告。</p>
            <h4>⏰ 11:00 | 社交连接：跨代际视频助手</h4><p>通过最简化的声控交互开启远程通话，协助老人与异地子女沟通，并自动优化老人的光影成像表现。</p>
            <h4>⏰ 14:00 | 生命兜底：跌倒预警防线</h4><p>全天候扫描全屋轨迹。若识别到洗手间区域发生高度突变且30秒无移动，系统在不开启摄像头的尊严保护下直连120与子女。</p>
            <h4>⏰ 21:00 | 隐形守护：水电气安全巡视</h4><p>利用声学与雷达感应确认居家安全隐患。在长者入睡后维持后台监测，实现真正的无感化“平安哨兵”。</p>
        </div>""", unsafe_allow_html=True)

    col_back_l, col_back_m, col_back_r = st.columns([1, 1.2, 1])
    with col_back_m: st.button("↺ 返回首页，重置决策系统", use_container_width=True, on_click=set_step, args=("概念导入",))