from googleapiclient.discovery import build
from urllib.parse import urlparse, parse_qs
import csv
import pandas as pd
import streamlit as st


def get_channel_videos(api_key,channel_id):

    youtube = build("youtube", "v3", developerKey=api_key)

    # Get video details to obtain the channel ID
    # video_response = youtube.videos().list(
    #     part="snippet",
    #     id=video_id
    # ).execute()

    channel_id=channel_id
    # Extract channel ID from video details
    # channel_id = video_response["items"][0]["snippet"]["channelId"]

    # Get videos from the channel
    videos_response = youtube.search().list(
        part="id",
        channelId=channel_id,
        order="date",
        type="video",
        maxResults=50  # Adjust as needed
    ).execute()

    total_views = 0
    total_likes = 0

    video_data = []
    # Iterate through each video and fetch details
    for item in videos_response["items"]:
        video_id = item["id"]["videoId"]

        # Get video details
        video_response = youtube.videos().list(
            part="snippet,statistics",
            id=video_id
        ).execute()
        # Extract video details
        try:    video_details = video_response["items"][0]
        except: video_details=''
        try:
            video_views=int(video_details["statistics"]["viewCount"])
        except: video_views=''
        try:
            video_likes=int(video_details["statistics"]["likeCount"])
        except:video_likes=''   
        try:
            video_thumbnail=video_details["snippet"]["thumbnails"]['standard']['url']
        except:video_thumbnail='' 

        total_views += video_views
        total_likes += video_likes

        # Print video details if needed
        try: video_title = video_details["snippet"]["title"]
        except: video_title=''
        try: video_url = 'https://www.youtube.com/watch?v='+video_details["id"]
        except: video_url = ''

        video_data.append({'VideoDetails':video_details,'VideoTitle':video_title,'VideoUrl':video_url,'VideoLikes':video_likes,'VideoViews':video_views,'VideoThumbnail':video_thumbnail})
        df=pd.DataFrame(video_data)
        df.to_csv('videos.csv',index=False)



    # Print total views and likes for all videos
    channel_response = youtube.channels().list(
        part="snippet,statistics",
        id=channel_id
    ).execute()

    channel_data  = []
    # Print channel details
    channel_details = channel_response["items"][0]
    print("Channel Title:", channel_details["snippet"]["title"])
    print("Channel ID:", channel_details["id"])
    print("Subscriber Count:", channel_details["statistics"]["subscriberCount"])
    print("Total Views:", channel_details["statistics"]["viewCount"])
    print("Total Videos:", channel_details["statistics"]["videoCount"])
    print("Channel Description:", channel_details["snippet"]["description"])
    print("\nVideo Details:")

    print("Total Views for All Videos:", total_views)
    print("Total Likes for All Videos:", total_likes)

    try:channel_details = channel_response["items"][0]
    except: channel_details=''    
    try:channel_title = channel_details["snippet"]["title"]
    except: channel_title=''    
    try:channel_id=channel_details["id"]
    except: channel_id=''    
    try:subscribers=channel_details["statistics"]["subscriberCount"]
    except: subscribers=''    
    try:total_views=total_views
    except: total_views=''    
    try:total_likes
    except: total_likes=''    
    try:total_videos=channel_details["statistics"]["videoCount"]
    except: total_videos=''    
    try:description=channel_details["snippet"]["description"]
    except: description='' 

    channel_data.append({'ChannelDetails':channel_details,'ChannelTitle':channel_title,'ChannelID':channel_id,'Subscriber':subscribers,'ChannelLikes':total_likes,'ChannelViews':total_views,'ChannelVideos':total_videos,'ChannelDescription':description})
    df=pd.DataFrame(channel_data)
    df.to_csv('channel.csv',index=False)
if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual API key
    api_key = st.secrets['api_key']

    channel_id='UCpBY3tMPPVi7i0ZEwv-tsaA'
    # video_url = "https://www.youtube.com/watch?v=c_zywB_EPII"

    get_channel_videos(api_key, channel_id)