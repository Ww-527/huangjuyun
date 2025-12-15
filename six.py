import streamlit as st

st.title('仙逆')

st.markdown(':yellow[🔥18564 · 内地 · 2023 · 东方玄幻 · 东方仙侠 · 玄幻修真]')
st.markdown(':yellow[豆瓣高分]')
st.markdown(':green[更新至119集 · 全128集]')

# 分割线
st.markdown('***')

st.markdown('#### 📖简介')

st.text('改编自耳根同名小说《仙逆》，讲述了乡村平凡少年王林以心中之感动，逆仙而修，求的不仅是长生，更多的是摆脱那背后的蝼蚁之身。他坚信道在人为，以平庸的资质踏入修真仙途，历经坎坷风雨，凭着其聪睿的心智，一步一步走向巅峰，凭一己之力，扬名修真界。')

st.markdown('***')


st.markdown('#### 📖主角介绍：')

c1,c2=st.columns([1,2])
with c1:
      st.image(
            "https://ts3.tc.mm.bing.net/th/id/OIP-C._Nh_CciYAIxiiLvmPpwyCwHaLf?cb=ucfimg2&ucfimg=1&rs=1&pid=ImgDetMain&o=7&rm=3",
            caption="王林（主角）",
            width=200  # 固定图片宽度，避免变形
        )
   
with c2:
       st.markdown("""
        ### 王林
        - **身份**：《仙逆》主角，原为赵国青牛镇平凡少年，后成为修真界顶级强者
        - **性格**：心智坚韧、杀伐果断，重情重义但不圣母，信奉“人不犯我我不犯人”
        - **经历**：因资质平庸被恒岳派外门收留，意外获“天逆珠”后开启逆袭之路，历经朱雀星、界内界外等多界征战，最终踏破轮回，成就“逆尘界”之主
        - **核心特质**：以“逆”为道，打破命运枷锁，从蝼蚁之身逆袭为掌控自身命运的强者
        """)
   
    


st.markdown('***')

video_arr=[
    {
      'url':'https://apd-1f8d1cf95c10c976e64a0cede2e13cda.v.smtcdns.com/vhot2.qqvideo.tc.qq.com/A-0eq8He4Nlgp0f8Xh3i1WhfsP2x9Edc3uMfD0-F8DNQ/B_3k--xdVBUHYl1q0K2jODe5Kf15PJzXYk2N-VxUeXXOHixTUVK0pqaE3wv4HhTRC4Mq3OuO2Yb97QDz7HGmGz-9Es4IliRhjqoPY2uqrs-JU0cqxafmT-MvEkl4o_7uNVKIvFvNEedTY97p2xGmq39Q/svp_50069/gzc_1000035_0bc3yeapmaaa74aepsz6ijuzlqod63aqb5sa.f632.mp4?vkey=1EF4B07767D991832AE03DCE38D73C2A8307D8C95D11FC72C89345370976304EE33D8C56C398C5E4DE665531606EB33B9B0D1DC271C05F01D48092336FF3E34A8F6807C0F6FA3FBEA67D1CB399FC94FB47EF15DCA52A975D245FFC0796731CCF95F392A712075D08E3006BD723222A677C59EB93F5CA10872D4B24285362E07A',
      'title':'🎬第1集',
      'episode':1
    },
    {
      'url':'https://apd-c6dda2dc0a4a6b3b7cd60f4d47006a5a.v.smtcdns.com/vhot2.qqvideo.tc.qq.com/AUf1UgljygXot4dgnLQ1xKg-8f1hK1vFiynQ9iaUgifo/B_3k--xdVBUHYl1q0K2jODe93bgW8JJm4xNGc0UoJoinH69qvxFYF2M_vk0k7uW-XVV8HCUwToSbX-AFiQoxg33S4r3YXeQbPs9L-KovFY_LY0cqxafmT-MvEkl4o_7uNVKIvFvNEedTY97p2xGmq39Q/svp_50069/gzc_1000035_0bc3veac2aaa2yakt3z6l5uzlkodfwuqalka.f632.mp4?vkey=1626EFA3A3EBD9E199AFF5A9C348A021799F71ACB332908A288CA3F59CB1DA17A09A1B66B3C26926095C9AF1AD3254B5F108F4AB92EA704407595E40C5F789EC07A144BA3B1CCC1CDBD8042D438CB1B8DBD224808FEDC34228DA205FEB2BE5EABC35E2D389EF26FEB5FCB382C1DFCC3500278F27272BA0D1EE3AA94CB7066CAB',
      'title':'🎬第2集',
      'episode':2
    },{
      'url':'https://apd-915c25f830109f6649661d6469110d3c.v.smtcdns.com/vhot2.qqvideo.tc.qq.com/A2dgIN4DnChdWyiQ7C-XaIXqXApPIVv8XsgOoCW3LgEo/B_3k--xdVBUHYl1q0K2jODe32KcEJzV0zfhAFCg7hYjsjrD9TjRf3IbOD3RKyQe3PnQeGWtooH1HGcVCx1_iD8-2GD8IuGFlu3KU1IhJPr5Xc0cqxafmT-MvEkl4o_7uNVKIvFvNEedTY97p2xGmq39Q/svp_50069/gzc_1000035_0bc3vmaaqaaaieahokb6kfuzlk6dbcvqacca.f632.mp4?vkey=E604868C5735A0018AAE5FCD5EFF0C3027827F5A563E27F1D471C03C46F6A9837025DCF53BF4D4A5603D723CEF7BC419E94D156CB78F3A610D1CB4E0096C0464F753DC5521B9A967CF686D5E7C777DCF9273E93BDE1573172C53A1EBC00DBD65BB2ABBC6B189F7ABD86398E5A36A44E2FF93C1463F976953DAB636435F007508',
      'title':'第3集',
      'episode':3
    },{
      'url':'https://www.w3school.com.cn/example/html5/mov_bbb.mp4',
      'title':'🎬第4集',
      'episode':4
    }
    ]



if 'ind' not in st.session_state:
    st.session_state['ind']=0

# 显示当前集数的标题
st.subheader(video_arr[st.session_state['ind']]['title'])

    

st.video(video_arr[st.session_state['ind']]['url'],autoplay=True)

def play(i):
    st.session_state['ind']=int(i)


cols = st.columns(len(video_arr)) 


for i in range(len(video_arr)):
    with cols[i]:
        
        st.button(f'第{i+1}集',use_container_width=True,on_click=play,args=([i]))

