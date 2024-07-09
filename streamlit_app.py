import streamlit as st
import re
from typing import List
from collections import Counter
from math import log
import textstat
import tiktoken
text = st.text_area("text")
calculate = st.button("Calculate")

encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

def shannon(string):
    counts = Counter(string)
    frequencies = ((i / len(string)) for i in counts.values())
    return - sum(f * log(f, 2) for f in frequencies)



if calculate:
    st.text(f"Shannon entropy: {shannon(text):.2f}")
    st.text(f"Gunning fox index: {textstat.gunning_fog(text)}")
    st.text(f"No of tokens: {len(encoding.encode(text))}")
