import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Edwin site",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'About': "Las updated: 10/14/2022"
    }
)

@st.cache
def generate_badge(kind:str, link:str) -> str:
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
    elif kind == "Maintained?":
        if link.lower() == "no":
            mkd = f"[![Maintenance](https://img.shields.io/badge/Maintained%3F-no-red.svg)]({link})"
        else:
            mkd = f"[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)]({link})"
    else:
        mkd = "<<Badge Missing>>"
    return mkd

@st.cache
def load_dataframe(sheet:str):
    df = pd.read_excel("./assets/database.xlsx", sheet_name=sheet)
    return df

# Add some styling with CSS selectors
with open("assets/style.css") as f:
    st.markdown(f"""
    <style>
        {f.read()}
    </style>
    """, unsafe_allow_html=True)

"# Hello"
"******"

# Layout
cols = st.columns([1, 2.5], gap="large")

with cols[0]:

    categories = ["Conferences", "Laboratories", "Repositories"]
    category = st.radio("Select an option:", categories, 1)

    "******"
    """**Edwin Y. Saavedra Cifuentes** """
    """PhD.(c) - Northwestern University"""

    st.markdown("""[![Github](https://img.shields.io/static/v1?label=&message=%20Github&color=ff4b4b&logo=github)](https://github.com/edsaac/) [![Google Scholar](https://img.shields.io/static/v1?label=&message=%20Google%20Scholar&color=ff4b4b&logo=googlescholar)](https://scholar.google.com/citations?hl=en&user=th-VSYIAAAAJ&view_op=list_works&sortby=pubdate)""")
    
    # # define what option labels and icons to display
    # option_data = [
    # {'icon': "💬", 'label':"Conferences"},
    # {'icon':"🔬",'label':"Laboratories"},
    # {'icon': "🗃️", 'label':"Repositories"}
    # ]

    # # Nav bar theme
    # over_theme = {
    #     'txc_inactive': 'gray',
    #     'menu_background':'rgb(255, 75, 75, 0.1)',
    #     'txc_active':'white',
    #     'option_active':'rgb(255, 75, 75, 0.5)'}

    # font_fmt = {'font-size':'150%', 'font-family':'"Source Sans Pro", sans-serif'}

    # # Choosing menu
    # category = sthc.option_bar(
    #     option_definition=option_data,
    #     title=None,
    #     key='PrimaryOption',
    #     font_styling=font_fmt,
    #     override_theme=over_theme,
    #     horizontal_orientation=False)

with cols[1]:
    if category == "Conferences":

        database = load_dataframe(category)
        for i, row in database.iterrows():
            st.markdown(f"""
                ## {row['Short'].strip()}\n
                **{row['Name'].strip()}**""")
            st.image(f"./assets/screenshots/{row['ImagePath']}", use_column_width=True)
            st.caption(f"{row['Title']}".strip())
            
            badges = [
                generate_badge("Google Scholar - Abstract", row['Abstract']),
                generate_badge("Iposter", row['Iposter']),
                generate_badge("Google Drive", row['Gdoc'])
            ]

            st.markdown(f"""
            | {badges[0]} | {badges[1]} | {badges[2]} |
            |:----:|:-----:|:----------:|
            
            ****

            """)

    if category == "Laboratories":
        database = load_dataframe(category)
        
        for i, row in database.iterrows():
            st.markdown(f"""
                ## [{row['Short'].strip()}]({row['Streamlit']})\n
                **{row['Name'].strip()}**""")
            st.image(f"./assets/screenshots/{row['ImagePath']}", use_column_width=True)
            st.caption(f"{row['Title']}".strip())
            
            badges = [
                generate_badge("Streamlit App", row['Streamlit']),
                generate_badge("Github Repo", row['Github'])
            ]

            st.markdown(f"""
            | {badges[0]} | {badges[1]} |
            |:----:|:-----:|
            
            ****

            """)

    if category == "Repositories":
        database = load_dataframe(category)
        
        for i, row in database.iterrows():
            st.markdown(f"""
                ## [{row['Short'].strip()}]({row['Github']})\n
                **{row['Name'].strip()}**""")
            st.image(f"./assets/screenshots/{row['ImagePath']}", use_column_width=True)
            #st.caption(f"{row['Title']}".strip())
            
            badges = [
                generate_badge("Github Docs", row['Documentation']),
                generate_badge("Github Repo", row['Github']),
                generate_badge("Maintained?", row['Maintained'])
            ]

            st.markdown(f"""
            | {badges[0]} | {badges[1]} | {badges[2]} |
            |:----:|:-----:|:-----:|
            
            ****

            """)
        

# <h2>CEE440 Labs:</h2>

# <p>See class description <a href="https://www.mccormick.northwestern.edu/civil-environmental/academics/courses/descriptions/440.html">[🔗]</a></p>

# <h3>CEE440 - Laboratory 1: Turbulence & signal processing </h3> 

#   <ul>
#     <li> <a href="https://edsaac-adv-processing--cee440-lab1-haq37n.streamlitapp.com">
#       <img alt="Streamlit Cloud" src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg">
#     </a></li>
#     <li> 
#       <a href="https://github.com/edsaac/ADV-processing.git">
#         <img alt="Github Repo" src="https://img.shields.io/static/v1?label=&message=Check repository&color=black&logo=github">
#       </a></li>
#   </ul>

# <h3>CEE440 - Laboratory 2: Bed sediment transport & image processing </h3>  

# <ul>
#   <li> <a href="https://edsaac-bedform-migration--cee440-lab2-l807qm.streamlitapp.com">
#     <img alt="Streamlit Cloud" src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg">
#   </a></li>
#   <li> 
#     <a href="https://github.com/edsaac/bedform-migration.git">
#       <img alt="Github Repo" src="https://img.shields.io/static/v1?label=&message=Check repository&color=black&logo=github">
#     </a></li>
# </ul>

# <p>_____________________________________</p>

# <h2>PFLOTRAN + bioparticle:</h2>

# <p>
#   <img alt="Not currently mantained" src="https://img.shields.io/badge/Maintained%3F-no-red.svg">
# </p>

# <ul>
#   <li> <a href="https://edsaac.github.io/bioparticle/">
#     <img alt="Streamlit Cloud" src="https://img.shields.io/static/v1?label=&message=Check web page&color=black&logo=githubpages">
#   </a></li>
#   <li> 
#     <a href="">
#       <img alt="Bitbucket Repo" src="https://img.shields.io/static/v1?label=&message=Check repository&color=black&logo=bitbucket">
#     </a></li>
# </ul>

# <p>_____________________________________</p>

# <h2>Other stuff:</h2>
# <p><strong>Box Models & Widgets:</strong> <a href="https://mybinder.org/v2/gh/edsaac/LinearBoxModels/master?urlpath=voila%2Frender%2FSaavedraC_hw3.ipynb"><img alt="Voila Binder" src="https://mybinder.org/badge_logo.svg"></a></p>
# <p><strong>Interactive Chemostats:</strong> <a href="https://github.com/edsaac/dashboards"><img alt="Github Repo" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"></a></p>

# <p>_____________________________________</p>

# <p><strong>Sites:</strong>
# <p><strong>Github:</strong> <a href="https://edsaac.github.io/">[Link]</a></p>
# <p><strong>Google:</strong> <a href="https://scholar.google.com/citations?hl=en&user=th-VSYIAAAAJ&view_op=list_works&sortby=pubdate">[Link]</a></p>

# <p>_____________________________________</p>

# <p><a href="https://www.overleaf.com?r=8bbb1cd2&rm=d&rs=b">Online LaTeX Editor Overleaf</a></strong></p>
# """, unsafe_allow_html= True)
