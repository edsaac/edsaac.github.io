import streamlit as st
from dataclasses import dataclass

"# Hello"
"******"

# Add some styling with CSS selectors
st.markdown("""
    <style>
    img {
        border-radius: 10px;
        border: solid 1px #dadee8;
    }

    a[href] {
        text-decoration: none;
        color: #ff4b4b;
    }

    h1 {
        font-size: 5rem;
        text-align: center;
    }

    h2 {
        font-size: 1.5rem;
        text-align: center;
    }

    .stRadio {
        position: sticky;
        top: 0px;
        padding: 0px;
        font-size: 25px;
    }

    iframe {
        border-radius: 10px;
        border: solid 1px #dadee8;
    }
    </style>
    """, unsafe_allow_html=True)

categories = [
    "Conferences",
    "Labs",
    "Repositories",
    "Other stuff", 
    "Social"
]

cols = st.columns([1, 2.5])
with cols[0]:
    category = st.radio("Categories", categories)

with cols[1]:
    if category == "Conferences":

        st.markdown(
        """ 
        ## Conference Presentations:

        **Frontiers in Hydrology Meeting - 2022:**

        <a href="https://drive.google.com/file/d/1mWvkKyYLSsTlcwhARnBcJIzybApNEjBO/view?usp=sharing">
            <img alt="See Poster" src="https://img.shields.io/static/v1?label=&message=Check poster&color=black&logo=googledrive">
        </a>

        **AGU Fall Meeting - 2021:**
        
        <a href="https://ui.adsabs.harvard.edu/abs/2021AGUFM.H35A..08S/abstract">
            <img alt="See Abstract" src="https://img.shields.io/static/v1?label=&message=Check abstract&color=black&logo=googlescholar">
        </a>        
        <a href="https://docs.google.com/presentation/d/1Jar5ThSvhYYakgkJcQerM6tUsDkK27dI7FHSKAOGxEs/edit?usp=sharing">
            <img alt="See Poster" src="https://img.shields.io/static/v1?label=&message=Check e-poster&color=black&logo=googledrive">
        </a>

        <div class="GSlides">
        <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vRBti4D1lI79iBmhcXWaaz9kwt270yAzSmc8qmXTRIRJEK7Sy3Un84lnTJXDdUUQ-NALGBbByT3-oFX/embed?start=false&loop=true&delayms=60000" frameborder="0" width="400" height="300" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
        </div>


        **AGU Fall Meeting - 2020:**
        
        <a href="https://docs.google.com/presentation/d/1M4uneQHBRlifLg2tcduoXKDNR0qy_G_FC06FYR3oAU8/edit?usp=sharing">
            <img alt="See Poster" src="https://img.shields.io/static/v1?label=&message=Check e-poster&color=black&logo=googledrive">
        </a>
        <a href="https://ui.adsabs.harvard.edu/abs/2020AGUFMH112.0022S/abstract">
            <img alt="See Abstract" src="https://img.shields.io/static/v1?label=&message=Check abstract&color=black&logo=googlescholar">
        </a>
        """, unsafe_allow_html=True)

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
