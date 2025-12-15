import streamlit as st
from PIL import Image  
import io  


st.set_page_config(page_title="个人简历生成器",page_icon="🖳",layout="wide")

# 顶部标题区域
st.markdown('# 🎨 个人简历生成器')
st.markdown('使用Streamlit创建您的个性化简历')
st.markdown('***')  

# 分栏布局：左侧表单(1份宽度)、右侧预览(2份宽度)
c1, c2 = st.columns([1, 2])

with c1:
    st.markdown('### 个人信息表单📋')
    st.markdown('***')
    
    # 基础信息输入
    user_name=st.text_input('姓名')
    user_position=st.text_input('职位')
    user_phone=st.text_input('电话号码')
    user_email=st.text_input('邮箱')
    user_birth = st.date_input("出生日期", value="2025-12-15")
    # 性别单选
    user_gender = st.radio("性别", ["男", "女", "其他"], index=0,horizontal=True)

    # 学历单选下拉（自定义格式函数）
    def format_edu(edu):
        return f'{edu}'
    user_edu = st.selectbox('学历', ['高中', '大专', '本科', '硕士', '博士', '博士后'], index=0, format_func=format_edu)

    # 语言能力多选下拉
    def format_language(language):
        return f'{language}'
    user_lang = st.multiselect('语言能力', ['中文', '日语', '英语', '德语', '西班牙语', '法语'], format_func=format_language)

    # 专业技能多选下拉（扩展技能选项）
    def format_skils(skils):
        return f'{skils}'
    user_skill = st.multiselect('技能（可多选）', ['Python', 'Java', 'SQL', '数据分析', '机器学习', '深度学习', '项目管理','UI/UX设计'], format_func=format_skils)

    # 工作经验滑块
    user_exp = st.slider('工作经验（年）', 0, 30, 0)

    # 薪资范围滑块
    st.markdown('### 期望薪资范围（元）')
    salary_range = st.slider("选择期望薪资", min_value=0, max_value=50000, value=(10000, 20000), step=1000, label_visibility="collapsed")

    # 个人简介文本域
    st.markdown('### 个人简历')
    user_intro = st.text_area(label='', placeholder='请简要介绍您的专业背景、职业目标和个人特点...', label_visibility="collapsed")

    # 联系时间下拉（每15分钟一个选项，默认09:00）
    st.markdown('### 每日最佳联系时间段')
    time_options = [f"{hour:02d}:{minute:02d}" for hour in range(24) for minute in [0, 15, 30, 45]]
    user_contact = st.selectbox(label="", options=time_options, index=time_options.index("09:00"), label_visibility="collapsed")

    # 照片上传组件（支持jpg/jpeg/png）
    st.markdown('### 上传个人照片')
    user_photo = st.file_uploader(
        label="",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed",
        help="Drag and drop file here\nLimit 200MB per file - JPG, JPEG, PNG"
    )


with c2:
    st.markdown('### 简历实时预览👁️‍🗨️ ')
    st.markdown('***')
    
    # 预览区分栏：左（基础信息+照片）、右（补充信息）
    preview_col1, preview_col2 = st.columns([2, 1])
    
    with preview_col1:
        # 照片预览逻辑：上传后压缩尺寸(120x120)并显示
        if user_photo:
            img = Image.open(user_photo)
            img.thumbnail((120, 120))  # 压缩图片避免过大
            buf = io.BytesIO()
            img.save(buf, format='PNG')
            st.image(buf, caption="个人照片", width=120)  
        
        # 姓名（二级标题）+ 基础信息（粗体标签）
        st.markdown(f'## {user_name if user_name else ""}')
        st.markdown(f'**职位**: {user_position if user_position else ""}')
        st.markdown(f'**电话**: {user_phone if user_phone else ""}')
        st.markdown(f'**邮箱**: {user_email if user_email else ""}')
        st.markdown(f'**出生日期**: {user_birth}')

        st.markdown('***')  
        
        # 个人简介+专业技能预览（无内容时显示默认提示）
        st.markdown('### 个人简介')
        st.markdown(user_intro if user_intro else "这个人很神秘，没有留下任何介绍...")

        st.markdown('### 专业技能')
        st.markdown(', '.join(user_skill) if user_skill else "暂无")

    with preview_col2:
        # 空行对齐姓名标题
        st.markdown('')
        st.markdown('')
        # 补充信息预览
        st.markdown(f'**性别**: {user_gender}')
        st.markdown(f'**学历**: {user_edu}')
        st.markdown(f'**工作经验**: {user_exp}年')
        st.markdown(f'**期望薪资**: {salary_range[0]}-{salary_range[1]}元')
        st.markdown(f'**最佳联系时间**: {user_contact}')
        st.markdown(f'**语言能力**: {", ".join(user_lang) if user_lang else ""}')
