import streamlit as st
import os

# ================= 1. 页面全局配置 =================
st.set_page_config(page_title="实体应用场景模拟 | 硅基陪伴系统", layout="wide")

# ================= 2. 样式注入 (优先调用外部 CSS) =================
def load_css(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        # 如果外部 CSS 不存在，注入基础商务样式作为兜底
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
            .img-caption { text-align: center; color: #666; font-size: 13px; margin-top: 8px; }
            </style>
        """, unsafe_allow_html=True)

load_css("style/custom.css")

# ================= 3. 状态获取与数据映射 =================
# 获取智能选型页面测出的结果，默认为高知尝鲜派
persona = st.session_state.get("persona_result", "高知尝鲜派")
st.sidebar.info(f"当前目标客群：{persona}")

# 深度对齐报告语录的数据字典
data_map = {
    "高知尝鲜派": {
        "title": "方案 A：高阶交互型产品（情感代偿导向）",
        "products": [
            {"name": "Tesla Optimus", "file": "optimus.jpg", "desc": "具备高精度触觉感知与多模态决策能力的通用人形机器人平台。"},
            {"name": "Loona 智能终端", "file": "loona.jpg", "desc": "支持拟人化情绪反馈与自主交互逻辑，主打社交代偿体验。"}
        ],
        "scenario": "情感抚慰场景：系统通过视觉算法识别用户疲态，激活柔性温控模块提供物理触觉反馈，并自动调用解压对话逻辑模型。通过物理实体的实时介入，缓解由于高强度社交真空带来的情感缺失，实现从工具理性向情感代偿的跨越。"
    },
    "亲子伴学派": {
        "title": "方案 B：实用管家型产品（教育与安全导向）",
        "products": [
            {"name": "Enabot EBO X", "file": "ebox.jpg", "desc": "集成家庭全屋安防巡航、声纹鉴权与儿童教育数字资源库。"}
        ],
        "scenario": "离线伴读场景：设备通过物理级摄像头遮蔽罩确保隐私边界。在识别儿童伴读需求后，依托端侧算力进行绘本识别，同步开启居家异常状态（如危险攀爬、跌倒）预警。在解决家长看护压力的同时，满足家庭教育的实用功能性替代。"
    },
    "普惠务实派": {
        "title": "方案 C：基础养成型产品（触觉治愈导向）",
        "products": [
            {"name": "Ropet 仿生伴侣", "file": "ropet.jpg", "desc": "采用仿生材质优化物理亲和力，专注于基础的解压与轻量级互动反馈。"}
        ],
        "scenario": "轻度解压场景：落实“做减法”理念，剥离昂贵且冗余的算力。依靠内置的物理触感反馈矩阵，设备在被抚摸时输出呼噜声或微量震动。以低成本的物理互动瓦解大众对于高价科技产品的观望心理，提供稳定且非侵入式的居家治愈体验。"
    },
    "传统保守派": {
        "title": "方案 D：适老辅助型产品（无感健康监测导向）",
        "products": [
            {"name": "适老版看护终端", "file": "ebox.jpg", "desc": "剔除复杂屏幕交互，专注于毫米波雷达跌倒监测与紧急呼救服务。"}
        ],
        "scenario": "无感看护场景：系统完全禁用视觉采集，全程采用非侵入式的雷达感知老人生命体征。当监测到洗手间区域异常倒地且伴随声学特征突变时，系统即刻触发异地预警。以“看不见的守护”降低老年群体的防御心理，实现家庭安全底线的兜底。"
    }
}

content = data_map[persona]

# ================= 4. 页面渲染 =================
st.title("具身智能陪伴机器人：场景落地体验模拟")
st.markdown(f"<div class='product-header'>{content['title']}</div>", unsafe_allow_html=True)

# 展示推荐产品图片
cols = st.columns(len(content['products']))

for i, product in enumerate(content['products']):
    with cols[i]:
        # 严格检查 assets/products/ 路径下的图片
        img_path = f"assets/products/{product['file']}"
        
        if os.path.exists(img_path):
            st.image(img_path, use_container_width=True)
            st.markdown(f"<div class='img-caption'>硬件形态参考：{product['name']}</div>", unsafe_allow_html=True)
        else:
            # 商务感占位符，不报错
            st.markdown(f"""
                <div style="background:#F0F0F0; border:1px dashed #CCC; padding:60px 20px; text-align:center; color:#888;">
                    [产品视觉预留区]<br>请确保文件放置于：<br><b>{img_path}</b>
                </div>
            """, unsafe_allow_html=True)
        
        st.write(f"**产品定位**：{product['desc']}")

st.write("\n")
st.subheader("核心应用场景模拟")
st.markdown(f"<div class='scenario-box'>{content['scenario']}</div>", unsafe_allow_html=True)

st.divider()

# 导航闭环
col_btn1, col_btn2 = st.columns(2)
with col_btn1:
    try:
        st.page_link("pages/2_📊_市场洞察.py", label="查看模型归因结论", icon="📊")
    except:
        pass # 防止路径名称微调导致报错
with col_btn2:
    if st.button("重新开始测评"):
        st.session_state.assessment_completed = False
        st.session_state.persona_result = None
        # 根据你的文件名进行自动匹配
        try:
            st.switch_page("pages/3_🤖_智能选型.py")
        except:
            st.info("测评已重置，请通过左侧导航栏返回测评页面。")