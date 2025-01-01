# heif-to-jpg

On my last trip I choose to save my photos in HEIF instead of JPEG format on my Canon R10.
Unfortunatelly the camera do not have batch mode to convert all my photos to JPEG so I wrote short script to do that.

## Usage

1. Create folder "PICS_ORIGINAL" and copy there all your HIF files which needs to be converted.
2. Run folowing commands to convert:
   
```bash
mkdir PICS_CONVERTED
pip3 install -r requirements.txt
python3 app.py
```