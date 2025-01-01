import streamlit as st
import requests
from bs4 import BeautifulSoup
import jieba
from collections import Counter


def get_text_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text()
    except requests.exceptions.RequestException as e:
        st.error(f"请求 URL 时出错: {e}")
        return ""


def analyze_word_frequency(text):
    words = jieba.lcut(text)
    word_freq = Counter(words)
    return word_freq


def main():
    st.title("网页文本词频分析")

    url = st.text_input("请输入网页 URL")
    if url:
        text = get_text_from_url(url)
        if text:
            word_freq = analyze_word_frequency(text)
            st.subheader("词频分析结果")
            top_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:10]
            for word, count in top_words:
                st.write(f"{word}: {count}")


if __name__ == "__main__":
    main()