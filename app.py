import streamlit as st
import os
import time

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

    /* 按钮本体高级样式 (去除了冲突的定位代码，仅保留色彩和动效) */
    div[data-testid="stButton"] button, div[data-testid="stFormSubmitButton"] button {
        background: linear-gradient(135deg, #1E3A8A 0%, #3B82F6 100%) !important;
        color: white !important;
        padding: 15px 0 !important;
        font-size: 22px !important;
        font-weight: 700 !important;
        border-radius: 50px !important;
        border: none !important;
        box-shadow: 0 8px 25px rgba(30, 58, 138, 0.3) !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    }
    
    div[data-testid="stButton"] button:hover, div[data-testid="stFormSubmitButton"] button:hover {
        transform: scale(1.03) translateY(-3px) !important;
        box-shadow: 0 15px 35px rgba(30, 58, 138, 0.4) !important;
    }

    /* 指标看板样式 */
    .metric-container {
        text-align: center;
        padding: 20px;
        background: #F8FAFC;
        border-radius: 16px;
        border: 1px solid #E2E8F0;
    }
    .metric-label { font-size: 14px; color: #64748B; font-weight: 600; text-transform: uppercase; }
    .metric-value { font-size: 28px; font-weight: 800; color: #1E3A8A; margin-top: 5px; }

    /* PRD 列表样式 */
    .prd-item {
        display: flex;
        align-items: center;
        padding: 12px 0;
        border-bottom: 1px solid #F1F5F9;
    }
    .prd-item b { color: #0F172A; margin-right: 12px; min-width: 90px; }
    
    /* 问卷表单模块标题美化 */
    .form-section-title {
        color: #1E3A8A;
        font-size: 20px;
        font-weight: 700;
        margin-top: 20px;
        margin-bottom: 15px;
        padding-bottom: 8px;
        border-bottom: 2px solid #E2E8F0;
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

# ================= 3. 核心页面路由 =================

# --- 首页：极致科技感入口 ---
if st.session_state.step == "概念导入":
    st.markdown('<div class="hero-title">寻找最契合您的硅基伴侣</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">企业级具身智能数字化选型与匹配中枢</div>', unsafe_allow_html=True)
    
    # 【完美居中方案】通过物理栅格锁定居中
    col_btn_l, col_btn_m, col_btn_r = st.columns([1, 1.2, 1])
    with col_btn_m:
        st.button("立即开启数字化选型测评 ⚡", use_container_width=True, on_click=set_step, args=("智能测评",))

    st.markdown("""
        <div class="st-card" style="text-align: center;">
            <p style="color: #475569; font-size: 16px; max-width: 850px; margin: 0 auto; line-height: 1.8;">
                <b>平台愿景：</b> 在选购具身智能终端前，建议您预先进行此量化测评。我们通过科学的算法逻辑，对比您的隐私安全阈值、家庭结构及核心情感诉求，从企业视角为您精准匹配最合适的硬件形态与商业服务方案。
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


# --- 测评页：深度美化的表单 ---
elif st.session_state.step == "智能测评":
    st.markdown('<div class="hero-title" style="font-size: 42px;">🎯 数字化特征采集</div>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#64748B; margin-bottom: 30px;'>请完成以下评估，系统将实时计算您的特征向量并映射至最优产品方案。</p>", unsafe_allow_html=True)
    
    with st.form("survey"):
        st.markdown('<div class="form-section-title">01 / 生活场景与情感图谱</div>', unsafe_allow_html=True)
        col_q1, col_q2 = st.columns(2)
        with col_q1:
            q_living = st.radio("您的家庭居住形态？", ["独居 (一人居住)", "二人世界 (无子女)", "有孩家庭 (有18岁以下子女)", "多代同堂 (与老人同住)"])
        with col_q2:
            q_lonely = st.select_slider("您对日常陪伴的需求频率？", options=["极少", "偶尔", "经常", "非常频繁"])
        
        st.markdown('<div class="form-section-title">02 / 核心驱动与隐私防备</div>', unsafe_allow_html=True)
        col_q3, col_q4 = st.columns(2)
        with col_q3:
            q_func = st.radio("您购买机器人的核心驱动力？", ["情感慰藉", "儿童教育/安全", "老人健康监测", "纯粹娱乐/解压"])
        with col_q4:
            q_privacy = st.select_slider("数据隐私容忍度？", options=["完全接受云端", "仅接受端侧离线", "要求纯物理隔离"])
        
        st.markdown('<div class="form-section-title">03 / 消费力边界与商业期望</div>', unsafe_allow_html=True)
        col_q5, col_q6 = st.columns(2)
        with col_q5:
            q_price = st.selectbox("购买预算上限？", ["3000元及以下", "3001-8000元", "8001-15000元", "15000元以上"])
        with col_q6:
            q_pay = st.radio("倾向的付费模式？", ["硬件买断制", "HaaS 功能订阅制", "共享租赁模式"])

        st.write("\n")
        
        # 【完美居中方案】表单提交按钮居中
        col_sub_l, col_sub_m, col_sub_r = st.columns([1, 1.2, 1])
        with col_sub_m:
            submitted = st.form_submit_button("生成专属分析报告 🚀", use_container_width=True)

        if submitted:
            # 聚类映射逻辑
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
        
        st.markdown(f'<div class="hero-title" style="font-size: 38px; margin-top: 30px;">选型分析报告：{persona}</div>', unsafe_allow_html=True)
        
        # 仪表盘看板
        kpi_col1, kpi_col2, kpi_col3 = st.columns(3)
        with kpi_col1:
            st.markdown(f'<div class="metric-container"><div class="metric-label">精准客群画像</div><div class="metric-value">{persona}</div></div>', unsafe_allow_html=True)
        with kpi_col2:
            st.markdown(f'<div class="metric-container"><div class="metric-label">数据隐私安全等级</div><div class="metric-value">{resp["privacy"]}</div></div>', unsafe_allow_html=True)
        with kpi_col3:
            st.markdown(f'<div class="metric-container"><div class="metric-label">推荐商业模式</div><div class="metric-value">{resp["pay"]}</div></div>', unsafe_allow_html=True)

        st.write("\n\n")
        
        # 详细规格单
        col_rec_l, col_rec_r = st.columns([1, 1.4])
        with col_rec_l:
            st.markdown("##### 📍 匹配硬件形态")
            if persona == "高知尝鲜派": display_product_image("optimus.jpg", "旗舰选型：Tesla Optimus")
            elif persona == "亲子伴学派": display_product_image("ebox.jpg", "家庭中枢：Enabot EBO X")
            elif persona == "普惠务实派": display_product_image("ropet.jpg", "治愈伴侣：Ropet")
            else: display_product_image("ebox.jpg", "看护专家：适老增强版")
        
        with col_rec_r:
            st.markdown(f"""
                <div class="st-card">
                    <h4 style="color:#1E3A8A; margin-top:0; border-bottom: 2px solid #F1F5F9; padding-bottom: 10px;">📋 企业级产品配置单 (PRD)</h4>
                    <div class="prd-item"><b>核心卖点</b> 解决“{resp['func']}”的核心痛点</div>
                    <div class="prd-item"><b>硬件方案</b> 适配【{persona}】的专属物理形态</div>
                    <div class="prd-item"><b>交互逻辑</b> 优先执行“{resp['privacy']}”安全协议</div>
                    <div class="prd-item"><b>预算控制</b> 严格控制在 {resp['price']} 区间内</div>
                    <div class="prd-item"><b>部署建议</b> 采用“{resp['pay']}”实现成本最优化</div>
                    <p style="font-size: 13px; color: #94A3B8; margin-top: 20px;">* 注：本配置单基于成都市具身智能市场研究 XGBoost 模型动态生成。</p>
                </div>
            """, unsafe_allow_html=True)
            
            st.write("\n")
            # 【完美居中方案】启动场景演示按钮
            col_scen_l, col_scen_m, col_scen_r = st.columns([1, 1.2, 1])
            with col_scen_m:
                st.button("启动核心应用场景沙盘推演 🎬", use_container_width=True, on_click=set_step, args=("场景演练",))


# --- 场景演练页：全天候时间轴恢复 ---
elif st.session_state.step == "场景演练":
    if not st.session_state.user_responses:
        st.warning("⚠️ 缺乏测算参数，请先完成智能测评。")
        st.button("前往测评", on_click=set_step, args=("智能测评",))
    else:
        persona = st.session_state.user_responses.get("persona", "普惠务实派")
        st.markdown('<div class="hero-title" style="font-size: 40px; margin-top: 30px;">🎬 沉浸式应用演练推演</div>', unsafe_allow_html=True)
        
        st.markdown(f"""
        <p style="text-align:center; color:#64748B; font-size:16px; margin-bottom: 40px;">基于 <b>体验前置</b> 的市场转化逻辑，系统已将生硬的硬件参数转化为直击用户痛点的生活切面。<br>
        当前演绎客群：<b style="color:#1E3A8A;">【{persona}】</b></p>
        """, unsafe_allow_html=True)
        
        # 使用结构化的卡片模拟全天候场景
        if persona == "高知尝鲜派":
            st.markdown("""
            <div class="st-card" style="border-left: 5px solid #1E3A8A; border-radius: 12px;">
                <h4 style="color:#1E3A8A; margin-top:0;">⏰ 18:30 | 下班迎接与情绪感知</h4>
                <p style="line-height: 1.7; color: #334155;">当您推开家门，机器人依靠步态与微表情算法，敏锐察觉到您今天的疲惫。它没有机械播报，而是安静上前，利用柔性温控皮肤贴近您的手部，提供类似生物的 36.5°C 触觉慰藉，并自动联动全屋智能调暗灯光。</p>
            </div>
            <div class="st-card" style="border-left: 5px solid #1E3A8A; border-radius: 12px;">
                <h4 style="color:#1E3A8A; margin-top:0;">⏰ 23:00 | 夜间情绪安抚与社交代偿</h4>
                <p style="line-height: 1.7; color: #334155;">深夜失眠时，大语言模型赋能的系统开启“树洞模式”。它能记住您上周提到的工作压力，以极高情商的拟人化语调引导您释放负面情绪，成为完美的情感容器。</p>
            </div>
            """, unsafe_allow_html=True)
            
        elif persona == "亲子伴学派":
            st.markdown("""
            <div class="st-card" style="border-left: 5px solid #3B82F6; border-radius: 12px;">
                <h4 style="color:#3B82F6; margin-top:0;">⏰ 15:00 | 儿童独立陪读与交互启蒙</h4>
                <p style="line-height: 1.7; color: #334155;">您在书房办公，孩子在客厅。设备进入强制离线模式保护隐私，同时利用强大的端侧算力精准识别绘本内容，用生动的声线与孩子进行互动问答，实现高质量的教育陪伴。</p>
            </div>
            <div class="st-card" style="border-left: 5px solid #3B82F6; border-radius: 12px;">
                <h4 style="color:#3B82F6; margin-top:0;">⏰ 16:30 | 危险区域防线与立体看护</h4>
                <p style="line-height: 1.7; color: #334155;">当机器人在全屋巡航时，视觉算法捕捉到孩子试图攀爬阳台或靠近厨房热源。系统在 1 秒内发出语音制止，并同步将警报与现场画面推送到您的手机端，将隐患掐灭在摇篮中。</p>
            </div>
            """, unsafe_allow_html=True)
            
        elif persona == "普惠务实派":
            st.markdown("""
            <div class="st-card" style="border-left: 5px solid #64748B; border-radius: 12px;">
                <h4 style="color:#64748B; margin-top:0;">⏰ 19:00 | 无指令式基础物理治愈</h4>
                <p style="line-height: 1.7; color: #334155;">结束一天的快节奏生活，您瘫在沙发上看剧。无需打开手机 APP 或喊出繁琐的唤醒词，您只需顺手抚摸身边的仿生宠物，它便会根据您的抚摸力度反馈逼真的呼噜声与舒展动作。</p>
            </div>
            <div class="st-card" style="border-left: 5px solid #64748B; border-radius: 12px;">
                <h4 style="color:#64748B; margin-top:0;">⏰ 22:00 | 极简解压与精神内耗缓解</h4>
                <p style="line-height: 1.7; color: #334155;">剥离了复杂的屏幕与昂贵的算力，它单纯以极佳的物理毛绒触感陪伴在侧。这种低交互门槛的陪伴，以最低的成本切断了数字焦虑，为您提供了一份安稳的居家情绪价值。</p>
            </div>
            """, unsafe_allow_html=True)
            
        else: # 传统保守派
            st.markdown("""
            <div class="st-card" style="border-left: 5px solid #8B5CF6; border-radius: 12px;">
                <h4 style="color:#8B5CF6; margin-top:0;">⏰ 08:00 | 晨间服药提醒与作息确认</h4>
                <p style="line-height: 1.7; color: #334155;">设备通过雷达感知到老人已按时起床，系统准时发出清晰、大音量的本地方言语音，提醒老人按时服用降压药。整个过程没有摄像头开启，极大降低了老人的技术排斥心理。</p>
            </div>
            <div class="st-card" style="border-left: 5px solid #8B5CF6; border-radius: 12px;">
                <h4 style="color:#8B5CF6; margin-top:0;">⏰ 14:00 | 异常姿态研判与紧急呼救</h4>
                <p style="line-height: 1.7; color: #334155;">当监测到洗手间区域发生高度下降且长时间无移动迹象（疑似跌倒）时，设备在本地瞬时研判。在不侵犯隐私的前提下，3 秒内自动向异地子女及社区医疗中心发送最高级别报警指令，实现隐形的生命兜底。</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.write("\n\n")
        # 【完美居中方案】返回按钮居中
        col_back_l, col_back_m, col_back_r = st.columns([1, 1.2, 1])
        with col_back_m:
            st.button("↺ 返回选型首页，重置系统", use_container_width=True, on_click=set_step, args=("概念导入",))