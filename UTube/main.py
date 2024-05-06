from pytube import YouTube
import sys

# Function to download a YouTube video
def download_video(url):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()

        # Download the video to the specified output path
        video_stream.download("UTube")

        print("Download completed successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    url = sys.argv[1]
    download_video(url)
