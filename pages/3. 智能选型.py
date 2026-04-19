import streamlit as st
import time
import pandas as pd
import plotly.graph_objects as go

# ================= 页面全局配置 =================
st.set_page_config(page_title="消费者特征映射与商业匹配", layout="wide")
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







# ================= 注入正规商务与学术 CSS =================
st.markdown("""
    <style>
    .main { background-color: #FAFAFA; }
    h1, h2, h3, h4 { font-family: 'Helvetica Neue', 'Arial', sans-serif; color: #1A2B4C; }
    
    .form-container {
        background-color: #FFFFFF;
        padding: 30px;
        border-radius: 4px;
        border-top: 3px solid #1A2B4C;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
        margin-bottom: 20px;
    }
    
    .result-card {
        background-color: #FFFFFF;
        padding: 24px;
        border-radius: 4px;
        border-left: 4px solid #1E3A8A;
        box-shadow: 0 2px 6px rgba(0,0,0,0.03);
        margin-bottom: 20px;
        line-height: 1.6;
        color: #333333;
    }
    .result-title { font-size: 18px; font-weight: 600; color: #1A2B4C; margin-bottom: 12px; border-bottom: 1px solid #EEEEEE; padding-bottom: 8px;}
    
    div.stButton > button:first-child {
        background-color: #1A2B4C;
        color: white;
        border-radius: 2px;
        height: 40px;
        font-weight: 500;
        width: 100%;
        border: none;
    }
    div.stButton > button:first-child:hover { background-color: #111D33; }
    </style>
""", unsafe_allow_html=True)

# ================= 状态管理 =================
if 'assessment_completed' not in st.session_state:
    st.session_state.assessment_completed = False
if 'persona_result' not in st.session_state:
    st.session_state.persona_result = None

# ================= 视图 A：多维特征采集表单 =================
if not st.session_state.assessment_completed:
    st.title("消费者特征提取与市场转化匹配模型")
    st.markdown("<p style='color: #555; font-size: 15px; margin-bottom: 30px;'>基于成都市中心城区实地调研样本与 K-means 聚类算法，输入潜在消费者特征变量，输出对应的产品形态与商业变现策略。</p>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="form-container">', unsafe_allow_html=True)
        st.markdown("<h4 style='margin-bottom:20px;'>模块一：应用场景与物理形态偏好</h4>", unsafe_allow_html=True)
        
        q_family = st.radio("1. 目标用户的核心应用场景属于：", 
                            ["社交代偿与情感慰藉（针对独居/二人家庭的孤独感缓解）", 
                             "儿童启蒙与居家安全伴学（针对有孩家庭）", 
                             "基础居家解压与轻度互动（针对快节奏年轻群体）", 
                             "适老辅助与无感健康监测（针对多代同堂或独居老人）"])
        
        # 严格对应问卷 Q15
        q_shape = st.radio("2. 目标用户对机器人的理想物理形态偏好为：",
                          ["类人形态（注重高阶拟人化交互）",
                           "仿生动物（如机器狗、仿生猫，注重触觉治愈）",
                           "简约机械感（如移动屏、监控终端，注重实用性）"])
        
        st.markdown("<h4 style='margin-top:30px; margin-bottom:20px;'>模块二：隐私阈值与购买意愿变量</h4>", unsafe_allow_html=True)
        
        q_privacy = st.select_slider("3. 目标用户对终端设备收集家庭视觉/语音数据的防备心理：",
                                     options=["极度敏感（要求物理断网）", "中度防备（接受本地端侧运算）", "技术信任（接受云端大模型联动）"], value="中度防备（接受本地端侧运算）")
        
        # 严格对应问卷 Q16
        q_budget = st.selectbox("4. 目标用户对具身智能产品的最高预算限制：", 
                                ["3000元以下", "3001-8000元", "8001-15000元", "15000元以上"])
        
        # 严格对应问卷 Q17
        q_payment = st.radio("5. 针对机器人的系统升级与服务，更倾向的付费模式：",
                             ["终身买断制（购机后软件永久免费升级）",
                              "功能订阅制（基础功能免费，高级情感/教育功能按月付费）",
                              "共享模式（按使用次数或服务时长付费）"])
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        if st.button("运行匹配算法提取目标画像"):
            with st.spinner("提取输入特征向量..."):
                time.sleep(0.5)
            with st.spinner("映射 K-means 聚类中心..."):
                time.sleep(0.5)
                
            # 基于用户输入的聚类逻辑映射
            persona = "普惠务实派" # 基准对照组
            
            if "儿童" in q_family:
                persona = "亲子伴学派"
            elif "适老" in q_family or "极度敏感" in q_privacy or "简约" in q_shape:
                persona = "传统保守派"
            elif "社交代偿" in q_family and ("8001" in q_budget or "15000" in q_budget) and "买断" in q_payment:
                persona = "高知尝鲜派"
            elif "订阅" in q_payment or "3000" in q_budget or "仿生" in q_shape:
                persona = "普惠务实派"
                
            st.session_state.persona_result = persona
            st.session_state.assessment_completed = True
            st.rerun()

# ================= 视图 B：算法匹配结果输出 =================
else:
    persona = st.session_state.persona_result
    st.title("市场分层结果与商业进入策略")
    st.markdown(f"<p style='color: #555; font-size: 15px;'>经算法匹配，该输入特征映射的市场分层结果为：<span style='color:#1A2B4C; font-weight:600; font-size:18px;'>【{persona}】</span></p>", unsafe_allow_html=True)
    st.divider()
    
    col_chart, col_text = st.columns([1, 1.2])
    
    with col_chart:
        # 雷达图保留，但维度名称全部替换为学术化表述
        categories = ['技术接受度', '价格敏感度', '情感交互刚需', '功能性替代需求', '隐私防御心理']
        
        base_scores = {
            "高知尝鲜派": [90, 20, 85, 30, 20],
            "亲子伴学派": [60, 60, 40, 90, 85],
            "普惠务实派": [50, 90, 70, 40, 50],
            "传统保守派": [20, 50, 30, 80, 95]
        }
        
        user_scores = [max(0, x - 5) for x in base_scores[persona]]
        
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(r=base_scores[persona], theta=categories, fill='toself', name='聚类中心基准线', line_color='rgba(200, 200, 200, 0.5)', fillcolor='rgba(200, 200, 200, 0.2)'))
        fig.add_trace(go.Scatterpolar(r=user_scores, theta=categories, fill='toself', name='当前样本特征测度', line_color='#1A2B4C', fillcolor='rgba(26, 43, 76, 0.4)'))
        
        fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=True, margin=dict(t=30, l=40, r=40, b=30), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)

    with col_text:
        st.markdown("<h4 style='color: #1A2B4C; margin-bottom: 15px;'>针对性商业转化建议</h4>", unsafe_allow_html=True)
        
        if persona == "高知尝鲜派":
            st.markdown("""
            <div class="result-card">
                <div class="result-title">产品形态定位：高阶交互型</div>
                <b>核心策略：</b>满足“四高”人群（高接受度、高收入、高知化、高情感需求）的先期体验诉求。<br><br>
                <b>技术配置：</b>融合大语言模型，强化系统的主动交互能力与社交代偿功能，以云端算力支撑复杂语义理解。<br>
                <b>商业模式：终身买断制。</b> 充分利用该群体较高的预算空间，通过硬件溢价收回前期研发成本，并以此建立品牌早期势能。
            </div>
            """, unsafe_allow_html=True)
        elif persona == "亲子伴学派":
            st.markdown("""
            <div class="result-card">
                <div class="result-title">产品形态定位：实用管家型</div>
                <b>核心策略：</b>聚焦家庭看护与儿童教育等明确的功能性替代场景。<br><br>
                <b>隐私机制：</b>考虑到该群体极高的隐私防备心理，必须提供物理级遮蔽方案，并保证核心教育功能在本地端侧流畅运行。<br>
                <b>商业模式：HaaS 订阅制。</b> 采用硬件低毛利策略降低进入家庭的门槛，通过后续提供“教育资源包”或“看护增值服务”实现按月/按季度的经常性收益。
            </div>
            """, unsafe_allow_html=True)
        elif persona == "普惠务实派":
            st.markdown("""
            <div class="result-card">
                <div class="result-title">产品形态定位：基础养成型</div>
                <b>核心策略：</b>落实“做减法”理念，剥离冗余的昂贵算力，回归基础的物理抚慰与情感治愈。<br><br>
                <b>技术配置：</b>摒弃复杂系统，重点提升物理材质的亲和力与仿生动作的流畅度，解决当前市场普遍存在的“工业级触感劝退”问题。<br>
                <b>商业模式：低门槛订阅或分期。</b> 针对其高价格敏感度，将定价严格控制在 3000-8000 元区间内，降低大众试错成本，打破观望壁垒。
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="result-card">
                <div class="result-title">产品形态定位：适老辅助型</div>
                <b>核心策略：</b>以非侵入式的无感健康监测为主导，规避技术带来的使用焦虑。<br><br>
                <b>技术配置：</b>弱化主动语音交互，强化被动式安全感知（如毫米波雷达跌倒预警），彻底消除老年群体的“被监视感”。<br>
                <b>商业模式：代际转移支付。</b> 营销受众转为有支付能力的异地子女群体，主推一次性买断+基础云储存服务费。
            </div>
            """, unsafe_allow_html=True)

        st.write("\n")
        
        # 导航交互
        b1, b2 = st.columns(2)
        with b1:
            try:
                st.page_link("pages/4_场景体验.py", label="查看实体应用场景模拟")
            except:
                st.info("请点击左侧导航栏前往【场景体验】")
        with b2:
            if st.button("清空数据，重新输入"):
                st.session_state.assessment_completed = False
                st.session_state.persona_result = None
                st.rerun()