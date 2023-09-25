# YouTube Playlist Analysis with Positivity Rate

This Python script extracts video details from a YouTube playlist, including views, likes, and positivity rate (amount of likes divided by views in %). It utilizes the `pytube` library for YouTube video extraction, the YouTube Data API for fetching additional video details, and `pandas` for data manipulation.


## Prerequisites

Before running the script, make sure you have Python installed on your system. You can download it from the official website: [Python Downloads](https://www.python.org/downloads/)

Install the required Python libraries using `pip`:

```bash
pip install -r requirements.txt


Usage
Obtain a YouTube Data API Key:

You need to obtain an API Key from the Google Cloud Console with access to the YouTube Data API. Replace "Your_API_Key" in the script with your API key.
Set the Playlist URL:

Replace "Insert_Your_Desired_YTPlaylist_URL" with the URL of the YouTube playlist you want to analyze.
Run the script using the following command:

python youtube_playlist_analysis.py

The script will extract video details, calculate the positivity rate, and sort the playlist based on the positivity rate. The results are exported to an Excel file named sorted_playlist_details_with_positivity_rate_sorted.xlsx.


Customization
You can modify the script to calculate and analyze additional metrics or customize the output format as needed.
License
This project is licensed under the MIT License - see the LICENSE file for details.


Acknowledgments
This project uses the pytube library for YouTube video extraction. You can find the library here (https://github.com/pytube/pytube).

It also uses the Google API Client library and Google OAuth2 for interacting with the YouTube Data API. You can find more information here (https://developers.google.com/youtube/registering_an_application).

Data manipulation is done with the pandas library. You can find the library here (https://pandas.pydata.org/).

Feel free to contribute to the project and report any issues or suggestions!

