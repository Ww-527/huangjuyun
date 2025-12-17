import streamlit as st
import pandas as pd

#  全局页面配置
st.set_page_config(
    page_title="我的实训作品集",
    page_icon="📚",
    layout="wide"
)


st.title("📁 我的Streamlit实训作品集")
st.markdown("---")
st.image(
        "https://ts2.tc.mm.bing.net/th/id/OIP-C.36rbRDot0DjjUYtWzOhLaAHaFj?cb=ucfimg2&ucfimg=1&rs=1&pid=ImgDetMain&o=7&rm=3",
        use_container_width=True  
    )
# 极简版首页内容（仅保留关键信息）
st.markdown("""
    ### 👋 实训合集简介
    基于Streamlit开发的Python实战项目，包含5个核心模块：
    - 音乐歌单数据可视化
    - 南宁美食流量分析
    - 交互式相册
    - 简易音乐播放器
    - 视频剧集播放
    
    ### 📌 核心目标
    掌握Streamlit交互组件、数据可视化、多媒体展示能力
    """)
st.markdown("---")
