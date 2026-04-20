import streamlit as st
import os

# ================= 1. 页面全局配置 =================
st.set_page_config(page_title="硅基陪伴 | 具身智能选型决策中枢", layout="wide", initial_sidebar_state="expanded")

# ================= 2. 苹果官网级精致 CSS 注入 =================
st.markdown("""
    <style>
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
    }

    /* 统一高能按钮：苹果深邃蓝 */
    div[data-testid="stButton"] button, div[data-testid="stFormSubmitButton"] button {
        background-color: #0071E3 !important;
        color: white !important;
        padding: 14px 40px !important;
        font-size: 18px !important;
        font-weight: 600 !important;
        border-radius: 30px !important;
        border: none !important;
        transition: all 0.3s ease !important;
        width: auto !important;
        min-width: 200px;
    }
    div[data-testid="stButton"] button:hover {
        background-color: #0077ED !important;
        transform: scale(1.02);
    }

    /* 产品卡片标签 */
    .product-label {
        margin-top: 12px;
        font-weight: 600;
        color: #1D1D1F;
        font-size: 15px;
        text-align: center;
    }

    /* PRD 样式 */
    .prd-item {
        display: flex;
        justify-content: space-between;
        padding: 16px 0;
        border-bottom: 1px solid #F5F5F7;
    }
    .prd-item b { color: #1D1D1F; font-weight: 600; }
    
    /* 模块小标题 */
    .section-header {
        color: #1D1D1F;
        font-size: 24px;
        font-weight: 700;
        margin: 40px 0 20px 0;
        border-left: 5px solid #0071E3;
        padding-left: 15px;
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
            st.image(file_name, use_container_width=True)
            st.markdown(f'<div class="product-label">{caption}</div>', unsafe_allow_html=True)
        else:
            st.info(f"🖼️ {caption} (待录入)")
    except Exception:
        pass

# ================= 3. 核心页面路由 =================

# --- 首页：14款产品全品类矩阵展示 ---
if st.session_state.step == "概念导入":
    st.markdown('<div class="hero-title">寻找最契合您的硅基伴侣</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">企业级具身智能数字化选型与匹配中枢</div>', unsafe_allow_html=True)
    
    # 居中大按钮
    col_btn_l, col_btn_m, col_btn_r = st.columns([1, 1.2, 1])
    with col_btn_m:
        st.button("立即开启数字化选型测评 ⚡", use_container_width=True, on_click=set_step, args=("智能测评",))

    st.markdown("""
        <div class="st-card" style="text-align: center;">
            <p style="color: #48484A; font-size: 17px; max-width: 850px; margin: 0 auto; line-height: 1.6;">
                基于科学的需求建模算法，从企业选型视角出发，为您精准匹配最适配的硬件形态与服务方案。
            </p>
        </div>
    """, unsafe_allow_html=True)

    # 视频区域
    col_v_l, col_v_m, col_v_r = st.columns([1, 4, 1])
    with col_v_m:
        st.markdown("""<iframe src="//player.bilibili.com/player.html?bvid=BV1mNdfBJEfT&page=1&autoplay=0" style="width:100%; height:480px; border-radius:32px; box-shadow: 0 30px 70px rgba(0,0,0,0.1);" frameborder="no" scrolling="no"></iframe>""", unsafe_allow_html=True)

    st.write("\n\n")
    st.markdown('<div class="section-header">🌐 全球具身智能“陪伴”旗舰矩阵</div>', unsafe_allow_html=True)
    
    # 第一排：核心四款（优先级最高）
    p1, p2, p3, p4 = st.columns(4)
    with p1: display_product_image("optimus.jpg", "Tesla Optimus")
    with p2: display_product_image("loona.jpg", "Loona 智能宠")
    with p3: display_product_image("ebox.jpg", "Enabot EBO X")
    with p4: display_product_image("ropet.jpg", "Ropet 仿生伴侣")

    # 第二排：高阶交互
    p5, p6, p7, p8 = st.columns(4)
    with p5: display_product_image("Ameca.jpg", "Ameca 社交机器人")
    with p6: display_product_image("Figure 02.jpg", "Figure 02 进化版")
    with p7: display_product_image("CyberOne.jpg", "小米 CyberOne")
    with p8: display_product_image("Astribot.jpg", "Astribot 精细操作")

    # 第三排：管家与仿生
    p9, p10, p11, p12 = st.columns(4)
    with p9: display_product_image("Aeolus Bot.jpg", "Aeolus 家庭管家")
    with p10: display_product_image("ASUS Zenbo.jpg", "华硕 Zenbo")
    with p11: display_product_image("Amazon Astro.jpg", "Amazon Astro")
    with p12: display_product_image("Elephant Robotics MarsCat.jpg", "MarsCat 仿生猫")

    # 第四排：教育陪伴（更新了圆宝机器人的名字）
    p13, p14, p15, p16 = st.columns(4)
    with p13: display_product_image("优必选悟空机器人.jpg", "优必选悟空")
    with p14: display_product_image("圆宝机器人.jpg", "圆宝机器人")

# --- 测评页 ---
elif st.session_state.step == "智能测评":
    st.markdown('<div class="hero-title" style="font-size: 42px;">🎯 数字化特征采集</div>', unsafe_allow_html=True)
    with st.form("survey"):
        st.markdown('<div class="form-section-title">01 / 生活切面与情感图谱</div>', unsafe_allow_html=True)
        col_q1, col_q2 = st.columns(2)
        with col_q1: q_living = st.radio("您的家庭居住形态？", ["独居 (一人居住)", "二人世界 (无子女)", "有孩家庭 (有18岁以下子女)", "多代同堂 (与老人同住)"])
        with col_q2: q_lonely = st.select_slider("您对日常陪伴的需求频率？", options=["极少", "偶尔", "经常", "非常频繁"])
        
        st.markdown('<div class="form-section-title">02 / 技术与隐私防备</div>', unsafe_allow_html=True)
        col_q3, col_q4 = st.columns(2)
        with col_q3: q_func = st.radio("购买机器人的核心驱动力？", ["情感慰藉", "儿童教育/安全", "老人健康监测", "纯粹娱乐/解压"])
        with col_q4: q_privacy = st.select_slider("数据隐私容忍度？", options=["完全接受云端", "仅接受端侧离线", "要求纯物理隔离"])
        
        st.markdown('<div class="form-section-title">03 / 消费决策</div>', unsafe_allow_html=True)
        col_q5, col_q6 = st.columns(2)
        with col_q5: q_price = st.selectbox("预算上限？", ["3000元及以下", "3001-8000元", "8001-15000元", "15000元以上"])
        with col_q6: q_pay = st.radio("倾向的付费模式？", ["硬件买断制", "HaaS 功能订阅制", "共享租赁模式"])

        st.write("\n")
        col_sub_l, col_sub_m, col_sub_r = st.columns([1, 1.2, 1])
        with col_sub_m:
            if st.form_submit_button("生成专属分析报告 🚀", use_container_width=True):
                if "儿童" in q_func or "有孩" in q_living: persona = "亲子伴学派"
                elif "老人" in q_func or "多代" in q_living: persona = "传统保守派"
                elif "15000" in q_price: persona = "高知尝鲜派"
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
    with k1: st.metric("精准画像", persona)
    with k2: st.metric("隐私协议", resp["privacy"])
    with k3: st.metric("推荐模式", resp["pay"])
    
    st.write("\n\n")
    col_rec_l, col_rec_r = st.columns([1, 1.4])
    with col_rec_l:
        if persona == "高知尝鲜派": display_product_image("Ameca.jpg", "推荐：Ameca 社交版")
        elif persona == "亲子伴学派": display_product_image("优必选悟空机器人.jpg", "推荐：优必选悟空")
        elif persona == "普惠务实派": display_product_image("loona.jpg", "推荐：Loona 智能宠")
        else: display_product_image("Amazon Astro.jpg", "推荐：Amazon Astro")
    
    with col_rec_r:
        st.markdown(f"""<div class="st-card"><h4 style="color:#1D1D1F; margin-top:0;">📋 专家级配置单 (PRD)</h4>
        <div class="prd-item"><b>核心卖点</b> <span>解决“{resp['func']}”的社交/功能痛点</span></div>
        <div class="prd-item"><b>部署建议</b> <span>采用“{resp['pay']}”实现闭环</span></div>
        <div class="prd-item"><b>安全协议</b> <span>执行“{resp['privacy']}”协议保护</span></div>
        <p style="font-size: 13px; color: #86868B; margin-top: 25px;">* 选型报告基于成都市具身智能市场研究模型动态生成。</p></div>""", unsafe_allow_html=True)
        col_scen_l, col_scen_m, col_scen_r = st.columns([1, 1.2, 1])
        with col_scen_m: st.button("启动 24H 沉浸式场景演练 🎬", use_container_width=True, on_click=set_step, args=("场景演练",))

# --- 场景演练页 ---
elif st.session_state.step == "场景演练":
    persona = st.session_state.user_responses.get("persona", "普惠务实派")
    st.markdown('<div class="hero-title" style="font-size: 40px; margin-top: 30px;">🎬 全时段沉浸式应用推演</div>', unsafe_allow_html=True)
    
    if persona == "高知尝鲜派":
        st.markdown("""
        <div class="st-card" style="border-left: 8px solid #0071E3;">
            <h4>⏰ 08:00 | 硅基唤醒：晨间深度简报</h4><p>机器人同步睡眠数据，通过温和语音播报当日全球要闻、股市动态及深度行程建议。</p>
            <h4>⏰ 13:00 | 商务代偿：异地视频会议</h4><p>利用精准微表情替代您进行远程商务对谈，并自动记录多维会议纪要。</p>
            <h4>⏰ 19:30 | 归家迎接：面部情绪感知</h4><p>识别到疲惫特征，主动发起“树洞对话”，提供心理疏导并联动调至解压模式。</p>
            <h4>⏰ 23:30 | 社交补位：深夜灵魂伴侣</h4><p>在寂静深夜提供高层次语义对谈，有效缓解城市孤独感，成为完美的情感容器。</p>
        </div>""", unsafe_allow_html=True)
    elif persona == "亲子伴学派":
        st.markdown("""
        <div class="st-card" style="border-left: 8px solid #0071E3;">
            <h4>⏰ 07:30 | 智慧晨起：今日学习路线</h4><p>自动提醒孩子洗漱，播报今日学习计划与目标，激发孩子自驱力。</p>
            <h4>⏰ 15:30 | 安全防线：全屋自动巡逻</h4><p>若识别孩子靠近厨房或阳台等高危区，即刻全屋警报并紧急连线家长。</p>
            <h4>⏰ 19:00 | 知识百科：沉浸式绘本伴读</h4><p>利用端侧算力精准识别各类教材，用多变声线陪孩子互动问答。</p>
            <h4>⏰ 21:00 | 助眠仪式：AI 互动故事会</h4><p>根据孩子今日表现现场创作童话，辅助孩子在安稳、温馨的氛围中入睡。</p>
        </div>""", unsafe_allow_html=True)
    elif persona == "普惠务实派":
        st.markdown("""
        <div class="st-card" style="border-left: 8px solid #86868B;">
            <h4>⏰ 10:00 | 静谧陪伴：办公氛围营造</h4><p>仿生宠物在脚边安静蜷缩，模拟真实心跳呼吸感，营造安心、专注的办公环境。</p>
            <h4>⏰ 14:00 | 趣动互动：午间解压时刻</h4><p>简单的逗弄触发拟真表情反馈，通过低成本交互切断繁琐的工作内耗。</p>
            <h4>⏰ 19:30 | 物理抚慰：触觉反馈治愈</h4><p>抚摸设备会触发模拟“呼噜声”，这种极高亲和力的物理反馈有效降低焦虑。</p>
            <h4>⏰ 22:30 | 稳定存在：非侵入式深夜守候</h4><p>设备反馈以柔和的机械微动，在寂静时刻提供一份“生命共处感”。</p>
        </div>""", unsafe_allow_html=True)
    else: # 传统保守派
        st.markdown("""
        <div class="st-card" style="border-left: 8px solid #0071E3;">
            <h4>⏰ 08:30 | 健康监测：晨间步态扫描</h4><p>非侵入式雷达扫描老人步态，准时语音提醒服药并向子女发送健康报告。</p>
            <h4>⏰ 11:30 | 社交连接：跨代际一键通话</h4><p>通过最简化的声控交互协助长者与异地子女沟通，自动优化视频表现。</p>
            <h4>⏰ 15:00 | 生命兜底：跌倒紧急预警</h4><p>若识别到高度突变且30秒未移动，系统在尊严保护下直连紧急中心与子女。</p>
            <h4>⏰ 21:00 | 隐形守护：全屋安全哨兵</h4><p>无感化确认水电气安全隐患，确保长者在绝对隐私下获得24小时安全保障。</p>
        </div>""", unsafe_allow_html=True)

    col_back_l, col_back_m, col_back_r = st.columns([1, 1.2, 1])
    with col_back_m: st.button("↺ 返回首页，重制决策系统", use_container_width=True, on_click=set_step, args=("概念导入",))