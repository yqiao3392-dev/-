import streamlit as st
import time

# ================= 1. 全局配置与高级样式 =================
st.set_page_config(page_title="硅基陪伴 | 消费决策与场景体验平台", layout="wide", initial_sidebar_state="expanded")

# 注入全局 CSS，去除默认冗余元素，提升商业质感
st.markdown("""
    <style>
    /* 全局背景与字体 */
    .main {background-color: #F8F9FA;}
    h1, h2, h3 {color: #2C3E50; font-family: 'Helvetica Neue', Arial, sans-serif;}
    
    /* 卡片化设计 */
    .st-card {
        background-color: #FFFFFF;
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 24px;
        border-top: 4px solid #0056b3;
    }
    
    /* 按钮美化 */
    div.stButton > button:first-child {
        background-color: #0056b3;
        color: white;
        border-radius: 8px;
        height: 3rem;
        font-weight: 600;
        border: none;
        width: 100%;
        transition: all 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        background-color: #004494;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)


# ================= 2. 状态管理与路由 =================
if 'current_page' not in st.session_state:
    st.session_state.current_page = "平台首页"
if 'persona' not in st.session_state:
    st.session_state.persona = None

# 左侧导航栏设计
st.sidebar.title("硅基陪伴选型系统")
st.sidebar.markdown("成都市具身智能陪伴机器人消费决策与场景体验平台")
st.sidebar.divider()

pages = ["平台首页", "智能需求测评", "画像与产品匹配", "沉浸式场景体验"]
selected_page = st.sidebar.radio("系统导航", pages, index=pages.index(st.session_state.current_page))
st.session_state.current_page = selected_page

def go_to_page(page_name):
    st.session_state.current_page = page_name


# ================= 3. 页面一：平台首页 =================
if st.session_state.current_page == "平台首页":
    st.title("具身智能陪伴机器人体验与选型平台")
    st.markdown("<h4 style='color: #6c757d; font-weight: 400;'>选对陪伴机器人，从精准的数据驱动测评开始。</h4>", unsafe_allow_html=True)
    st.divider()
    
    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("""
        <div class="st-card">
        <h3>项目研发背景</h3>
        <p>在“人工智能+”与“孤独经济”背景下，具身智能陪伴机器人正成为满足社交代偿与情感慰藉需求的重要产品。</p>
        <p>本系统基于成都市核心城区 693 份有效问卷数据，利用 <strong>XGBoost 归因模型</strong> 与 <strong>K-means 聚类算法</strong> 驱动。</p>
        <p>旨在解决当前市场“高认知、低转化”的痛点，帮助消费者匹配最适宜的智能伴侣形态与商业订阅模式。</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("开始我的专属选型测评"):
            st.session_state.current_page = "智能需求测评"
            st.rerun()
            
    with col2:
        # 这里预留给你们放一张高大上的项目海报或产品概念图
        st.info("[预留展示位]：此处可插入项目海报或具身智能机器人的概念演示视频。")
        # 实际部署时，将代码替换为： st.image("您的图片链接或本地路径", use_container_width=True)


# ================= 4. 页面二：智能需求测评 (深度还原问卷) =================
elif st.session_state.current_page == "智能需求测评":
    st.title("智能需求深度测评")
    st.markdown("系统将根据您的真实生活场景，实时计算匹配权重。")
    st.divider()
    
    with st.form("assessment_form"):
        st.markdown("#### 第一部分：生活图谱与家庭结构")
        q_family = st.radio("1. 您目前的家庭居住结构是？", 
                            ["独居（一人居住）", 
                             "二人家庭（无子女）", 
                             "有孩家庭（子女18岁以下）", 
                             "多代同堂（含60岁以上老人）"])
        
        st.markdown("#### 第二部分：技术准备度与隐私阈值")
        q_tech = st.radio("2. 您对前沿科技产品（如AI大模型、人形机器人）的态度是？",
                          ["极度狂热，愿意第一时间高价尝鲜",
                           "比较感兴趣，看是否有实际用处再决定",
                           "比较保守，更习惯传统的生活方式"])
        
        q_privacy = st.select_slider("3. 您对机器人收集家庭视觉/语音数据的顾虑程度？",
                                     options=["极度担忧(要求纯物理断网)", "中度担忧", "完全不担忧(接受云端上传)"], value="中度担忧")
        
        st.markdown("#### 第三部分：商业价值与预算预期")
        q_budget = st.selectbox("4. 针对陪伴机器人，您能接受的最高购买预算是？", 
                                ["3000元以下", "3001-8000元", "8001-15000元", "15000元以上"])
        
        q_payment = st.radio("5. 对于机器人的“AI大脑”持续升级，您更倾向于哪种付费模式？",
                             ["终身买断制（购机后软件永久免费升级）",
                              "功能订阅制（基础功能免费，高级情感能力按月付费）",
                              "共享模式（不拥有所有权，按使用服务时长付费）"])
        
        st.divider()
        submitted = st.form_submit_button("提交数据，生成专属画像")
        
        if submitted:
            # 核心后台分类逻辑（映射报告的 K-means 四类人群）
            persona = "普惠务实派" # 默认基础分类
            
            if q_family == "有孩家庭（子女18岁以下）":
                persona = "亲子伴学派"
            elif q_family == "多代同堂（含60岁以上老人）" or q_tech == "比较保守，更习惯传统的生活方式":
                persona = "传统保守派"
            elif ("独居" in q_family or "二人家庭" in q_family) and ("15000" in q_budget or "8001" in q_budget) and "尝鲜" in q_tech:
                persona = "高知尝鲜派"
            elif "订阅" in q_payment or "3000元以下" in q_budget:
                persona = "普惠务实派"
                
            st.session_state.persona = persona
            st.session_state.current_page = "画像与产品匹配"
            st.rerun()


# ================= 5. 页面三：画像与产品匹配 =================
elif st.session_state.current_page == "画像与产品匹配":
    if not st.session_state.persona:
        st.warning("请先完成智能需求测评，以获取您的专属推荐方案。")
        if st.button("前往测评"):
            st.session_state.current_page = "智能需求测评"
            st.rerun()
    else:
        st.title("消费者画像与市场转化方案")
        
        with st.spinner("系统正在调取 K-means 聚类特征库..."):
            time.sleep(1)
            
        persona = st.session_state.persona
        
        # 模块 A：画像展示
        st.markdown(f"""
        <div class="st-card">
            <h2 style='color: #0056b3;'>系统识别结果：{persona}</h2>
            <hr>
        </div>
        """, unsafe_allow_html=True)
        
        # 模块 B：商业模式与产品配置
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 推荐产品形态与功能配置")
            if persona == "高知尝鲜派":
                st.info("**方案级别**：高阶多模态交互款")
                st.write("1. **核心交互**：接入千亿参数大模型，支持拟人化情绪记忆。")
                st.write("2. **物理硬件**：仿生柔性温控皮肤（36.5°C）+ 复杂地形避障雷达。")
                st.write("3. **隐私配置**：端云结合，本地处理敏感图像，云端处理通用对话。")
            elif persona == "亲子伴学派":
                st.info("**方案级别**：教育管家看护款")
                st.write("1. **核心交互**：绘本视觉识别 + 儿童声纹专属唤醒。")
                st.write("2. **物理硬件**：环保防摔抗造外壳 + 柔性无锐角设计。")
                st.write("3. **隐私配置**：物理级摄像头遮蔽罩，断网状态下的全本地离线运行。")
            elif persona == "普惠务实派":
                st.info("**方案级别**：基础养成毛绒款")
                st.write("1. **核心交互**：精简版指令交互，主打基础的物理触觉治愈。")
                st.write("2. **物理硬件**：高品质仿生毛绒材质，重点优化使用续航时间。")
                st.write("3. **隐私配置**：无摄像头，仅保留语音唤醒阵列。")
            else:
                st.info("**方案级别**：极简适老看护款")
                st.write("1. **核心交互**：方言识别模块 + 单向亲情语音留言。")
                st.write("2. **物理硬件**：去屏幕化极简设计，大音量与强提示灯。")
                st.write("3. **隐私配置**：毫米波雷达跌倒监测（无视觉画面，绝对隐私保护）。")

        with col2:
            st.markdown("### 推荐商业变现与定价模式")
            if persona in ["普惠务实派", "亲子伴学派"]:
                st.success("**转化策略：HaaS（硬件即服务）订阅制**")
                st.write("基于您对价格和试错成本的敏感度，建议采用 HaaS 模式：")
                st.write("- **初始门槛**：提供免押金或极低价格的硬件“领养”服务。")
                st.write("- **后端盈利**：每月支付基础服务费，可根据成长需求随时订阅“早教资源包”或“性格升级插件”。")
                st.write("- **商业逻辑**：化解高昂的初始价格壁垒，建立长效的用户留存与数据反哺闭环。")
            else:
                st.warning("**转化策略：高溢价买断 + 专属尊享包**")
                st.write("基于您对前沿科技的高接受度与预算空间，建议采用买断模式：")
                st.write("- **初始门槛**：一次性高价买断核心硬件（彰显科技社交标签）。")
                st.write("- **后端盈利**：提供高算力的云端 API 极速响应通道会员，或专属的外观涂装配件。")
                st.write("- **商业逻辑**：通过极致体验满足情绪代偿的刚需，实现品牌溢价的最大化。")

        st.divider()
        if st.button("进入真实场景体验"):
            st.session_state.current_page = "沉浸式场景体验"
            st.rerun()


# ================= 6. 页面四：场景体验 =================
elif st.session_state.current_page == "沉浸式场景体验":
    if not st.session_state.persona:
        st.warning("请先完成智能需求测评。")
    else:
        persona = st.session_state.persona
        st.title("沉浸式场景体验中心")
        st.markdown(f"基于您的群体特征 **[{persona}]**，系统已为您匹配最佳产品落地场景。")
        st.divider()
        
        col_video, col_desc = st.columns([1.5, 1])
        
        with col_video:
            # 这里的 st.video 是为你们答辩准备的占位符。
            # 答辩前，如果有视频，可以用 st.video("你的视频路径.mp4") 替换。
            st.info("📺 [多媒体展示区] 答辩时，请在此处嵌入对应的产品运行或交互视频。")
            
        with col_desc:
            st.markdown("### 典型应用场景演示")
            if persona == "高知尝鲜派":
                st.write("**场景定义：深夜情感补位与压力释放**")
                st.write("您加班到深夜，推开家门。它通过视觉算法识别到您步伐沉重、面露疲态。它没有机械地进行语音播报，而是安静地走近，用带有温控系统的仿生外壳蹭您的腿部，并自动将室内灯光调暗，播放舒缓的白噪音。它成为了承接您都市孤独感的情感容器。")
            elif persona == "亲子伴学派":
                st.write("**场景定义：安全可控的离线伴读**")
                st.write("周末您需要居家办公，孩子在客厅玩耍。您通过物理按键关闭了机器人的联网功能，保护家庭隐私。机器人利用端侧算力，通过视觉模组精准识别孩子手中的纸质绘本，用高度拟人的声线开始讲故事。在孩子试图攀爬危险家具时，它能发出语音预警并向您的手机推送消息。")
            elif persona == "普惠务实派":
                st.write("**场景定义：基础治愈与轻量级互动**")
                st.write("对于生活节奏快、注重性价比的您，它化身为一只极度逼真的毛绒机械宠物。无需复杂的APP设置，当您坐在沙发上看剧时，顺手抚摸它的背部，它会发出呼噜声并做出伸懒腰的动作。简单的触觉与听觉反馈，以最低的成本为您提供了一份安稳的居家陪伴感。")
            else:
                st.write("**场景定义：无感知的适老安全网**")
                st.write("对于不在父母身边的您，它是一重安心保障。由于没有摄像头，老人不会有“被监视”的抵触感。当其内置的毫米波雷达监测到老人在卫生间区域长时间未移动，且姿态判定为异常跌倒时，机器人在本地迅速处理数据，在3秒内自动拨通您的紧急联系电话，完成生命通道的建立。")
        
        st.divider()
        if st.button("重新开始测评"):
            st.session_state.persona = None
            st.session_state.current_page = "平台首页"
            st.rerun()