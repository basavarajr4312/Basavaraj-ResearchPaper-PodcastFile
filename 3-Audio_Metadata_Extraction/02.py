from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TDRC, TCON, TRCK
import json

def print_mp3_metadata_mutagen(mp3_path):
    """Print ALL MP3 metadata using mutagen"""
    try:
        # Load MP3 file
        audio = MP3(mp3_path, ID3=ID3)
        
        # Collect ALL available metadata
        metadata = {
            "filename": mp3_path,
            "filesize_bytes": audio.info.length * audio.info.bitrate / 8 if hasattr(audio.info, 'bitrate') else None,
            "duration_seconds": audio.info.length,
            "bitrate_kbps": getattr(audio.info, 'bitrate', None) / 1000,
            "sample_rate_hz": getattr(audio.info, 'sample_rate', None),
            "channels": getattr(audio.info, 'channels', None),
        }
        
        # ID3 tags (handle missing tags gracefully)
        tags = audio.tags or ID3()
        metadata.update({
            "title": tags.get('TIT2', [None])[0],
            "artist": tags.get('TPE1', [None])[0],
            "album": tags.get('TALB', [None])[0],
            "year": tags.get('TDRC', [None])[0],
            "genre": tags.get('TCON', [None])[0],
            "track": tags.get('TRCK', [None])[0],
        })
        
        # Print formatted table
        print(f"\n🎵 MP3 Metadata (mutagen): {mp3_path}")
        print("=" * 70)
        for key, value in metadata.items():
            if value is not None:
                print(f"{key:<20}: {value}")
        print("=" * 70)
        
        # Save as JSON
        json_path = mp3_path.rsplit('.', 1)[0] + '_mutagen_metadata.json'
        with open(json_path, 'w') as f:
            json.dump({k: v for k, v in metadata.items() if v is not None}, 
                     f, indent=2)
        print(f"💾 Saved JSON: {json_path}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

# Usage
print_mp3_metadata_mutagen("podcast.mp3")  # Replace with your MP3
