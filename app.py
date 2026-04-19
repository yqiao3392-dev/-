import streamlit as st
import os

# ================= 1. 页面全局配置 =================
st.set_page_config(page_title="硅基陪伴 | 具身智能选型决策中枢", layout="wide")

# ================= 2. 注入学术级 CSS (集成在单文件内，防止加载失败) =================
st.markdown("""
    <style>
    .main { background-color: #FAFAFA; }
    h1, h2, h3 { color: #1A2B4C; font-family: 'Helvetica Neue', Arial, sans-serif; }
    /* 商业卡片样式 */
    .biz-card {
        background-color: #FFFFFF;
        padding: 24px;
        border-radius: 4px;
        border-top: 3px solid #1A2B4C;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        margin-bottom: 24px;
    }
    .scenario-box {
        background-color: #F8F9FB;
        padding: 20px;
        border-left: 4px solid #1A2B4C;
        color: #333333;
        line-height: 1.7;
    }
    /* 按钮美化 */
    div.stButton > button {
        background-color: #1A2B4C !important;
        color: white !important;
        border-radius: 2px !important;
        height: 3rem;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# ================= 3. 核心逻辑与状态管理 =================
if 'step' not in st.session_state:
    st.session_state.step = "首页"
if 'persona' not in st.session_state:
    st.session_state.persona = None

def set_step(step_name):
    st.session_state.step = step_name

# 智能图片加载函数：优先从根目录读取，确保无占位符
def display_product_image(file_name, caption):
    # 尝试直接读取根目录
    if os.path.exists(file_name):
        st.image(file_name, caption=caption, use_container_width=True)
    else:
        # 如果根目录没有，尝试 assets/products/ 路径（兼容旧操作）
        path = f"assets/products/{file_name}"
        if os.path.exists(path):
            st.image(path, caption=caption, use_container_width=True)
        else:
            st.warning(f"检测到图片 {file_name} 尚未上传至根目录，请检查 GitHub 仓库。")

# ================= 4. 路由页面渲染 =================

# --- 4.1 简明首页 ---
if st.session_state.step == "首页":
    st.title("具身智能陪伴机器人选型决策平台")
    st.markdown("#### 基于成都市739份调研样本与K-means聚类模型")
    st.divider()
    
    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.markdown("""
        <div class="biz-card">
        <h3>项目摘要</h3>
        <p>本项目针对当前市场“认知转化率低”的现实困境，通过 <b>XGBoost 算法</b> 锁定了隐私安全与物理亲和力两大核心影响因子。</p>
        <p>本平台旨在落实“体验前置”理念，通过量化测评为消费者精准匹配产品形态与商业订阅模式，实现研究成果的数字化落地。</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("开始精准需求测评 ➡️", on_click=set_step, args=("测评",))
    with col2:
        # 首页展示图：建议放 optimus 或全家福
        display_product_image("optimus.jpg", "Tesla Optimus：具身智能行业标杆")

# --- 4.2 核心测评 (严格对应附录问卷) ---
elif st.session_state.step == "测评":
    st.title("消费者多维特征采集")
    st.write("请根据真实需求进行选择，系统将实时计算聚类偏差。")
    
    with st.form("survey"):
        q1 = st.radio("1. 您的家庭核心居住结构是？", ["独居形态", "二人家庭", "有孩家庭", "多代同堂"])
        q2 = st.radio("2. 您对前沿科技产品（如AI大模型）的态度是？", ["极度狂热（尝鲜派）", "务实观望", "防御保守"])
        q3 = st.radio("3. 您理想中的机器人物理形态是？", ["类人形态", "仿生动物", "简约机械感"])
        q4 = st.selectbox("4. 您的最高购买预算范围是？", ["3000元以下", "3001-8000元", "8000元以上"])
        q5 = st.radio("5. 您更倾向于哪种付费模式？", ["一次性买断制", "HaaS 硬件订阅制"])
        
        submitted = st.form_submit_button("提交并生成匹配方案")
        if submitted:
            # 简化版 K-means 逻辑模拟
            if "有孩" in q1: persona = "亲子伴学派"
            elif "多代" in q1 or "防御" in q2: persona = "传统保守派"
            elif "独居" in q1 and "8000" in q4: persona = "高知尝鲜派"
            else: persona = "普惠务实派"
            
            st.session_state.persona = persona
            set_step("结果")
            st.rerun()

# --- 4.3 画像匹配与产品介绍 (核心加分项) ---
elif st.session_state.step == "结果":
    persona = st.session_state.persona
    st.title(f"聚类识别结果：{persona}")
    st.divider()
    
    # 核心：根据画像配对产品，介绍产品
    if persona == "高知尝鲜派":
        col1, col2 = st.columns(2)
        with col1:
            display_product_image("optimus.jpg", "产品形态 A：Tesla Optimus")
            st.write("**定位**：高阶交互型。搭载多模态大模型，主打拟人化情感代偿。")
        with col2:
            display_product_image("loona.jpg", "产品形态 B：Loona 智能宠")
            st.write("**定位**：灵敏交互型。具备仿生微表情与语义记忆能力。")
        st.info("💡 **商业模式建议**：高溢价买断制。满足高净值客群的品牌排他性与先发体验需求。")

    elif persona == "亲子伴学派":
        col1, col2 = st.columns([1, 1.2])
        with col1:
            display_product_image("ebox.jpg", "推荐产品：Enabot EBO X")
        with col2:
            st.write("### 方案：实用管家型")
            st.write("**核心优势**：一机守护全屋。集成绘本伴读、安全巡航与跌倒预警。")
            st.write("**隐私策略**：配备物理遮蔽罩，核心功能支持端侧离线运行，彻底消弭家长隐私焦虑。")
            st.success("💰 **商业模式建议**：HaaS 硬件订阅制。降低购机门槛，通过早教资源包持续盈利。")

    elif persona == "普惠务实派":
        col1, col2 = st.columns([1, 1.2])
        with col1:
            display_product_image("ropet.jpg", "推荐产品：Ropet 仿生伴侣")
        with col2:
            st.write("### 方案：基础养成型")
            st.write("**设计理念**：落实“做减法”理念。剥离冗余算力，回归纯粹的物理触觉治愈。")
            st.write("**市场逻辑**：3000元以下普惠定价。通过仿生毛绒材质优化亲和力，解决“工业冷冰冰”带来的认知劝退。")
            st.warning("💳 **商业模式建议**：免押金租赁/分期模式。最大化降低试错成本。")

    else: # 传统保守派
        col1, col2 = st.columns([1, 1.2])
        with col1:
            display_product_image("ebox.jpg", "适老版 EBO X (无感监测版)")
        with col2:
            st.write("### 方案：隐形看护型")
            st.write("**核心逻辑**：去视觉化监测。采用毫米波雷达技术，在不侵犯隐私的前提下实现健康监测。")
            st.write("**代际转化**：营销受众锁定为异地子女，解决“想管管不上、想看不能看”的家庭痛点。")

    st.write("\n")
    st.button("查看此产品的典型落地场景体验 🎬", on_click=set_step, args=("场景",))

# --- 4.4 典型场景展示 ---
elif st.session_state.step == "场景":
    persona = st.session_state.persona
    st.title("典型场景沉浸式演练")
    st.divider()
    
    if persona == "高知尝鲜派":
        st.markdown("""<div class="scenario-box"><b>深夜情感补位场景</b>：当用户加班归家，机器人识别其面部疲态，主动提供柔性温控触碰，并开启舒缓的情绪交互逻辑，承接都市个体的孤独感。</div>""", unsafe_allow_html=True)
    elif persona == "亲子伴学派":
        st.markdown("""<div class="scenario-box"><b>居家安全防线场景</b>：设备进入离线模式。一边陪同孩子伴读绘本，一边利用传感器阵列实时监测洗手间等高危区域，确保家长的“精神解脱”。</div>""", unsafe_allow_html=True)
    elif persona == "普惠务实派":
        st.markdown("""<div class="scenario-box"><b>日常轻度解压场景</b>：无需复杂指令，用户在沙发小憩时顺手抚摸机器人，设备反馈以仿生呼噜声与震动。通过物理本质的治愈，降低精神内耗。</div>""", unsafe_allow_html=True)
    else:
        st.markdown("""<div class="scenario-box"><b>无感式健康兜底场景</b>：全程无摄像头。当雷达监测到洗手间区域老人体位异常且长时间未动时，系统自动在3秒内直连子女手机报警。</div>""", unsafe_allow_html=True)
    
    st.write("\n")
    st.button("🔄 重新评测", on_click=set_step, args=("首页",))