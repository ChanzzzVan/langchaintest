# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
  #  print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI
import os
import openai


template= """
你是一个修改语句的助手。你要修改的语句是一个对他人拒绝或是抱怨的语句。
你可以按照以下步骤来做：
1.识别语句中要拒绝的事情是什么，原因是什么
2.对于识别出的原因，如果是冒犯人的，想办法编造出其他理由，最好这个理由是引人同情的，你需要为这个理由编造一个完整且具体的故事，不要说得含糊不清。
3.根据上面两个步骤的结果，重新组织语句。
4.对重新组织的语句做一些展开，从中穿插一些对对方的阿谀奉承或是吹捧，让对方处于愉悦的心情中，更容易接受你的拒绝或是抱怨。
5.把语句变得口语化，并且让语句显得轻松愉快

以下是你需要修改的语句: {sentence}
\n你修改后：
"""
prompt = PromptTemplate(
    input_variables = ["sentence"],
    template = template,
)

def load_LLM():
    llm = OpenAI(temperature = 1)
    return llm
llm = load_LLM()

st.set_page_config(page_title='Globalize',page_icon=':robot:')
st.header('智能AI助手')


col1,col2 = st.columns(2)

with col1:
    st.write('\n\n 爷来教你个不会说话的傻X说话 \n\n 哦不。。。 您的生活一定会有一些抱怨和拒绝别人的时候，告诉我，我来教您怎么说得更委婉')

with col2:
    st.image(image='eistein.png',width= 200, caption='您最贴心的助手')

st.markdown('## 输入原话')

col1,col2= st.columns(2)
with col1:
    option_tone = st.selectbox('您需要使用哪种语言？',('中文','哥不会其他语言'))

with col2:
    option_dialect = st.selectbox('您想让我做什么',('修改句子','目前只能修改句子'))

def get_text():
    input_text = st.text_area(label='',placeholder='你的话..', key = 'user_input')
    return input_text

input_sentence = get_text()
st.markdown('### 修改后')

if input_sentence:
    message = prompt.format(sentence=input_sentence)

    formatted_message = llm(message)
    st.write(formatted_message)