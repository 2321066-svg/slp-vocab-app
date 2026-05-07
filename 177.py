import streamlit as st

# 1. 앱 페이지 설정
st.set_page_config(page_title="꼬마 사전", page_icon="🐥")

# 2. 스타일링 (아이들이 좋아할 만한 귀여운 느낌)
st.markdown("""
    <style>
    .main { background-color: #f0f8ff; }
    .stButton>button { background-color: #ffcc00; border-radius: 20px; font-weight: bold; }
    .title { color: #ff6600; text-align: center; font-family: 'Nanum Gothic', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='title'>🐥 꼬마 지식인: 단어 사전</h1>", unsafe_allow_html=True)
st.write("---")

# 3. 임시 단어 데이터베이스 (예시)
# 실무에서는 여기서 LLM(GPT)을 호출하여 동적으로 설명을 생성하는 것이 좋습니다.
word_db = {
    "배려": {
        "easy": "내 마음보다 다른 사람의 기분을 먼저 생각해주고 도와주는 예쁜 마음이에요.",
        "example": "비가 올 때 친구에게 우산을 씌워주는 건 정말 멋진 배려예요!",
        "tag": "❤️ 마음"
    },
    "경제": {
        "easy": "우리가 물건을 만들고, 사고팔고, 돈을 사용하는 모든 활동을 말해요.",
        "example": "용돈을 모아서 사고 싶은 장난감을 사는 것도 경제 활동 중 하나예요.",
        "tag": "💰 생활"
    },
    "협력": {
        "easy": "혼자 하기 힘든 일을 여러 친구와 힘을 합쳐서 완성하는 거예요.",
        "example": "커다란 레고 성을 친구들과 같이 만드는 것이 바로 협력이에요.",
        "tag": "🤝 함께"
    }
}

# 4. 메인 화면 구성
st.subheader("궁금한 단어를 입력해봐요!")
target_word = st.text_input("어떤 단어가 궁금한가요?", placeholder="예: 배려, 경제, 협력")

if st.button("설명해줘!"):
    if target_word in word_db:
        data = word_db[target_word]
        
        # 결과 출력 공간
        st.success(f"### 🔍 {target_word} (이/가) 무슨 뜻인가요?")
        
        col1, col2 = st.columns([1, 3])
        with col1:
            st.info(data['tag'])
        
        st.write(f"**아이 눈높이 설명:**")
        st.info(data['easy'])
        
        st.write(f"**이렇게 사용해요! (예시):**")
        st.warning(data['example'])
        
        st.balloons() # 축하 효과
    else:
        if target_word == "":
            st.error("단어를 입력해주세요!")
        else:
            st.error("앗! 아직 사전에 없는 단어예요. 선생님께 물어볼게요!")
            st.write(f"💡 **'{target_word}'**를 쉽게 설명하려면 GPT와 같은 AI 연동이 필요합니다.")

# 5. 하단 안내
st.sidebar.title("💡 사용 팁")
st.sidebar.info("""
- 단어를 입력하고 버튼을 누르세요.
- 어려운 단어도 친구처럼 설명해줄게요.
- 데이터베이스에 없는 단어는 AI API를 연결해 확장해보세요!
""")
