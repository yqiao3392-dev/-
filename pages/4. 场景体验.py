import streamlit as st
import os

# ================= 1. 页面全局配置 =================
st.set_page_config(page_title="实体应用场景模拟 | 硅基陪伴系统", layout="wide")

# ================= 2. 样式注入 =================
# 尝试多个路径加载CSS，确保样式不丢失，且失败时不报错
css_loaded = False
for css_path in ["style/custom.css", "../style/custom.css", "custom.css"]:
    try:
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
            css_loaded = True
            break
    except FileNotFoundError:
        continue

if not css_loaded:
    st.markdown("""
        <style>
        .main { background-color: #FAFAFA; }
        .scenario-box { 
            background-color: #FFFFFF; 
            padding: 24px; 
            border-radius: 4px; 
            border-left: 4px solid #1A2B4C;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        }
        .product-header {
            font-size: 24px;
            font-weight: 600;
            color: #1A2B4C;
            border-bottom: 1px solid #EAEAEA;
            padding-bottom: 12px;
            margin-bottom: 24px;
        }
        </style>
    """, unsafe_allow_html=True)

# ================= 3. 状态获取与数据映射 =================
persona = st.session_state.get("persona_result", "高知尝鲜派")
st.sidebar.info(f"当前目标客群：{persona}")

data_map = {
    "高知尝鲜派": {
        "title": "方案 A：高阶交互型产品（情感代偿导向）",
        "products": [
            {"name": "Tesla Optimus", "file": "optimus.jpg", "desc": "具备高精度触觉感知与多模态决策能力的通用人形机器人平台。"},
            {"name": "Loona 智能终端", "file": "loona.jpg", "desc": "支持拟人化情绪反馈与自主交互逻辑，主打社交代偿体验。"}
        ],
        "scenario": "核心验证场景：深夜情感补位与压力释放<br><br>在独居城市白领的高频生活切面中，设备不仅是科技展品，更是情绪的承接者。当用户深夜归家，设备依托云端大模型与视觉算法，敏锐捕捉用户的疲态微表情。主动靠近并通过高拟真的柔性接触提供物理慰藉，同时联动全屋智能调暗灯光，开启深度解压对话模式，实现从工具理性向情感代偿的跨越。"
    },
    "亲子伴学派": {
        "title": "方案 B：实用管家型产品（教育与安全导向）",
        "products": [
            {"name": "Enabot EBO X", "file": "ebox.jpg", "desc": "集成家庭全屋安防巡航、声纹鉴权与儿童教育数字资源库。"}
        ],
        "scenario": "核心验证场景：安全的离线伴读与立体防线<br><br>针对中产家庭强烈的隐私防御与育儿减压诉求，该终端在进入儿童陪伴模式后，将自动切断云端连接，依靠强大的本地端侧算力进行绘本视觉识别与辅导。同时，设备在家庭公共区域巡航时，可实时识别儿童危险攀爬等行为，并即时向父母终端推送预警，完美达成安全看护与教育陪伴的双重功能替代。"
    },
    "普惠务实派": {
        "title": "方案 C：基础养成型产品（触觉治愈导向）",
        "products": [
            {"name": "Ropet 仿生伴侣", "file": "ropet.jpg", "desc": "采用仿生材质优化物理亲和力，专注于基础的解压与轻量级互动反馈。"}
        ],
        "scenario": "核心验证场景：低门槛的居家轻度解压<br><br>落实“做减法”理念，剥离昂贵且冗余的大模型算力，回归陪伴的物理本质。在快节奏的日常生活中，用户无需复杂的系统设定。在沙发小憩时，设备通过内置的高精度触摸传感器矩阵，在被抚摸时输出平稳的声学反馈与微弱的肢体震动。以最低的决策成本缓解用户的精神内耗。"
    },
    "传统保守派": {
        "title": "方案 D：适老辅助型产品（无感健康监测导向）",
        "products": [
            {"name": "适老版看护终端", "file": "ebox.jpg", "desc": "剔除复杂屏幕交互，专注于毫米波雷达跌倒监测与紧急呼救服务。"}
        ],
        "scenario": "核心验证场景：捍卫尊严的无感式适老看护<br><br>面对老年群体强烈的技术排斥与隐私敏感，系统彻底摒弃了摄像头的全天候开启。依托内置的毫米波雷达，设备在不侵犯隐私的前提下，全天候被动监测老人的生命体征与姿态。一旦发生洗手间跌倒等突发状况，设备在本地瞬时研判，3秒内直连子女手机报警。以看不见的守护降低老年群体的防御心理。"
    }
}

content = data_map[persona]

# ================= 4. 页面渲染 =================
st.title("具身智能陪伴机器人：场景落地体验模拟")
st.markdown(f"<div class='product-header'>{content['title']}</div>", unsafe_allow_html=True)

cols = st.columns(len(content['products']))

for i, product in enumerate(content['products']):
    with cols[i]:
        filename = product['file']
        
        # 智能路径检索机制：无论图片存在 GitHub 的哪个层级，都能自动抓取
        possible_paths = [
            f"assets/products/{filename}",
            f"assets/{filename}",
            filename,
            f"../assets/products/{filename}",
            f"../{filename}"
        ]
        
        image_displayed = False
        for path in possible_paths:
            if os.path.exists(path):
                st.image(path, use_container_width=True)
                image_displayed = True
                break
                
        # 如果穷举了所有路径还是找不到文件，强制调用标准组件（不再输出任何文字占位符）
        if not image_displayed:
            try:
                st.image(filename, use_container_width=True)
            except:
                pass
                
        st.markdown(f"<div style='text-align:center; color:#666; font-size:13px; margin-top:8px;'>硬件形态参考：{product['name']}</div>", unsafe_allow_html=True)
        st.write(f"**产品定位**：{product['desc']}")

st.write("\n")
st.subheader("核心应用场景模拟")
st.markdown(f"<div class='scenario-box'>{content['scenario']}</div>", unsafe_allow_html=True)

st.divider()

col_btn1, col_btn2 = st.columns(2)
with col_btn1:
    try:
        st.page_link("pages/2_市场洞察.py", label="查看模型归因结论")
    except:
        pass 
with col_btn2:
    if st.button("重新开始测评"):
        st.session_state.assessment_completed = False
        st.session_state.persona_result = None
        try:
            st.switch_page("pages/3_智能选型.py")
        except:
            st.info("测评已重置，请通过侧边栏返回。")