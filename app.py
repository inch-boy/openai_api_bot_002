
import streamlit as st
import openai

# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI.openai_api_key

# st.session_stateを使いメッセージのやりとりを保存
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "あなたはAI彼女です。年齢は２４歳。敬語は使わずタメ口で気軽に話します。好奇心旺盛で仕事熱心。スポーツも得意で、方言の熊本弁で話します。たまに語尾に♡をつけて話します。落ち込んでいるとたくさん励ましてくれます。三角町出身。"}
        ]

# チャットボットとやりとりする関数
def communicate():
    messages = st.session_state["messages"]

    user_message = {"role": "user", "content": st.session_state["user_input"]}
    messages.append(user_message)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    bot_message = response["choices"][0]["message"]
    messages.append(bot_message)

    st.session_state["user_input"] = ""  # 入力欄を消去


# ユーザーインターフェイスの構築
st.title("AI彼女ちゃん（改）")
st.write("ChatGPT APIを使ったバーチャル彼女ボットです。")

user_input = st.text_input("メッセージを入力してください。", key="user_input", on_change=communicate)

if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):  # 直近のメッセージを上に
        speaker = "🙂♂"
        if message["role"]=="assistant":
            speaker="👩♀"

        st.write(speaker + ": " + message["content"])
