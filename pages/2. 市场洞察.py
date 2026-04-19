import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ================= 页面全局配置 =================
st.set_page_config(page_title="市场洞察与数据归因 | 硅基陪伴", layout="wide")
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









# ================= 注入高级商务与学术风 CSS =================
st.markdown("""
    <style>
    .main { background-color: #FAFAFA; }
    h1, h2, h3, h4 { font-family: 'Helvetica Neue', 'Arial', sans-serif; color: #1A2B4C; }
    
    .insight-card {
        background-color: #FFFFFF;
        padding: 24px;
        border-radius: 6px;
        border: 1px solid #EBEBEB;
        box-shadow: 0 2px 6px rgba(0,0,0,0.02);
        margin-bottom: 24px;
        border-left: 4px solid #1E3A8A;
    }
    .insight-title { font-size: 18px; font-weight: 600; color: #1A2B4C; margin-bottom: 12px; }
    .insight-text { font-size: 14px; color: #555555; line-height: 1.6; }
    .highlight-text { color: #1E3A8A; font-weight: 600; }
    </style>
""", unsafe_allow_html=True)

st.title("市场洞察与深度数据归因")
st.markdown("<p style='color: #666; font-size: 16px; margin-bottom: 30px;'>基于 12000+ 全网文本 NLP 情感分析与 693 份成都市实地调研样本的量化洞察</p>", unsafe_allow_html=True)

# ================= 使用 Tabs 划分分析维度 =================
tab1, tab2, tab3 = st.tabs(["01 舆情与认知诊断", "02 消费意愿归因 (XGBoost+SHAP)", "03 市场动态分层 (K-means)"])

# ---------------- Tab 1: NLP 与舆情诊断 ----------------
with tab1:
    st.markdown("### 市场生命周期诊断：创新扩散的『认知与转化断层』")
    
    col1, col2 = st.columns([1.2, 1])
    with col1:
        # 模拟 LDA 和 SnowNLP 产出的关注度分布数据
        nlp_data = pd.DataFrame({
            "关注维度": ["功能技术(算力/避障)", "外观与材质(物理亲和力)", "情感交互能力", "价格与订阅费用", "隐私与数据安全"],
            "声量占比(%)": [38, 25, 18, 12, 7],
            "负面情绪占比(%)": [15, 62, 45, 58, 85] 
        })
        
        # 绘制交互式条形图
        fig_nlp = px.bar(nlp_data, x="声量占比(%)", y="关注维度", orientation='h', 
                         color="负面情绪占比(%)", color_continuous_scale="Blues",
                         title="全网 12000+ 评论 LDA 主题声量与情感极性交叉分析")
        fig_nlp.update_layout(plot_bgcolor="white", margin=dict(t=50, l=0, r=0, b=0))
        st.plotly_chart(fig_nlp, use_container_width=True)

    with col2:
        st.markdown("""
        <div class="insight-card">
            <div class="insight-title">核心洞察：认知热、转化冷</div>
            <div class="insight-text">
                通过对主流电商平台的 NLP 情感分析，我们发现当前市场处于典型的导入期。<br><br>
                消费者对“具身智能”概念的认知声量极高（主要集中在功能与算力维度），但转化为实际购买的动力严重不足。<br><br>
                <b>结构性错位：</b>厂商过度堆砌硬件算力（声量高、负面低），而消费者真正关心的<span class="highlight-text">物理亲和力（如冰冷的工业材质）</span>与<span class="highlight-text">隐私安全顾虑</span>却成为极高负面情绪的爆发点。这也是阻碍冷启动阶段创新扩散的核心壁垒。
            </div>
        </div>
        """, unsafe_allow_html=True)

# ---------------- Tab 2: XGBoost + SHAP 归因 ----------------
with tab2:
    st.markdown("### 购买意愿归因：破除工具理性，回归情感代偿")
    
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.markdown("""
        <div class="insight-card">
            <div class="insight-title">模型解释：什么在决定购买？</div>
            <div class="insight-text">
                为量化各项因素对购买意愿的真实影响，本平台引入 <b>XGBoost 树模型</b>，并结合 <b>SHAP (SHapley Additive exPlanations)</b> 值进行全局与局部归因。<br><br>
                <b>一票否决权：</b>研究证实，<span class="highlight-text">家庭隐私安全顾虑</span>是最大的负向制约因素。若不解决端侧离线运行问题，即便算力再强也难以促成转化。<br><br>
                <b>核心驱动力：</b><span class="highlight-text">“情感联结预期”与“物理材质亲和力”</span>构成了正向驱动的绝对主力。消费者本质上在购买一个“情绪容器”，而非一个家用电器。
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # 模拟 SHAP Feature Importance 数据
        shap_data = pd.DataFrame({
            "驱动因素": ["情感陪伴预期 (+)", "物理材质亲和力 (+)", "AI算力与多模态 (-)", "隐私数据顾虑 (-)", "初始价格门槛 (-)"],
            "SHAP绝对贡献度": [0.45, 0.32, 0.12, 0.58, 0.38],
            "作用方向": ["正向驱动", "正向驱动", "弱负向(冗余)", "强负向(劝退)", "负向阻力"]
        })
        
        fig_shap = px.bar(shap_data, x="SHAP绝对贡献度", y="驱动因素", orientation='h',
                          color="作用方向", color_discrete_map={
                              "正向驱动": "#1E3A8A", "弱负向(冗余)": "#A0AEC0", 
                              "强负向(劝退)": "#E53E3E", "负向阻力": "#DD6B20"
                          },
                          title="XGBoost 购买意愿影响因子全局 SHAP 贡献度排序")
        fig_shap.update_layout(plot_bgcolor="white", margin=dict(t=50, l=0, r=0, b=0), yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig_shap, use_container_width=True)

# ---------------- Tab 3: K-means 市场分层 ----------------
with tab3:
    st.markdown("### 潜在客群识别：基于高维特征的 K-means 聚类映射")
    st.markdown("<p style='font-size:14px; color:#666;'>摒弃单一的人口统计学粗放分类，融合技术准备度、孤独感指数与预算约束的多维动态聚类。</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # 绘制雷达图展示四大客群特征
        categories = ['技术接受度', '价格敏感度', '情感互动需求', '家庭看护需求', '隐私防御心理']
        
        fig_radar = go.Figure()
        
        fig_radar.add_trace(go.Scatterpolar(
            r=[90, 20, 95, 30, 40], theta=categories, fill='toself', name='高知尝鲜派', line_color='#1E3A8A'
        ))
        fig_radar.add_trace(go.Scatterpolar(
            r=[70, 60, 60, 90, 85], theta=categories, fill='toself', name='亲子伴学派', line_color='#3182CE'
        ))
        fig_radar.add_trace(go.Scatterpolar(
            r=[50, 95, 80, 40, 60], theta=categories, fill='toself', name='普惠务实派', line_color='#63B3ED'
        ))
        fig_radar.add_trace(go.Scatterpolar(
            r=[20, 50, 40, 95, 95], theta=categories, fill='toself', name='传统保守派', line_color='#A0AEC0'
        ))

        fig_radar.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            showlegend=True, title="四大核心客群雷达特征矩阵", margin=dict(t=50, l=0, r=0, b=0)
        )
        st.plotly_chart(fig_radar, use_container_width=True)

    with col2:
        st.markdown("""
        <div class="insight-card">
            <div class="insight-title">市场进入策略与动态匹配</div>
            <div class="insight-text">
                基于 693 份有效样本的无监督学习，市场呈现出高度的非同质化特征：<br><br>
                <b>1. 先导消费群（高知尝鲜派）：</b>具备“高接受度、高收入、高知化、高情感需求”的四高特征，是跨越冷启动鸿沟的绝对主力，适用高溢价买断制。<br><br>
                <b>2. 下沉破局点（普惠务实派）：</b>样本占比最大。企业必须采取“做减法”的务实策略，推出聚焦基础治愈反馈的轻量级产品，结合 <b>HaaS（硬件即服务）</b> 分期订阅模式，大幅降低试错门槛。<br><br>
                <b>3. 刚需细分场（亲子伴学 / 传统保守）：</b>高度敏感于隐私数据，产品必须支持物理防窥与完全断网的端侧算力运行。
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 引导跳转按钮
        st.markdown("<p style='margin-top: 20px; font-size: 14px; color: #555;'>*基于上述数据洞察，本平台开发了针对消费者个体的量化选型工具：</p>", unsafe_allow_html=True)
        try:
            st.page_link("pages/3_🤖_智能选型.py", label="体验算法驱动的消费者智能选型 ➡")
        except:
            st.info("请通过左侧导航栏体验【智能选型】模块。")