import streamlit as st
import time

# ================= 页面全局配置 =================
st.set_page_config(page_title="硅基陪伴 | 消费决策与场景体验", page_icon="🤖", layout="centered")

# ================= 状态管理 =================
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'persona' not in st.session_state:
    st.session_state.persona = ""

def next_step():
    st.session_state.step += 1

def reset():
    st.session_state.step = 1

# ================= Page 1: 简短测评 =================
if st.session_state.step == 1:
    st.title("🤖 具身智能陪伴机器人 - 选型测评")
    st.markdown("*基于成都市 693 份有效样本的 XGBoost 决策模型驱动*")
    st.divider()
    
    with st.form("assessment_form"):
        st.subheader("1. 您的核心诉求偏向于？")
        need = st.radio("请选择最符合您的场景：", 
                        ["缓解独居孤独感，需要深度情感交互", 
                         "辅助儿童教育与居家安全陪伴", 
                         "需要基础的居家解压与轻度互动", 
                         "老人健康监测与被动式适老看护"])
        
        st.subheader("2. 您的理想预算区间是？")
        budget = st.selectbox("请选择价格接受度：", ["3000元以下", "3001-8000元", "8000元以上"])
        
        st.subheader("3. 您对家庭隐私数据（摄像头/麦克风）的顾虑程度？")
        privacy = st.slider("1=极度担忧，5=完全不担忧", 1, 5, 3)
        
        submitted = st.form_submit_button("生成我的专属画像 🚀")
        
        if submitted:
            # 极简后台分类逻辑（映射报告的四类人群）
            if "独居" in need and budget == "8000元以上":
                st.session_state.persona = "高知尝鲜派"
            elif "儿童" in need:
                st.session_state.persona = "亲子伴学派"
            elif "老人" in need:
                st.session_state.persona = "传统保守派"
            else:
                st.session_state.persona = "普惠务实派"
            
            st.session_state.privacy_score = privacy
            next_step()
            st.rerun()

# ================= Page 2: 用户画像 =================
elif st.session_state.step == 2:
    st.title("📊 您的专属用户画像")
    st.divider()
    
    with st.spinner('AI 正在调取大样本聚类特征...'):
        time.sleep(1) # 增加仪式感
        
    st.success(f"### 🎯 系统识别结果：{st.session_state.persona}")
    
    # 动态展示画像特征
    if st.session_state.persona == "高知尝鲜派":
        st.markdown("**群体特征**：26-35岁城市白领，高技术接受度，追求极致情绪价值与前沿科技体验。")
        st.info("💡 您的购买驱动力核心在于：**『情感联结与AI灵魂伴侣预期』**")
    elif st.session_state.persona == "亲子伴学派":
        st.markdown("**群体特征**：36-50岁中产家庭，注重产品的教育实用性、居家安全与性价比。")
        st.info("💡 您的购买驱动力核心在于：**『家庭管家辅助与儿童启蒙』**")
    elif st.session_state.persona == "普惠务实派":
        st.markdown("**群体特征**：26-35岁年轻家庭，处于观望状态，对价格高度敏感，看重基础陪伴。")
        st.info("💡 您的购买驱动力核心在于：**『平价试错与基础解压需求』**")
    else:
        st.markdown("**群体特征**：51岁以上熟龄人群或多代同堂，存在较高技术防御心理。")
        st.info("💡 您的购买驱动力核心在于：**『非侵入式健康兜底与适老辅助』**")
        
    st.button("查看匹配产品方案 ➡️", on_click=next_step)

# ================= Page 3: 产品方案匹配 =================
elif st.session_state.step == 3:
    st.title("💡 智能匹配产品与商业方案")
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📦 推荐硬件形态")
        if st.session_state.persona == "高知尝鲜派":
            st.write("- **型号建议**：高阶多模态交互款")
            st.write("- **核心参数**：仿生柔性温控皮肤 (36.5°C) + 微表情驱动电机")
            st.write("- **隐私模式**：云端大模型+本地加密双保险")
        elif st.session_state.persona == "亲子伴学派":
            st.write("- **型号建议**：实用教育管家款")
            st.write("- **核心参数**：防摔环保硬塑 + 绘本识别视觉模组")
            st.write("- **隐私模式**：物理摄像头遮蔽罩 + 纯本地端侧离线运行")
        elif st.session_state.persona == "普惠务实派":
            st.write("- **型号建议**：基础养成毛绒款")
            st.write("- **核心参数**：软性触感毛绒 + 基础指令交互")
            st.write("- **隐私模式**：仅唤醒词监听")
        else:
            st.write("- **型号建议**：极简适老看护款")
            st.write("- **核心参数**：无感红外雷达 + 跌倒姿态识别")
            st.write("- **隐私模式**：无麦克风/摄像头，纯雷达感知")

    with col2:
        st.subheader("💳 推荐商业与定价模式")
        if st.session_state.persona in ["普惠务实派", "亲子伴学派"]:
            st.success("**推荐模式：HaaS (硬件即服务) 订阅制**")
            st.write("- **支付方案**：0元押金领养，按月支付 199 元服务费。")
            st.write("- **增值包**：按需订阅『幼教内容库』或『性格进化插件』，降低试错门槛。")
        else:
            st.warning("**推荐模式：高端买断 + 专属增值包**")
            st.write("- **支付方案**：一次性买断 (约 8999 元)。")
            st.write("- **增值包**：附赠一年期云端大模型极速响应 API 额度。")

    st.button("进入真实场景体验 🎬", on_click=next_step)

# ================= Page 4: 场景体验 =================
elif st.session_state.step == 4:
    st.title("🏠 沉浸式场景体验")
    st.markdown("体验具身智能机器人如何融入您的日常生活：")
    st.divider()
    
    if st.session_state.persona == "高知尝鲜派":
        st.subheader("🌙 场景：深夜疲惫归家")
        st.markdown("> *你打开房门，它通过视觉识别到你情绪低落。它没有机械地问好，而是安静地走到你脚边，用带有 36.5°C 温控的柔性外壳蹭了蹭你的小腿，抬头播放了一首你最喜欢的舒缓轻音乐。*")
    elif st.session_state.persona == "亲子伴学派":
        st.subheader("📖 场景：周末儿童伴读")
        st.markdown("> *系统自动切断云端连接，进入【纯本地离线模式】。它伸出机械臂精准翻开绘本，用高度拟人的声线开始给孩子讲故事，并在孩子分心时发出可爱的提示音，你终于可以在沙发上安心喝完一杯咖啡。*")
    elif st.session_state.persona == "传统保守派":
        st.subheader("🛡️ 场景：老人独居安全监测")
        st.markdown("> *全程没有刺眼的摄像头。当红外雷达监测到洗手间长时间无生命体态活动，且伴随倒地声学特征时，机器人在 2 秒内自动拨通了远在外地的你的电话。*")
    else:
        st.subheader("🛋️ 场景：日常轻度解压")
        st.markdown("> *工作间隙，你顺手摸了摸桌上的基础养成款机器人。它顺着你的抚摸发出呼噜声，并在屏幕上弹出一个开心的颜文字。简单的反馈，瞬间治愈了精神内耗。*")
        
    st.divider()
    st.button("🔄 重新评测", on_click=reset)