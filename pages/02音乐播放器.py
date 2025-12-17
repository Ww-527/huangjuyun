import streamlit as st

st.title("🎵简易音乐播放器")
st.text("使用streamlit制作的简单音乐播放器，支持切歌和基本播放控制")

# 初始化当前歌曲索引
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

# 音乐+图片+音频URL 数据（替换为音频文件直链）
music_data = [
    {
        "name": "再见（good bye）", 
        "singer": "G.E.M.邓紫棋",
        "url": "http://p2.music.126.net/kVwk6b8Qdya8oDyGDcyAVA==/1364493930777368.jpg",
        "time": "5:55",
        "map3": "https://music.163.com/song/media/outer/url?id=2709447832.mp3",
        "text": "专辑封面"
    },
    {
        "name": "最好的我们", 
        "singer": "陈飞宇",
        "url": "https://so1.360tres.com/t0172e1255c71f0292e.jpg",
        "time": "4:30",
        "map3": "https://music.163.com/song/media/outer/url?id=2709447832.mp3"  ,
        "text": "专辑封面"
    },
    {
        "name": "起风了", 
        "singer": "买辣椒也用券",
        "url": "https://p1.music.126.net/diGAyEmpymX8G7JcnElncQ==/109951163699673355.jpg?param=300y300",
        "time": "3:45",
        "map3": "https://music.163.com/song/media/outer/url?id=1330348068.mp3" ,
        "text": "专辑封面"
    }
]
  


idx = st.session_state.ind
cur = music_data[idx]


# 核心布局：左列放图片，右列放音乐信息
col_left, col_right = st.columns([1, 2])

# 左列：显示当前歌曲的专辑封面
with col_left:
    st.image(music_data[st.session_state['ind']]['url'])
    st.caption("专辑封面")



# 右列：显示当前歌曲的信息+切歌按钮
with col_right:
    st.subheader(music_data[st.session_state['ind']]['name'])
    st.write(f"歌手: {music_data[st.session_state['ind']]['singer']}")
    st.write(f"时长: {music_data[st.session_state['ind']]['time']}")
   
    

# 切歌按钮
    btn1, btn2 = st.columns(2)
    with btn1:
        st.button(
            "◀上一首",
            on_click=lambda: st.session_state.update(ind=(st.session_state['ind']-1)%len(music_data)),
            use_container_width=True
        )
    with btn2:
        st.button(
            "下一首 ▶",
            on_click=lambda: st.session_state.update(ind=(st.session_state['ind']+1)%len(music_data)),
            use_container_width=True
        )



st.audio(music_data[st.session_state['ind']]['map3'],format="audio/mpeg")
    
