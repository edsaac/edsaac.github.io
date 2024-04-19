import streamlit as st
import json
from typing import Union, Optional

st.set_page_config(
    page_title="Edwin's site",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={"About": "Last updated: 4/4/2024"},
)


def right_text(text: Optional[str]):
    if text:
        st.html(
            f"""
            <p style="text-align:right; line-height:0.1em; color:#cf409f;">
                <em>{text}</em>
            </p>
            """
        )


def generate_badge_table(badges: list):
    chain_badges = "&emsp;".join(list(filter(lambda x: x is not None, badges)))

    st.write('<p align="center">' f"{chain_badges}" "</p>", unsafe_allow_html=True)

    "****"


@st.cache_data
def generate_badge(kind: str, link: Union[str, bool]) -> Union[str, None]:
    if link:
        if kind == "Streamlit App":
            img_src = (
                "https://static.streamlit.io/badges/streamlit_badge_black_white.svg"
            )
            alt_txt = "Open in Streamlit Community Cloud"

        elif kind == "Github Repo":
            img_src = "https://img.shields.io/static/v1?label=&message=Repository&color=black&logo=github"
            alt_txt = "Show Github repository"

        elif kind == "Google Drive":
            img_src = "https://img.shields.io/static/v1?label=&message=Slides&color=black&logo=googledrive"
            alt_txt = "Slides in Google Drive"

        elif kind == "Google Scholar - Abstract":
            img_src = "https://img.shields.io/static/v1?label=&message=Abstract&color=black&logo=googlescholar"
            alt_txt = "Show in Google Scholar"

        elif kind == "Iposter":
            img_src = "https://img.shields.io/badge/🪧-Iposter-purple.svg"
            alt_txt = "Show Iposter"

        elif kind == "Github Docs":
            img_src = "https://img.shields.io/static/v1?label=&message=Documentation&color=gray&logo=github"
            alt_txt = "Show Documentation"

        elif kind == "Maintained":
            if link == "yes":
                img_src = "https://img.shields.io/badge/Maintained%3F-yes-green.svg"
                alt_txt = "It is currently maintained"

            else:
                img_src = "https://img.shields.io/badge/Maintained%3F-no-red.svg"
                alt_txt = "It is not maintained"

        else:
            raise Exception("Badge not found.")

        return f"<a href='{link}'><img src='{img_src}' alt='{alt_txt}'></a>"

    else:
        return None


@st.cache_data
def load_json() -> dict:
    with open("assets/datadisplay.json") as f:
        data = json.load(f)
    return data


def main():
    # Add some styling with CSS selectors
    with open("assets/style.css") as f:
        st.html(f"<style>{f.read()}</style>")

    # Get query params to personalize the landing page
    page = st.query_params.get("page", "conferences")

    st.title("Hello", anchor=False)

    database = load_json()

    # Layout
    cols = st.columns([1, 2.5], gap="large")

    with cols[0]:
        categories = database.keys()

        pgidx = 0

        match page:
            case "conferences":
                pgidx = 0
            case "classes" | "labs":
                pgidx = 1
            case "repos":
                pgidx = 2
            case "other":
                pgidx = 3

        category = st.session_state.get("category", "")

        "&nbsp;"
        with st.popover("☰", use_container_width=True):
            category = st.radio(
                "Explore other sections:",
                categories,
                index=pgidx,
                # label_visibility="collapsed",
                horizontal=False,
                key="category",
            )

        "*****"

        st.html(
            """
            <p style="text-align:center; line-height:1.2rem;">
                <b>Edwin Y. Saavedra Cifuentes</b>
            </p>
            <p style="text-align:center; font-size:0.8rem; line-height:0.9rem;">
                Ph.D.(c) - Civil & Environmental Engineering <br>
                Northwestern University
            </p>
            """
        )

        st.html(
            """
            <p style="text-align:center;">
            <a href="https://github.com/edsaac/">
                <img src="https://img.shields.io/static/v1?label=&message=%20Github&color=053957&logo=github" alt="Github homepage">
            </a>
            <a href="https://orcid.org/0000-0003-1242-4815">
                <img src="https://img.shields.io/static/v1?label=&message=%20ORCiD&color=a6a8ab&logo=orcid" alt="ORCiD page">
            </a>
            <a href="https://scholar.google.com/citations?hl=en&user=th-VSYIAAAAJ&view_op=list_works&sortby=pubdate">
                <img src="https://img.shields.io/static/v1?label=&message=%20Google%20Scholar&color=058657&logo=googlescholar" alt="Google Scholar page">
            </a>
            <a href="https://www.linkedin.com/in/edsaac/">
                <img src="https://img.shields.io/static/v1?label=&message=%20Linkedin&color=589acf&logo=github" alt="Linkedin page">
            </a>
            </p>
            """
        )

    with cols[1]:
        right_text(category)

        if category == "Conferences":
            data = database["Conferences"]

            for i, (k, row) in enumerate(data.items()):
                st.header(k.strip(), anchor=False)
                f"**{row['Name'].strip()}**" ""

                st.image(
                    f"./assets/screenshots/{row['ImagePath']}", use_column_width=True
                )
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
                st.header(f"[{k.strip()}]({row['Streamlit']})", anchor=False)
                st.markdown(f"**{row['Name'].strip()}**")

                if row["ImagePath"]:
                    st.image(
                        f"./assets/screenshots/{row['ImagePath']}",
                        use_column_width=True,
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
                st.header(f"[{k.strip()}]({row['Repo']})", anchor=False)
                st.markdown(f"**{row['Name'].strip()}**")

                if row.get("Embed", None):
                    st.components.v1.iframe(row["Embed"], height=400, scrolling=True)

                else:
                    st.image(
                        f"./assets/screenshots/{row['ImagePath']}",
                        use_column_width=True,
                    )

                badges = [
                    generate_badge("Github Docs", row["Documentation"]),
                    generate_badge("Github Repo", row["Repo"]),
                    generate_badge("Maintained", row["Maintained"]),
                ]

                generate_badge_table(badges)

        elif category == "Other":
            data = database["Other"]

            for i, (k, row) in enumerate(data.items()):
                st.header(f"[{k.strip()}]({row['Repo']})", anchor=False)
                st.markdown(f"**{row['Name'].strip()}**")

                st.image(
                    f"./assets/screenshots/{row['ImagePath']}", use_column_width=True
                )

                badges = [
                    generate_badge("Streamlit App", row["App"]),
                    generate_badge("Github Repo", row["Repo"]),
                    generate_badge("Maintained", row["Maintained"]),
                ]

                generate_badge_table(badges)


if __name__ == "__main__":
    print(st.header.__func__.__dict__)
    main()
