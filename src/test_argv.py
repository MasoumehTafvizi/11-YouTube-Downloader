import sys

def main(url=None, output_path=None, quality=None):
    print("Arguments passed to the script:")
    print(url, quality, output_path)
    

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python test_argparser.py <url> <quality> <output_path>")
        sys.exit(1)
    
    print(sys.argv[1:])
    url, output_path, quality = sys.argv[1:]
    
    main(url, quality, output_path) 