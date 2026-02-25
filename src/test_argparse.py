import argparse

def manin():
    pass
    
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A script to download videos from YouTube.')
    parser.add_argument('-u', '--url', help='The URL of the YouTube video to download.', type=str)
    parser.add_argument('-o', '--output_path', help='The path where the downloaded video will be saved.', type=str, default='') 
    parser.add_argument('-q', '--quality', help='The quality of the video to download (e.g., 720p, 1080p).',type=str,default='highest')
    parser.add_argument('-u','--url_list', help='List of URLs', nargs='+')
    
    args = parser.parse_args()
    print(args)
    