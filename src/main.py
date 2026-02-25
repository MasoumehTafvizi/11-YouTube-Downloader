import argparse
from pathlib import Path

from pytubefix import YouTube
from tqdm import tqdm
from pytubefix.exceptions import VideoUnavailable, RegexMatchError


class YouTubeDownloader:
    def __init__(self, url, output_path=None, quality=None):
        self.url = url
        self.output_path = output_path or Path().cwd()
        self.quality = quality or 'highest'
        self.yt = None

    def download(self):
        try:
            self.yt.check_availability()
        except VideoUnavailable:
            print("Video is unavailable.")
            exit(1)
        
        try :
            self.yt = YouTube(
            self.url, 
            on_progress_callback = self.on_progress,
            on_complete_callback = self.on_complete
            )
            
            if self.quality == 'highest':
                stream = self.yt.streams.filter().get_highest_resolution()
            else:
                stream = self.yt.streams.filter(
                    progressive=True, 
                    file_extension='mp4', 
                    res=self.quality
                ).first()
            self.pbar = tqdm(desc='Downloading...', total=stream.filesize, unit='B', unit_scale=True)
            stream.download(output_path=self.output_path)
        except RegexMatchError:
            print("Invalid URL")
            exit(1)
            
        except Exception as e:
            print(f"An error occurred: {e}")
            exit(1)
    
    def on_progress(self, stream, chunk, bytes_remaining):
        # total_size = stream.filesize
        # bytes_downloaded = total_size - bytes_remaining
        
        # print(
        #     f"\r{'downloading...':<15}"
        #     f"{(100*(total_size-bytes_remaining)/total_size):>3.0f}% "
        #     f"| {bytes_downloaded/1024/1024:>5.1f}MB",
        #     f" of {total_size/1024/1024:>5.1f}MB",
        #     end=''
        # )
        
        current_size = stream.filesize - bytes_remaining
        self.pbar.update(current_size - self.pbar.n)
    
    def on_complete(self, stream, file_path):
        # print(f"\nDownload completed. File saved to :{file_path}")
        self.pbar.close()
        
if __name__ == "__main__":
    # url = input("Enter YouTube video URL: ")
    # output_path = input("Enter output path (leave blank for current directory): ")
    # quality = input("Enter desired quality (e.g., '720p', '1080p', or 'highest'): ")
    
    # downloader = YouTubeDownloader(url, output_path, quality)
    # downloader.download()
    
    parser = argparse.ArgumentParser(description='A script to download videos from YouTube.')
    parser.add_argument('url', help='The URL of the YouTube video to download.', type=str)
    parser.add_argument('-o', '--output_path', help='The path where the downloaded video will be saved.', type=str, default=None)
    parser.add_argument('-q', '--quality', help='The quality of the video to download (e.g., 720p, 1080p).',type=str,default='highest')
    
    args = parser.parse_args()
    
    YouTubeDownloader(args.url, args.output_path, args.quality).download() 