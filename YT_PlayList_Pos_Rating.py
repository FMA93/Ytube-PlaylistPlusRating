import pandas as pd
from pytube import Playlist
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

# Here you need to fill in your API Key after you've enabled Youtube Data to your Google Cloud Console Project
# YouTube Data API credentials (obtained from Google Cloud Console, have ot create a free dev account)
API_KEY = "Your_API_Key"  # Replace with your API key

# Here you need to paste the playlist URL you wish to use
# URL of the YouTube playlist
playlist_url = "Insert_Your_Desired_YTPlaylist_URL"

# Initialize a playlist object
playlist = Playlist(playlist_url)

# Create a YouTube Data API client
youtube = build("youtube", "v3", developerKey=API_KEY)

# Create an empty list to store dictionaries of video details
video_details = []

# Function to fetch video details from the YouTube Data API
def fetch_video_details(video_id):
    response = youtube.videos().list(
        part="snippet,statistics",
        id=video_id
    ).execute()
    item = response.get("items", [])[0]
    if item:
        snippet = item["snippet"]
        statistics = item["statistics"]
        title = snippet["title"]
        author = snippet["channelTitle"]
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        views = int(statistics.get("viewCount", 0))
        likes = int(statistics.get("likeCount", 0))
        posting_date = snippet["publishedAt"]
        return title, author, video_url, views, likes, posting_date
    return None, None, None, None, None, None

# Loop through the videos in the playlist
for video in playlist.videos:
    # Extract video details using pytube
    video_id = video.watch_url.split("v=")[1]
    title, author, video_url, views, likes, posting_date = fetch_video_details(video_id)
    
    if title:
        # Calculate the positivity rate as a percentage and format it
        positivity_rate = "{:.2f} %".format((likes / views) * 100) if views > 0 else "0.00 %"
        
        # Split the "Posting Date" column into separate "Date" and "Time" columns
        posting_date_parts = posting_date.split("T")
        date_parts = posting_date_parts[0].split("-")
        date_formatted = f"{date_parts[2]}-{date_parts[1]}-{date_parts[0]}"
        time_parts = posting_date_parts[1].split(":")
        time_formatted = f"{time_parts[0]}:{time_parts[1]}"
        
        # Append the details to the list
        video_details.append({"Title": title, "Author": author, "Video URL": video_url, "Views": views, 
                              "Likes": likes, "Date": date_formatted, "Time": time_formatted, 
                              "Positivity Rate": positivity_rate})

# Create a DataFrame from the list of video details
df = pd.concat([pd.DataFrame([detail]) for detail in video_details], ignore_index=True)

# Reorder the columns to position the "Positivity Rate" column after "Likes"
df = df[["Title", "Author", "Video URL", "Views", "Likes", "Date", "Time", "Positivity Rate"]]

# Sort the DataFrame by Positivity Rate in descending order
df["Positivity Rate"] = df["Positivity Rate"].str.replace(" %", "").astype(float)  # Convert to numeric for sorting
df = df.sort_values(by="Positivity Rate", ascending=False)

# Format the "Positivity Rate" column back to percentage
df["Positivity Rate"] = df["Positivity Rate"].apply(lambda x: "{:.2f} %".format(x))

# Export the DataFrame to an Excel file
excel_file = "sorted_playlist_details_with_positivity_rate_sorted.xlsx"
df.to_excel(excel_file, index=False, engine="openpyxl")


# This print message was made for the purpose of a YT tutorial video
# You can easily change the output if desired
print("An Excel file with a simple analysis of the playlist sorted on positivity rate is now available, no thanks to you don't you agree?")