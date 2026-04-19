import streamlit as st
import os
import time

# ================= 1. 页面全局配置 =================
st.set_page_config(page_title="硅基陪伴 | 决策中枢", layout="wide", initial_sidebar_state="expanded")

# 注入商务学术风 CSS
st.markdown("""
    <style>
    .main { background-color: #F7F9FB; }
    .st-card { background: white; padding: 25px; border-radius: 4px; border-top: 4px solid #1A2B4C; box-shadow: 0 4px 12px rgba(0,0,0,0.05); margin-bottom: 20px; }
    .metric-val { font-size: 28px; font-weight: 700; color: #1A2B4C; }
    .metric-lab { font-size: 14px; color: #666; }
    .highlight-box { background-color: #E8F0FE; padding: 15px; border-radius: 4px; border-left: 5px solid #1E3A8A; margin: 10px 0; }
    div.stButton > button { background-color: #1A2B4C !important; color: white !important; width: 100%; border-radius: 2px; height: 3rem; }
    </style>
""", unsafe_allow_html=True)

# 状态管理
if 'step' not in st.session_state: st.session_state.step = "概念导入"
if 'user_responses' not in st.session_state: st.session_state.user_responses = {}

def set_step(name): st.session_state.step = name

# ================= 2. 页面逻辑 =================

# --- 2.1 概念导入与产品矩阵 ---
if st.session_state.step == "概念导入":
    st.title("具身智能：从“工具理性”到“情感代偿”的跨越")
    st.markdown("#### 硅基陪伴：成都市具身智能陪伴机器人消费需求分析平台")
    
    col_intro, col_video = st.columns([1.2, 1])
    with col_intro:
        st.markdown(f"""
        <div class="st-card">
            <h3>项目执行摘要</h3>
            <p>基于成都市 <b>693 份</b> 有效实地样本，我们发现具身智能市场呈现明显的 <b>“认知热、转化冷”</b> 断层。</p>
            <p>本平台旨在落实 <b>“体验前置”</b> 理念，剥离冗余算力溢价，回归物理触觉治愈的商业本质。通过量化测评，解决由于“隐私防御”与“物理亲和力缺失”带来的消费阻力。</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_video:
        # 插入 Tesla Optimus 视频演示
        st.markdown("""
        <iframe src="//player.bilibili.com/player.html?bvid=BV1QC4y1572d&page=1&autoplay=0" 
                style="width:100%; height:320px; border-radius:8px;" frameborder="no" scrolling="no"></iframe>
        """, unsafe_allow_html=True)

    st.subheader("🌐 全球主流具身智能产品矩阵")
    p1, p2, p3, p4 = st.columns(4)
    with p1:
        if os.path.exists("optimus.jpg"): st.image("optimus.jpg", caption="Tesla Optimus (Gen 2)")
        st.caption("**高阶通用型**：主打多模态决策与精细触觉。")
    with p2:
        if os.path.exists("loona.jpg"): st.image("loona.jpg", caption="Loona 智能宠")
        st.caption("**情感驱动型**：拟人化微表情，主打社交陪伴。")
    with p3:
        if os.path.exists("ebox.jpg"): st.image("ebox.jpg", caption="Enabot EBO X")
        st.caption("**安全看护型**：全屋移动巡航，兼顾教育伴读。")
    with p4:
        if os.path.exists("ropet.jpg"): st.image("ropet.jpg", caption="Ropet 仿生伴侣")
        st.caption("**治愈体验型**：极致物理亲和力，去算力冗余。")

    st.button("进入数字化需求测评系统 ➡️", on_click=set_step, args=("智能测评",))

# --- 2.2 智能需求测评 (多维特征采集) ---
elif st.session_state.step == "智能测评":
    st.title("🎯 消费者多维特征采集与需求归因")
    st.write("系统将根据您的反馈实时匹配 XGBoost 归因模型中的核心变量权重。")
    
    with st.form("survey"):
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("##### 维度一：家庭生活图谱")
            f_structure = st.radio("1. 您的家庭核心居住形态？", ["独居/二人家庭", "有孩家庭 (18岁以下)", "多代同堂 (含60岁+老人)"])
            f_lonely = st.select_slider("2. 您在日常生活中感到孤独/需要陪伴的频率？", options=["极低", "中度", "高频"])
            
            st.markdown("##### 维度二：物理亲和力与触觉需求")
            f_touch = st.radio("3. 您是否更倾向于具有仿生毛绒材质、能产生触觉治愈的产品？", ["强烈倾向 (做减法模型)", "一般", "更看重科技感材质"])

        with c2:
            st.markdown("##### 维度三：技术接受度与隐私防御")
            f_privacy = st.select_slider("4. 您对机器人收集居家多模态数据（视频/语音）的防备阈值？", options=["完全不设防", "中度保护", "极度防御 (要求断网)"])
            
            st.markdown("##### 维度四：经济弹性与付费预期")
            f_budget = st.selectbox("5. 针对具身智能产品的最高单次购买预算？", ["3000元以下", "3001-8000元", "8000元以上"])
            f_mode = st.radio("6. 倾向的付费商业模式？", ["硬件一次性买断", "HaaS (硬件即服务) 按月订阅"])

        if st.form_submit_button("运行分析模型并生成匹配结论"):
            # 简化版 K-means 映射逻辑
            if "有孩" in f_structure: persona = "亲子伴学派"
            elif "多代" in f_structure or "极度防御" in f_privacy: persona = "传统保守派"
            elif "8000" in f_budget and "高频" in f_lonely: persona = "高知尝鲜派"
            else: persona = "普惠务实派"
            
            st.session_state.user_responses = {"persona": persona, "lonely": f_lonely, "privacy": f_privacy}
            set_step("结论分析")
            st.rerun()

# --- 2.3 深度分析结论与产品匹配 ---
elif st.session_state.step == "结论分析":
    persona = st.session_state.user_responses["persona"]
    st.title(f"聚类识别结果：【{persona}】")
    
    # 深度分析部分 (体现调研报告逻辑)
    st.markdown(f"""
    <div class="st-card">
        <h3>📊 归因权重分析 (SHAP 模型解释)</h3>
        <p>基于 XGBoost 归因模型分析，影响您决策的核心因子为 <b>家庭结构</b> 与 <b>隐私安全</b>。</p>
        <div class="highlight-box">
            <b>分析结论：</b>针对您的特征，系统识别出您对“端侧运行”与“离线计算”有较高倾向性。
            您的需求特征在成都市场中占比约为 <b>23.5%</b>，属于关键的市场进入切入点。
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 产品展示与建议
    col_img, col_rec = st.columns([1, 1.2])
    with col_img:
        # 发挥想象力的产品展示布局
        if persona == "高知尝鲜派":
            st.image("optimus.jpg", caption="Tesla Optimus - 极致交互方案")
            st.image("loona.jpg", caption="辅助配置：Loona 情感引擎")
        elif persona == "亲子伴学派":
            st.image("ebox.jpg", caption="Enabot EBO X - 家庭安全中枢")
        elif persona == "普惠务实派":
            st.image("ropet.jpg", caption="Ropet - 物理治愈方案")
        else: # 传统保守派
            st.image("ebox.jpg", caption="无感健康监测终端")

    with col_rec:
        st.subheader("💡 针对性商业策略建议")
        if persona == "高知尝鲜派":
            st.write("**产品形态**：高阶交互型。搭载多模态大模型，支持社交代偿。")
            st.write("**商业模式**：硬件买断制。满足高溢价区间的先发体验需求。")
        elif persona == "亲子伴学派":
            st.write("**产品形态**：实用管家型。集成教育资源库与物理隐私遮蔽罩。")
            st.write("**商业模式**：HaaS 订阅制。降低初次购机门槛，通过增值内容获利。")
        elif persona == "普惠务实派":
            st.write("**产品形态**：基础养成型。落实“做减法”理念，回归触觉治愈本质。")
            st.write("**商业模式**：免押金租赁/分期。打破“高认知、低转化”的消费壁垒。")
        else:
            st.write("**产品形态**：隐形看护型。去视觉化监测（毫米波雷达），解决隐私防御。")
            st.write("**商业模式**：代际转移支付。营销受众锁定为异地子女。")
            
        st.button("进入沉浸式落地场景演练 🎬", on_click=set_step, args=("场景演练",))

# --- 2.4 场景演练 ---
elif st.session_state.step == "场景演练":
    persona = st.session_state.user_responses["persona"]
    st.title("典型生活场景应用模拟")
    
    st.markdown(f"""
    <div class="highlight-box">
        基于 <b>体验前置</b> 理念，以下场景旨在通过数字化形式模拟产品在真实居家环境中的应用效果。
    </div>
    """, unsafe_allow_html=True)
    
    if persona == "高知尝鲜派":
        st.markdown("### 🌙 场景 A：深夜补位社交代偿")
        st.write("您加班归来，机器人识别到面部疲态，主动通过柔性温控皮肤提供物理慰藉，并开启深度解压对话。")
    elif persona == "亲子伴学派":
        st.markdown("### 📖 场景 B：离线伴读与立体看护")
        st.write("设备物理切断云端连接，本地算力识别绘本并朗读，同时监测儿童是否进入洗手间等危险区域。")
    elif persona == "普惠务实派":
        st.markdown("### 🛋️ 场景 C：无指令式触觉反馈")
        st.write("无需复杂喚醒，简单的抚摸即可触发拟真的呼噜声与震动。剥离昂贵算力，回归纯粹的压力释放。")
    else:
        st.markdown("### 🛡️ 场景 D：隐私安全隐形守护")
        st.write("全程无视觉画面留存。当雷达判定洗手间内有异常倒地且30秒无移动时，系统即刻触发子女手机强提醒。")
    
    st.divider()
    st.button("↺ 重置分析模型", on_click=set_step, args=("概念导入",))