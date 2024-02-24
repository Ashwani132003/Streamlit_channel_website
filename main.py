import streamlit as st
import pandas as pd
from youtube_scrape import get_channel_videos


youtube_api_key = st.secrets['api_key']
channel_id='UCpBY3tMPPVi7i0ZEwv-tsaA'

get_channel_videos(api_key=youtube_api_key,channel_id=channel_id)

def add_style():
    """
    Adds style so link are not blue
    """
    # Define style
    style = """
    a:link {
    color: inherit;
    text-decoration: none;
    }

    a:visited {
    color: inherit;
    text-decoration: none;
    }

    a:hover {
    color: red;
    text-decoration: underline;
    }

    a:active {
    color: red;
    text-decoration: underline;
    }
    """
    my_html = f"""
                <style>
                {style} 
                </style>
                """

    # Execute your app
    st.components.v1.html(my_html, height=0, width=0)

def add_color_to_top_cards():
    """
    Adds color to the expanders.
    Users don't need to call this function, is executed by default.
    """
    # Define your javascript
    # classname = classname
    my_js = """
    var cards = window.parent.document.getElementsByClassName('st-emotion-cache-v84420 e1f1d6gn3');
    for (var i = 0; i < cards.length; i++) {
        let card = cards[i];
        // See if there's content in the card
        N_chars_in_cards = String(card.firstChild.innerHTML).length;
        if (N_chars_in_cards >100){
            card.style.border = "solid";
            card.style.borderColor = "#E4F6F8";
            card.style.borderWidth = "2px";
            card.style.padding = "10px";
            card.style.borderRadius = "10px";
            card.style.borderRadius = "10px";
            card.addEventListener("mouseover", function(event){card.style.borderColor = "red"})
            card.addEventListener("mouseout",  function(event){card.style.borderColor = "#E4F6F8"})
        }
    }    
    """
        # Wrapt the javascript as html code
    my_html = f"""
                <script>
                {my_js}
                </script>
                """
    # Execute your app
    st.components.v1.html(my_html, height=0, width=0)

    return
def add_color_to_cards():
    """
    Adds color to the expanders.
    Users don't need to call this function, is executed by default.
    """
    # Define your javascript
    # classname = classname
    my_js = """
    var cards = window.parent.document.getElementsByClassName('st-emotion-cache-tcjedx e1f1d6gn3');
    for (var i = 0; i < cards.length; i++) {
        let card = cards[i];
        // See if there's content in the card
        N_chars_in_cards = String(card.firstChild.innerHTML).length;
        if (N_chars_in_cards >100){
            card.style.border = "solid";
            card.style.borderColor = "#E4F6F8";
            card.style.borderWidth = "2px";
            card.style.padding = "10px";
            card.style.borderRadius = "10px";
            card.style.borderRadius = "10px";
            card.addEventListener("mouseover", function(event){card.style.borderColor = "red"})
            card.addEventListener("mouseout",  function(event){card.style.borderColor = "#E4F6F8"})
        }
    }    
    """
    # Wrapt the javascript as html code
    my_html = f"""
                <script>
                {my_js}
                </script>
                """
    # Execute your app
    st.components.v1.html(my_html, height=0, width=0)

    return

df = pd.read_csv('videos.csv')
cdf = pd.read_csv('channel.csv')

st.set_page_config(layout="wide")


st.subheader(cdf['ChannelTitle'][0])
st.write(cdf['ChannelDescription'][0])

c0,c1,c2,c3=st.columns([0.5, 0.5,0.5,0.5],gap='large')
c0.write('Subscribers: '+str(cdf['Subscriber'][0]))
c1.write('Total Videos: '+str(cdf['ChannelVideos'][0]))
c2.write('Total Likes: '+str(cdf['ChannelLikes'][0]))
c3.write('Total Views: '+str(cdf['ChannelViews'][0]))
add_color_to_top_cards()

n_cards = 3
# total_videos = 30
total_videos = len(df['VideoUrl'])
# if 
for i in range(total_videos):
    # with st.container():
    #     clickable_image = f'<a href="{df["VideoUrl"][i]}" target="_blank"><img src="{df["VideoThumbnail"][i]}" style="width: 640;height: 480"></a>'

    #     st.markdown(clickable_image, unsafe_allow_html=True)
    #     # st.write(f"https://www.youtube.com/watch?v={df['VideoUrl'][i]}")
    #     st.write(df['VideoTitle'][i])    
    #     col1,col2=st.columns(2)
    #     col1.markdown('Views: '+ str(df['VideoViews'][i]))
    #     col2.markdown('Likes: '+str(df['VideoLikes'][i]))
    row_card = i%n_cards
    if row_card==0:
        cols=st.columns(n_cards,gap="medium")
    with cols[i%n_cards]:
        # st.write('Card')
        # st.image(f"https://www.youtube.com/watch?v={df['VideoID'][i]}")
        clickable_image = f'<a href="{df["VideoUrl"][i]}" target="_blank"><img src="{df["VideoThumbnail"][i]}" style="width:100%;"></a>'

        st.markdown(clickable_image, unsafe_allow_html=True)
        # st.write(f"https://www.youtube.com/watch?v={df['VideoUrl'][i]}")
        st.title(df['VideoTitle'][i])    
        col1,col2=st.columns(2)
        col1.markdown('Views: '+ str(df['VideoViews'][i]))
        col2.markdown('Likes: '+str(df['VideoLikes'][i]))

    add_style()
    add_color_to_cards()    