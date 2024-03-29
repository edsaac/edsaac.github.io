import streamlit as st
import json
from typing import Union

st.set_page_config(
    page_title="Edwin's site",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={"About": "Last updated: 05/26/2022"},
)


def generate_badge_table(badges: list):
    
    chain_badges = "&emsp;".join(list(filter(lambda x: x is not None, badges)))

    st.write(
        "<p align=\"center\">"
        f"{chain_badges}"
        "</p>", unsafe_allow_html=True         
    )
    
    "****"


@st.cache_data
def generate_badge(kind: str, link: Union[str, bool]) -> Union[str, None]:
    if link:
        if kind == "Streamlit App":
            mkd = f"<a href='{link}'><img src='https://static.streamlit.io/badges/streamlit_badge_black_white.svg' alt='Open in Streamlit Community Cloud'></a>"""
        elif kind == "Github Repo":
            mkd = f"<a href='{link}'><img src='https://img.shields.io/static/v1?label=&message=Repository&color=black&logo=github' alt='Show Github repository'></a>"""
        elif kind == "Google Drive":
            mkd = f"<a href='{link}'><img src='https://img.shields.io/static/v1?label=&message=Slides&color=black&logo=googledrive' alt='Slides in Google Drive'></a>"""
        elif kind == "Google Scholar - Abstract":
            mkd = f"<a href='{link}'><img src='https://img.shields.io/static/v1?label=&message=Abstract&color=black&logo=googlescholar' alt='Show in Google Scholar'></a>"""
        elif kind == "Iposter":
            mkd = f"<a href='{link}'><img src='https://img.shields.io/badge/🪧-Iposter-purple.svg' alt='Show Iposter'></a>"""
        elif kind == "Github Docs":
            mkd = f"<a href='{link}'><img src='https://img.shields.io/static/v1?label=&message=Documentation&color=gray&logo=github' alt='Show Documentation'></a>"""
        elif kind == "Maintained":
            if link == "yes":
                mkd = f"<img src='https://img.shields.io/badge/Maintained%3F-yes-green.svg' alt='It is currently maintained'>"""
            else:
                mkd = f"<img src='https://img.shields.io/badge/Maintained%3F-no-red.svg' alt='It is not maintained'>"""
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

# Get query params to personalize the landing page
query_params = st.experimental_get_query_params()
page = query_params.get("page", "classes")

"# Hello"
"******"
database = load_json()

# Layout
cols = st.columns([1, 2.5], gap="large")

with cols[0]:
    categories = database.keys()

    pgidx = 0

    match page[0]:
        case "conferences":
            pgidx = 0
        case "classes" | "labs":
            pgidx = 1
        case "repos":
            pgidx = 2
        case "other":
            pgidx = 3

    category = st.radio(
        "Select an option:", categories, pgidx, label_visibility="collapsed"
    )

    "******"
    """**Edwin Y. Saavedra Cifuentes** """
    """Ph.D.(c) - Northwestern University"""

    st.markdown(
        """[![Github](https://img.shields.io/static/v1?label=&message=%20Github&color=ff4b4b&logo=github)](https://github.com/edsaac/) [![ORCiD](https://img.shields.io/static/v1?label=&message=%20ORCiD&color=ff4b4b&logo=orcid)](https://orcid.org/0000-0003-1242-4815) [![Google Scholar](https://img.shields.io/static/v1?label=&message=%20Google%20Scholar&color=ff4b4b&logo=googlescholar)](https://scholar.google.com/citations?hl=en&user=th-VSYIAAAAJ&view_op=list_works&sortby=pubdate)"""
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

            generate_badge_table(badges)

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

            generate_badge_table(badges)

    elif category == "Repositories":
        data = database["Repositories"]

        for i, (k, row) in enumerate(data.items()):
            st.markdown(
                f"""
                ## [{k.strip()}]({row['Repo']})\n
                **{row['Name'].strip()}**"""
            )

            if row.get("Embed", None):
                st.markdown(
                    f"""
                    <iframe
                    src="{row['Embed']}"
                    height="400"
                    style="width:100%;border:none;"
                    ></iframe>
                    """, unsafe_allow_html=True
                )
            
            else: 
                st.image(f"./assets/screenshots/{row['ImagePath']}", use_column_width=True)

            badges = [
                generate_badge("Github Docs", row["Documentation"]),
                generate_badge("Github Repo", row["Repo"]),
                generate_badge("Maintained", row["Maintained"]),
            ]

            generate_badge_table(badges)
        
        

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

            generate_badge_table(badges)
