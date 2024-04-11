import streamlit as st

def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# OpenAI 광고 카피 생성")
    st.write("# 서비스를 소개합니다 👋")
    st.markdown(
        """
        ## OpenAI 광고 카피 생성 서비스
        OpenAI 광고 카피 서비스는 OpenAI의 gpt-3.5-turbo 모델을 사용하여 구축한 AI 카피 생성 서비스입니다.
        제품명, 제품 특징, 브랜드 명, 원하는 톤앤매너 등을 선택하여 다양한 상황과 목적에 맞는 광고 카피를 생성할 수 있습니다.
        데모 버전을 이용해보세요!
        ## 서비스를 이용하고 싶으신가요?
        - 가장 먼저 [OpenAI API 키](https://platform.openai.com/api-keys)를 발급해주세요.
        - **👈 사이드바에서 데모를 클릭**하고, API 키를 입력해주세요.
        - 제품명, 필수 포함 키워드 등을 입력한 후, 광고 문구 생성을 클릭하면 카피가 생성됩니다!
    """
    )


if __name__ == "__main__":
    run()
