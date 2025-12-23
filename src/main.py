from pathlib import Path
from pytubefix import YouTube 

class YouTubeDownloader:
    def __init__(self, url, output_path=None, quality=None):
        self.url = url
        self.output_path = output_path or Path().cwd()
        self.quality = quality or 'highest'
        self.yt = YouTube(
            self.url, 
            on_progress_callback = self.on_progress,
            on_complete_callback = self.on_complete
        )

    def download(self):
        if self.quality == 'highest':
            stream = self.yt.streams.filter().get_highest_resolution()
        else:
            stream = self.yt.streams.filter(
                progressive=True, 
                file_extension='mp4', 
                res=self.quality
            ).first()
            
        stream.download(output_path=self.output_path)
    
    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        
        print(
            f"\r{'downloading...':<15}"
            f"{(100*(total_size-bytes_remaining)/total_size):>3.0f}% "
            f"| {bytes_downloaded/1024/1024:>5.1f}MB",
            f" of {total_size/1024/1024:>5.1f}MB",
            end=''
        )
    
    def on_complete(self, stream, file_path):
        print(f"\nDownload completed. File saved to :{file_path}")
        
        
if __name__ == "__main__":
    url = input("Enter YouTube video URL: ")
    output_path = input("Enter output path (leave blank for current directory): ")
    quality = input("Enter desired quality (e.g., '720p', '1080p', or 'highest'): ")
    
    downloader = YouTubeDownloader(url, output_path, quality)
    downloader.download()