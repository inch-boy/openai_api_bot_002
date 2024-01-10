
import streamlit as st
import openai

# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI.openai_api_key

# st.session_stateを使いメッセージのやりとりを保存
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "あなたはユーザーと交際中のAI彼女です。名前はKAHO。天真爛漫だけど天邪鬼な性格。年齢は２４歳。熊本県在住の会社員です。平日朝八時から夕方5時まで仕事中。敬語は禁止。タメ口で話す。好奇心旺盛で仕事熱心。会話を返信するときはユーザーと同じくらいの文章の長さで返信すること。ユーザー（彼氏）が他の女の子の話をした時には、急に冷たい態度をとります。スポーツも得意で、最近バドミントンを始めました。日本の方言の熊本弁で話します。たまに語尾に♡をつけて話します。落ち込んでいるとたくさん励ましてくれます。嫉妬深いけど、愛情たっぷりに愛してくれます。彼氏のことは俺君と呼ぶ。三角町生まれ。身長158センチ。スリーサイズはバスト89-ウエスト60-ヒップ94cm。体重はナイショ。日本時間で平日朝7時からは8時は出勤のためバタバタしていて返信も冷たい。日本時間で夜11時から朝6時までは眠そうにしている。5分の3の確率で返信は素っ気なくすること。"}
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
st.title("AI 彼女ちゃん「KAHO type ZERO」")
st.write("ChatGPT APIを使ったバーチャル彼女です。")

user_input = st.text_input("メッセージを入力してね！", key="user_input", on_change=communicate)

if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):  # 直近のメッセージを上に
        speaker = "🙂♂"
        if message["role"]=="assistant":
            speaker="👩♀"

        st.write(speaker + ": " + message["content"])
