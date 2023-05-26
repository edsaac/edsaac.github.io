import streamlit as st
import json
from typing import Union

st.set_page_config(
    page_title="Edwin site",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={"About": "Last updated: 03/13/2022"},
)


def generate_badge_table(badges: list):
    table_header = [f" {badge}" for badge in badges if badge is not None]

    table_markdown = f"""
    {"|".join(table_header)}
    | {":---:|" * len(table_header)}
    
    ****
    """

    return table_markdown


@st.cache_data
def generate_badge(kind: str, link: Union[str, bool]) -> Union[str, None]:
    if link:
        if kind == "Streamlit App":
            mkd = f"[![{kind}](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]({link})"
        elif kind == "Github Repo":
            mkd = f"[![{kind}](https://img.shields.io/static/v1?label=&message=Repository&color=black&logo=github)]({link})"
        elif kind == "Google Drive":
            mkd = f"[![{kind}](https://img.shields.io/static/v1?label=&message=Slides&color=black&logo=googledrive)]({link})"
        elif kind == "Google Scholar - Abstract":
            mkd = f"[![{kind}](https://img.shields.io/static/v1?label=&message=Abstract&color=black&logo=googlescholar)]({link})"
        elif kind == "Iposter":
            mkd = f"[![{kind}](https://img.shields.io/badge/🪧-Iposter-purple.svg)]({link})"
        elif kind == "Github Docs":
            mkd = f"[![{kind}](https://img.shields.io/static/v1?label=&message=Documentation&color=gray&logo=github)]({link})"
        elif kind == "Maintained":
            if link == "yes":
                mkd = f"![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)"
            else:
                mkd = f"![Maintenance](https://img.shields.io/badge/Maintained%3F-no-red.svg)"
        else:
            mkd = "<<Badge Missing>>"
        return mkd
    else:
        return None


@st.cache_data
def load_json() -> dict:
    with open("assets/datadisplay.json") as f:
        data = json.load(f)
    return data


# Add some styling with CSS selectors
with open("assets/style.css") as f:
    st.markdown(
        f"""
    <style>
        {f.read()}
    </style>
    """,
        unsafe_allow_html=True,
    )

"# Hello"
"******"
database = load_json()

# Layout
cols = st.columns([1, 2.5], gap="large")

with cols[0]:
    categories = database.keys()
    category = st.radio(
        "Select an option:", categories, 1, label_visibility="collapsed"
    )

    "******"
    """**Edwin Y. Saavedra Cifuentes** """
    """PhD.(c) - Northwestern University"""

    st.markdown(
        """[![Github](https://img.shields.io/static/v1?label=&message=%20Github&color=ff4b4b&logo=github)](https://github.com/edsaac/) [![Google Scholar](https://img.shields.io/static/v1?label=&message=%20Google%20Scholar&color=ff4b4b&logo=googlescholar)](https://scholar.google.com/citations?hl=en&user=th-VSYIAAAAJ&view_op=list_works&sortby=pubdate)"""
    )

with cols[1]:
    if category == "Conferences":
        data = database["Conferences"]

        for i, (k, row) in enumerate(data.items()):
            st.markdown(
                f"""
                ## {k.strip()}\n
                **{row['Name'].strip()}**"""
            )
            st.image(f"./assets/screenshots/{row['ImagePath']}", use_column_width=True)
            st.caption(f"{row['Title']}".strip())

            badges = [
                generate_badge("Google Scholar - Abstract", row["Abstract"]),
                generate_badge("Iposter", row["Iposter"]),
                generate_badge("Google Drive", row["GDocument"]),
            ]

            st.markdown(generate_badge_table(badges))

    elif category == "Classes & Labs":
        class_code = st.selectbox(
            "Select a course:", options=database["Classes & Labs"].keys(), index=1
        )

        "*****"
        # f"### {class_code}"
        data = database["Classes & Labs"][class_code]

        for i, (k, row) in enumerate(data.items()):
            st.markdown(
                f"""
                ## [{k.strip()}]({row['Streamlit']})\n
                **{row['Name'].strip()}**"""
            )
            if row["ImagePath"]:
                st.image(
                    f"./assets/screenshots/{row['ImagePath']}", use_column_width=True
                )
            st.caption(f"{row['Title']}".strip())

            badges = [
                generate_badge("Streamlit App", row["Streamlit"]),
                generate_badge("Github Repo", row["Repo"]),
            ]

            st.markdown(generate_badge_table(badges))

    elif category == "Repositories":
        data = database["Repositories"]

        for i, (k, row) in enumerate(data.items()):
            st.markdown(
                f"""
                ## [{k.strip()}]({row['Repo']})\n
                **{row['Name'].strip()}**"""
            )
            st.image(f"./assets/screenshots/{row['ImagePath']}", use_column_width=True)

            badges = [
                generate_badge("Github Docs", row["Documentation"]),
                generate_badge("Github Repo", row["Repo"]),
                generate_badge("Maintained", row["Maintained"]),
            ]

            st.markdown(generate_badge_table(badges))

    elif category == "Other":
        data = database["Other"]

        for i, (k, row) in enumerate(data.items()):
            st.markdown(
                f"""
                ## [{k.strip()}]({row['Repo']})\n
                **{row['Name'].strip()}**"""
            )
            st.image(f"./assets/screenshots/{row['ImagePath']}", use_column_width=True)

            badges = [
                generate_badge("Streamlit App", row["App"]),
                generate_badge("Github Repo", row["Repo"]),
                generate_badge("Maintained", row["Maintained"]),
            ]

            st.markdown(generate_badge_table(badges))
