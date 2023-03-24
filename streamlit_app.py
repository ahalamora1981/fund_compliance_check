import streamlit as st
import openai
openai.api_key = st.secrets["OPENAI_API_KEY"]

def check(text_input, prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature = 0.2,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": text_input}
        ]
    )
    return response['choices'][0]['message']['content']

st.title("基金公司销售电话合规检查 with GPT3.5")

option = st.selectbox(
    "合规检查类型:",
    ("对话总结", "基金经理违规项", "改善建议")
)

text_input = st.text_input("输入要判断的文字：")

if st.button("提交", use_container_width=True):
    if option == "对话总结":
        prompt = "请给出文本总结，只总结，不要给出任何分析。"
    elif option == "基金经理违规项":
        prompt = "你是一个有20年合规经验的基金公司监察稽核人员，请根据文本说明该基金经理有哪些违规行为。"
    elif option == "改善建议":
        prompt = "你是一个有20年合规经验的基金公司监察稽核人员，请根据文本中基金经理的违规行为，给出改善建议。"
        
    response = check(text_input, prompt)

    st.write(response)
