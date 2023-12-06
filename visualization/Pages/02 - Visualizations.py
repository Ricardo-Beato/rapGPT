import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import base64


st.set_page_config(page_title="RAP GPT", page_icon=":microphone:", layout="wide")

st.header("Along with the model I've also taken a look at some interesting facts from our rappers")
st.markdown("The choice for the rappers to fetch lyrics from was somewhat personal but mostly I've tried to get lyrics from artists featured in [Rolling Stone's 200 best rap albums of all time](https://www.rollingstone.com/music/music-lists/best-hip-hop-albums-1323916/). This is the final list I came up with (81 artists):")

# The list of rappers in my analysis:
st.code('artists_songs_metadata = ["2Pac", "21 Savage", "50 Cent", "A Tribe Called Quest", "A$AP Rocky", "Aesop Rock", "Atmosphere", "Azealia Banks", "Baby Keem", "Big Daddy Kane", "Big L", "Big Pun", "Big Sean", "Cardi B", "Chance the Rapper", "Chief Keef", "Childish Gambino", "Common", "Cordae", "Cypress Hill", "Danny Brown", "De La Soul", "DMX", "Doja Cat", "Dr_ Dre", "Drake", "Earl Sweatshirt", "Eminem", "Eric B & Rakim", "Future", "Ghostface Killah", "Gucci Mane", "Hopsin", "Ice Cube", "Ice Spice", "J. Cole", "Jack Harlow", "JAY_Z", "Jeezy", "Joey Bada$$ ", "Joyner Lucas", "Juice WRLD", "Kanye West", "Kendrick Lamar", "Kid Cudi", "KMD", "Lauryn Hill", "Lil Nas X", "Lil Uzi Vert", "Lil Wayne", "Lil Yachty", "Lil_ Kim", "Logic", "Lupe Fiasco", "Mac Miller", "Masta Ace", "Megan Thee Stallion", "MF DOOM", "Migos", "Missy Elliott", "Mobb Deep", "Nas", "Nipsey Hussle", "OutKast", "Playboi Carti", "Pop Smoke", "Public Enemy", "Pusha T", "Queen Latifah", "Run_DMC", "Scarface", "Slick Rick", "Snoop Dogg", "Talib Kweli", "The Notorious B.I.G.", "The Pharcyde", "Travis Scott", "Vince Staples", "Wu_Tang Clan", "Yasiin Bey", "Young Thug"]')

# Everyone should insert their code of Tableau in here to make it Unique! The tableau Temp should be inside a main function:
st.title ("Rap vocabulary analysis")
st.markdown("*With Tableau*")
def main():
    html_temp = '''<div class='tableauPlaceholder' id='viz1701864972721' style='position: relative; overflow-x: auto;'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ra&#47;Rapanalysis&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Rapanalysis&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ra&#47;Rapanalysis&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div> <script type='text/javascript'> var divElement = document.getElementById('viz1701864972721'); var vizElement = divElement.getElementsByTagName('object')[0]; if ( divElement.offsetWidth > 800 ) { vizElement.style.width='3000px';vizElement.style.minHeight='827px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='3200px';vizElement.style.minHeight='827px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='2727px';} var scriptElement = document.createElement('script'); scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js'; vizElement.parentNode.insertBefore(scriptElement, vizElement); </script>'''
    components.html(html_temp, width=9000, height=1000)


if __name__ == '__main__':
    main()

#Easy. You only have to replicate this code changing the HTML_TEMP that will appear in your Tableau Public (careful, NOT Tableau Desktop). The Tableau will be then interactive for the user. 









st.caption("_(...) I was in a dark room, loud tunes, lookin' to make a vow soon / That I'ma get f*cked up, fillin' up my cup I see the crowd mood / Changin' by the minute and the record on repeat / Took a sip, then another sip, then somebody said to me (...)_")


