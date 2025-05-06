import streamlit as st
from streamlit.components.v1 import iframe

st.set_page_config(
    page_title="> edsaac.me",
    page_icon="🎀",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={"About": "Last updated: 5/6/2025"},
)

st.html("assets/style.css")


@st.dialog("Hello!", width="small")
def warn_moved():
    st.info("**:blue[This site has moved to https://edsaac.me !]**", icon="🧹")
    st.image("https://placecats.com/neo_banana/300/200", caption="Not a cat", use_container_width=True)
    st.link_button(
        "**:rainbow-background[https://edsaac.me]**",
        "https://edsaac.me",
        help="Go to new site!",
        icon="🔗",
        use_container_width=True,
        type="primary",
    )


warn_moved()
cols = st.columns([0.25, 1], vertical_alignment="center")
with cols[0]:
    st.link_button(
        "**:rainbow-background[https://edsaac.me]**",
        "https://edsaac.me",
        help="Go to new site!",
        icon="🔗",
        use_container_width=True,
        type="primary",
    )

with cols[1]:
    iframe("https://edsaac.me", height=800, scrolling=True)
