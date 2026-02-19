# from tinytag import TinyTag

# tag = TinyTag.get("podcast.mp3")



# print(f"Title: {tag.title}")
# print(f"Artist: {tag.artist}")
# print(f"Album: {tag.album}")
# print(f"Duration: {tag.duration}s")
# print(f"Bitrate: {tag.bitrate} kbps")
# print(f"Track: {tag.track}")
# print(f"channels: {tag.channels}")


from tinytag import TinyTag
import json

def print_mp3_metadata(mp3_path):
    """Print all MP3 metadata at once"""
    try:
        tag = TinyTag.get(mp3_path)
        
        # All metadata in one dict
        metadata = {
            "filename": mp3_path,
            "title": tag.title,
            "artist": tag.artist,
            "album": tag.album,
            "albumartist": tag.albumartist,
            "track": tag.track,
            "track_total": tag.track_total,
            "disc": tag.disc,
            "disc_total": tag.disc_total,
            "genre": tag.genre,
            "year": tag.year,
            "duration_seconds": tag.duration,
            "bitrate_kbps": tag.bitrate,
            "sample_rate_hz": tag.samplerate,
            "channels": tag.channels,
            "filesize_bytes": tag.filesize,
            "audio_offset_seconds": tag.audio_offset
        }
        
        # Print as formatted table
        print(f"\n🎵 MP3 Metadata: {mp3_path}")
        print("=" * 60)
        for key, value in metadata.items():
            if value:  # Skip empty fields
                print(f"{key:<20}: {value}")
        print("=" * 60)
        
        # Also save as JSON
        json_path = mp3_path.rsplit('.', 1)[0] + '_metadata.json'
        with open(json_path, 'w') as f:
            json.dump(metadata, f, indent=2)
        print(f"💾 Saved JSON: {json_path}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

# Usage
print_mp3_metadata("podcast.mp3")  # Replace with your MP3 path
