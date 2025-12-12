# 导入streamlit库
import streamlit as st
# 导入pandas库
import pandas as pd


# 设置页面主标题，添加表情符号
st.title("音乐--薄荷鱼🎧的歌单日志")

# 添加分割线
st.markdown('***')


# 设置二级标题（header），标注模块名称+音乐表情
st.header('基础听歌数据🎵')

# 展示总收藏歌曲数，用红色文本
st.markdown('总收藏歌曲：:red[328首]')

# 展示年度听歌时长，红色文本突出
st.markdown('年度听歌时长：:red[1280小时]')

# 展示最近一周听歌时长，红色文本突出
st.markdown('最近一周听歌：:red[28小时]')

# 展示常用听歌设备，红色文本+耳机表情突出
st.markdown('常用听歌设备：:red[手机/耳机🎧️]')



# 设置三级标题，标注分类列表模块+笔记表情
st.markdown('### 分类列表📝')

# 创建三列布局，用于并列展示3个分类的热度数据
col1, col2, col3 = st.columns(3)

# 第一列：最近分类的热度数据
with col1:
    # 分类名称（加粗显示）
    st.markdown('**最近**')
    # 热度值（三级标题样式突出显示）
    st.markdown('### 95%')
    # 热度变化：绿色文本+上升箭头，标注上升2%
    st.markdown(':green[↑+2%]')

# 第二列：收藏分类的热度数据
with col2:
    # 分类名称（加粗显示）
    st.markdown('**收藏**')
    
    st.markdown('### 87%')
    # 热度变化：红色文本+下降箭头，标注下降1%
    st.markdown(':red[↓-1%]')

# 第三列：博客分类的热度数据
with col3:
    # 分类名称（加粗显示）
    st.markdown('**博客**')
    # 热度值（三级标题样式突出显示）
    st.markdown('### 68%')
    # 热度变化：红色文本+下降箭头，标注下降10%
    st.markdown(':red[↓-10%]')
    

# 添加分割线，分隔分类列表和歌单进度模块
st.markdown('***')



# 设置三级标题，
st.markdown('### 歌单听歌进度⏯︎')

# 进度条说明文本：指定对应的歌单名称
st.markdown('「通勤必备」歌单完成度')

# 定义进度值（0-1之间，0.65对应65%）
progress = 0.65
# 展示进度条组件
st.progress(progress)

# 添加分割线
st.markdown('***')


# 歌单听歌日志模块，三级标题

st.markdown('### 歌单听歌日志✏️')
# 构造日志数据字典，包含日期、歌单名称、状态、喜爱度4个字段
log_data = {
    "日期": ["2025-12-01", "2025-12-05", "2025-12-10"],  # 听歌日期
    "歌单名称": ["《小孩》", "《后陡门的夏》", "《宠爱》"],  # 歌单名称
    "状态": ["✅ 已听完", "🔄 收听中", "❌ 未开始"],  # 听歌状态
    "喜爱度": ["⭐️⭐️⭐️⭐️", "⭐️⭐️⭐️", "⭐️⭐️⭐️⭐️⭐️"]  # 喜爱度星级
}
# 将字典转换为表格展示（DataFrame）
st.dataframe(
    log_data,  # 要展示的数据源
    hide_index=True,  # 隐藏表格默认的索引列（更简洁）
    use_container_width=True  # 表格宽度适配页面容器
)

# 添加分割线，分隔听歌日志和音乐脚本模块
st.markdown('***')

# 音乐收藏脚本模块
# 设置三级标题，标注模块名称+音乐表情
st.markdown('### 🎵 音乐收藏脚本')

# 定义Python脚本字符串，实现收藏歌曲的功能
music_script = '''def collect_favorite_songs():
    favorite_list = []  # 初始化空列表，用于存储收藏的歌曲
    while True:  # 无限循环，直到输入“结束”
        song = input("输入想收藏的歌曲：")  # 提示用户输入歌曲名
        if song == "结束":  # 判断是否输入“结束”
            print("收藏完成！当前歌单：", favorite_list)  # 打印收藏结果
            return favorite_list  # 返回收藏列表，结束函数
        else:  # 输入的是歌曲名
            favorite_list.append(song)  # 将歌曲名添加到收藏列表
            print(f"已收藏：{song}")  # 提示已收藏该歌曲'''

# 展示代码块，指定语言为Python，显示行号
st.code(music_script, language="python", line_numbers=True)


# 添加分割线
st.markdown('***')


# 音乐歌单更新提示模块，三级标题

st.markdown('### 🎧 歌单更新提示')
# 系统提示：绿色文本，告知新歌曲已加入
st.markdown('> :green[>> SYSTEM MESSAGE: 新歌曲已加入歌单...]')
# 新歌提示：蓝色文本，标注新增歌曲名称和歌手
st.markdown('> :blue[>> NEW SONG: 《七里香》（周杰伦）]')
# 更新时间：橙色文本，标注歌单更新时间
st.markdown('> :orange[>> UPDATE TIME: 2025-12-12 19:30:00]')
# 空行，分隔提示文本和状态文本
st.markdown('')
# 展示歌单当前状态：更新状态和播放状态
st.markdown('歌单状态：已更新 | 播放状态：可收听')
