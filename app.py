import streamlit as st
import os

# ================= 1. 页面全局配置 =================
st.set_page_config(page_title="硅基陪伴 | 具身智能选型决策小程序", layout="wide", initial_sidebar_state="expanded")

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

    /* === 终极按钮居中 CSS === */
    /* 针对普通按钮 */
    div.stButton {
        display: flex;
        justify-content: center;
    }
    /* 针对表单提交按钮 */
    div[data-testid="stFormSubmitButton"] {
        display: flex;
        justify-content: center;
    }

    /* 统一高能按钮样式：苹果深邃蓝 */
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

    /* 产品标签 */
    .product-label {
        margin-top: 12px;
        font-weight: 600;
        color: #1D1D1F;
        font-size: 15px;
        text-align: center;
    }

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
            st.info(f"{caption} (待上传)")
    except Exception:
        pass

# ================= 3. 核心页面路由 =================

# --- 首页 ---
# --- 首页 ---
if st.session_state.step == "概念导入":
    
    # 【优化1：顶部核心交互区收拢】比例 [1, 2.5, 1]
    col_hero_l, col_hero_m, col_hero_r = st.columns([1, 2.5, 1])
    
    with col_hero_m:
        st.markdown('<div class="hero-title">寻找最契合您的硅基伴侣</div>', unsafe_allow_html=True)
        st.markdown('<div class="hero-subtitle">企业级具身智能数字化选型与匹配小程序</div>', unsafe_allow_html=True)
        
        # 将愿景说明提上来，逻辑更顺：先看理念，再点按钮
        st.markdown("""
            <div class="st-card" style="text-align: center; padding: 25px; margin-bottom: 30px;">
                <p style="color: #48484A; font-size: 16px; margin: 0; line-height: 1.6;">
                    <b>平台愿景：</b>在选购具身智能终端前，通过科学的算法逻辑，对比您的隐私安全阈值、家庭结构及核心情感诉求，从企业视角为您精准匹配最合适的硬件形态。
                </p>
            </div>
        """, unsafe_allow_html=True)

        # 嵌套一层列，防止按钮在中间列里依然被拉得太长
        col_btn_inner_l, col_btn_inner_m, col_btn_inner_r = st.columns([1, 1.5, 1])
        with col_btn_inner_m:
            st.button("立即开启数字化选型测评 ", use_container_width=True, on_click=set_step, args=("智能测评",))

        st.write("\n\n")

        # 视频区域也放在中间列，保持边缘对齐，高度微调为 400px 保证比例协调
        st.markdown("""<iframe src="//player.bilibili.com/player.html?bvid=BV1mNdfBJEfT&page=1&autoplay=0" style="width:100%; height:400px; border-radius:24px; box-shadow: 0 20px 40px rgba(0,0,0,0.08);" frameborder="no" scrolling="no"></iframe>""", unsafe_allow_html=True)

    st.write("\n\n")

    # 【优化2：产品矩阵区收拢】比例 [1, 4, 1] 留出恰到好处的边距，图片不会过大或贴边
    col_matrix_l, col_matrix_m, col_matrix_r = st.columns([1, 4, 1])
    
    with col_matrix_m:
        st.markdown('<div class="section-header">🌐 全球具身智能陪伴机器人产品矩阵</div>', unsafe_allow_html=True)
        
        # 第一排：核心四款
        p1, p2, p3, p4 = st.columns(4)
        with p1: display_product_image("optimus.jpg", "Tesla Optimus")
        with p2: display_product_image("loona.jpg", "Loona 智能宠物机器人")
        with p3: display_product_image("ebox.jpg", "Enabot EBO X")
        with p4: display_product_image("ropet.jpg", "Ropet 仿生伴侣")

        # 第二排：交互与进阶
        p5, p6, p7, p8 = st.columns(4)
        with p5: display_product_image("Ameca.jpg", "Ameca 陪伴机器人")
        with p6: display_product_image("Figure 02.jpg", "Figure 02机器人")
        with p7: display_product_image("CyberOne.jpg", "小米 CyberOne")
        with p8: display_product_image("Astribot.jpg", "Astribot 精细操作")

        # 第三排：管家与仿生
        p9, p10, p11, p12 = st.columns(4)
        with p9: display_product_image("Aeolus Bot.jpg", "Aeolus 家庭管家")
        with p10: display_product_image("ASUS Zenbo.jpg", "华硕 Zenbo")
        with p11: display_product_image("Amazon Astro.jpg", "Amazon Astro")
        with p12: display_product_image("Elephant Robotics MarsCat.jpg", "MarsCat 仿生猫")

        # 第四排：教育陪伴
        p13, p14, p15, p16 = st.columns(4)
        with p13: display_product_image("优必选悟空机器人.jpg", "优必选悟空")
        with p14: display_product_image("圆宝机器人.jpg", "圆宝陪伴机器人")

# --- 测评页 ---
elif st.session_state.step == "智能测评":
    st.markdown('<div class="hero-title" style="font-size: 42px;"> 数字化特征采集</div>', unsafe_allow_html=True)
    
    # 【核心优化点】：使用 3 列布局，左右留白（比例为 1），中间放表单（比例为 2.5 或 3）
    col_space_left, col_main, col_space_right = st.columns([1, 2.5, 1]) 
    
    with col_main: # 将整个 form 放入居中的主列中
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
            # 【强制居中提交按钮】
            submitted = st.form_submit_button("生成专属分析报告", use_container_width=True)
            if submitted:
                if "儿童" in q_func or "有孩" in q_living: persona = "亲子伴学派"
                elif "老人" in q_func or "多代" in q_living: persona = "传统保守派"
                elif "15000" in q_price: persona = "高知尝鲜派"
                else: persona = "普惠务实派"
                st.session_state.user_responses = {"persona": persona, "privacy": q_privacy, "price": q_price, "func": q_func, "pay": q_pay}
                set_step("结论分析")
                st.rerun()

# --- 结论页 ---
elif st.session_state.step == "结论分析":
    resp = st.session_state.user_responses
    persona = resp.get("persona")
    st.markdown(f'<div class="hero-title" style="font-size: 38px; margin-top: 30px;">选型报告：{persona}</div>', unsafe_allow_html=True)
    
    # 【核心优化点】：使用 3 列布局，左右留白，将所有内容向中间聚拢
    col_space_left, col_main, col_space_right = st.columns([1, 2.8, 1]) 
    
    with col_main:
        # 仪表盘看板 (聚拢后会显得更紧凑专业)
        k1, k2, k3 = st.columns(3)
        with k1: st.metric("精准画像", persona)
        with k2: st.metric("隐私协议", resp["privacy"])
        with k3: st.metric("推荐模式", resp["pay"])
        
        st.write("\n\n")
        
        # 产品图与PRD卡片的内部左右布局
        col_rec_l, col_rec_r = st.columns([1, 1.4])
        with col_rec_l:
            if persona == "高知尝鲜派": display_product_image("optimus.jpg", "旗舰推荐：Optimus陪伴机器人")
            elif persona == "亲子伴学派": display_product_image("优必选悟空机器人.jpg", "推荐形态：优必选悟空陪伴机器人")
            elif persona == "普惠务实派": display_product_image("loona.jpg", "推荐形态：Loona 智能宠物机器人")
            else: display_product_image("Amazon Astro.jpg", "推荐：Amazon Astro陪伴机器人")
        
        with col_rec_r:
            st.markdown(f"""<div class="st-card" style="margin-bottom: 25px;"><h4 style="color:#1D1D1F; margin-top:0;">精准配置单 (PRD)</h4>
            <div style="border-bottom: 1px solid #F5F5F7; padding: 12px 0;"><b>核心卖点</b> <span style="float:right;">解决“{resp['func']}”社交痛点</span></div>
            <div style="border-bottom: 1px solid #F5F5F7; padding: 12px 0;"><b>部署建议</b> <span style="float:right;">采用“{resp['pay']}”模式实现转化</span></div>
            <div style="border-bottom: 1px solid #F5F5F7; padding: 12px 0;"><b>安全协议</b> <span style="float:right;">执行“{resp['privacy']}”协议保护</span></div>
            <p style="font-size: 13px; color: #86868B; margin-top: 25px;">* 基于成都市具身智能市场研究模型动态生成。</p></div>""", unsafe_allow_html=True)
            
            # 按钮放置在PRD卡片下方对齐
            st.button("模拟居家场景", use_container_width=True, on_click=set_step, args=("场景演练",))

# --- 场景演练页 ---
elif st.session_state.step == "场景演练":
    persona = st.session_state.user_responses.get("persona", "普惠务实派")
    st.markdown('<div class="hero-title" style="font-size: 40px; margin-top: 30px;">🎬 全时段沉浸式应用推演</div>', unsafe_allow_html=True)
    
    # 【核心优化点】：建立三列布局，比例设为 [1, 2.5, 1]，让中间的内容区更聚拢
    col_space_l, col_main, col_space_r = st.columns([1, 2.5, 1])
    
    with col_main:
        # 根据画像展示差异化的 24 小时生活卡片
        if persona == "高知尝鲜派":
            st.markdown("""<div class="st-card" style="border-left: 8px solid #0071E3;">
                <h4> 08:00 | 清晨唤醒</h4><p>机器人同步健康数据，通过温和语音播报当日全球科技简报及深度行程建议。</p>
                <h4> 13:00 | 商务代偿</h4><p>利用精准微表情替代您进行远程视频会议，并自动生成多维会议纪要。</p>
                <h4> 19:30 | 归家迎接</h4><p>识别到疲惫面部特征，主动发起“树洞对话”等活动，提供心理疏导。</p>
                <h4> 23:30 | 深夜补位</h4><p>在寂静深夜提供高层次语义对谈，有效缓解都市孤独感。</p>
                </div>""", unsafe_allow_html=True)
        elif persona == "亲子伴学派":
            st.markdown("""<div class="st-card" style="border-left: 8px solid #0071E3;">
                <h4> 07:30 | 智慧晨起</h4><p>播报今日学习计划与背诵任务，通过互动语音激发孩子学习自驱力。</p>
                <h4> 15:30 | 安全防线</h4><p>若识别孩子靠近阳台等高危区，即刻全屋警报并远程连线家长。</p>
                <h4> 19:00 | 知识百科</h4><p>端侧算力精准识别教材，用生动声线陪孩子进行百科互动问答。</p>
                <h4> 21:00 | 助眠仪式</h4><p>现场实时创作互动童话故事，辅助孩子在温馨氛围中快速入睡。</p>
                </div>""", unsafe_allow_html=True)
        elif persona == "普惠务实派":
            st.markdown("""<div class="st-card" style="border-left: 8px solid #86868B;">
                <h4> 10:00 | 静谧陪伴</h4><p>仿生宠物在脚边安静蜷缩，通过拟真呼吸律动营造安心的居家办公环境。</p>
                <h4> 14:00 | 趣动时刻</h4><p>简单的逗弄即可触发拟真反馈，通过低成本交互有效切断工作内耗。</p>
                <h4> 19:30 | 物理抚慰</h4><p>抚摸设备触发模拟“呼噜声”，这种模拟触觉治愈能有效降低焦虑。</p>
                <h4> 22:30 | 稳定存在</h4><p>设备反馈以柔和机械微动，在寂静深夜为您提供一份“共处感”。</p>
                </div>""", unsafe_allow_html=True)
        else: # 传统保守派
            st.markdown("""<div class="st-card" style="border-left: 8px solid #0071E3;">
                <h4> 08:30 | 健康监测</h4><p>雷达扫描步态，准时语音提醒服药并同步向子女发送健康日报。</p>
                <h4> 11:30 | 社交连接</h4><p>最简声控交互协助长者与子女视频通话，AI 自动优化画质表现。</p>
                <h4> 15:00 | 生命兜底</h4><p>若识别高度突变且长时间未动，在保护隐私的前提下直连救护中心。</p>
                <h4> 21:00 | 隐形守护</h4><p>无感确认水电气安全隐患，确保长者在绝对隐私环境下获得守护。</p>
                </div>""", unsafe_allow_html=True)

        # 【返回按钮】也放在中间列，确保视觉重心不偏移
        st.button("返回首页，重置决策系统", use_container_width=True, on_click=set_step, args=("概念导入",))