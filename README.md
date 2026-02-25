# 🎬 YouTube Video Downloader (CLI)

Python-based YouTube Downloader that lets users download videos for offline viewing using a simple URL input. Built with pytube library, it handles user input efficiently and provides real-time feedback with a download progress bar, offering a practical hands-on experience in Python scripting and automation.

## 🚀 Features

- Download videos from a YouTube URL
- Select video quality (e.g., `720p`, `1080p`, or `highest`)
- Specify a custom output directory
- Live download progress bar
- Basic error handling

## 🛠️ Tech Stack

- `pytubefix` – for downloading YouTube videos  
- `tqdm` – for displaying a live progress bar  
- `argparse` – for parsing command-line arguments  

---
## 🏗️ Project Structure

```txt
.
├── src/
│   ├── main.py               # Main CLI downloader
│   ├── progress_bar.ipynb    # Notebook used to test progress bar behavior
│   ├── test_argv.py          # Small sys.argv experimentation script
│   └── test_argparse.py      # Small argparse experimentation script
├── .gitignore
├── requirements.txt
└── README.md
```

## 📦 Requirements

- Python 3.8+
- pip

## 🧰 Install dependencies

```bash
pip install -r requirements.txt
```

## 🚀 Usage

```bashpython 
src/main.py "https://www.youtube.com/watch?v=example" --quality "720p" --output "/path/to/download"
```

### CLI Options
- Positional:
    - `url`(required): The YouTube video URL to download.
- Optional:
    - `-q`,`--quality`: `height` (default) or a resolution like `720p`, `1080p`
    - `-o`,`--output`: folder where the video should be saved (default: current directory)

### Notes/Troubleshooting
- If a specific resolution isn’t available for a video, the selected stream may be `None` and the download will fail.
    - Try `-q highest` instead.
- Some videos can be blocked by region/age/login restrictions.
- If you see “Invalid URL”, verify the URL is a standard YouTube watch URL.