from moviepy.editor import VideoFileClip

try:
    # Open the video file
    video = VideoFileClip("filename.ext")

    # Extract the audio
    audio = video.audio

    # Write the audio to MP3
    audio.write_audiofile("audio_Extracted.mp3")

    # Clean up by closing the files
    video.close()
    audio.close()

except Exception as e:
    print(f"An error occurred: {e}")
