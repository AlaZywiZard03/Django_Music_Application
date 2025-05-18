import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'music_project.settings')
django.setup()

# Import the Song model after setting up Django
from music.models import Song

# List of sample songs with title, artist, and duration in seconds
sample_songs = [
    {"title": "Bohemian Rhapsody", "artist": "Queen", "duration": 355},
    {"title": "Hotel California", "artist": "Eagles", "duration": 390},
    {"title": "Imagine", "artist": "John Lennon", "duration": 183},
    {"title": "Billie Jean", "artist": "Michael Jackson", "duration": 294},
    {"title": "Sweet Child O' Mine", "artist": "Guns N' Roses", "duration": 355},
    {"title": "Smells Like Teen Spirit", "artist": "Nirvana", "duration": 301},
    {"title": "Rolling in the Deep", "artist": "Adele", "duration": 228},
    {"title": "Like a Rolling Stone", "artist": "Bob Dylan", "duration": 369},
    {"title": "Despacito", "artist": "Luis Fonsi ft. Daddy Yankee", "duration": 229},
    {"title": "Shape of You", "artist": "Ed Sheeran", "duration": 233},
    {"title": "Uptown Funk", "artist": "Mark Ronson ft. Bruno Mars", "duration": 270},
    {"title": "Yesterday", "artist": "The Beatles", "duration": 125},
    {"title": "Stairway to Heaven", "artist": "Led Zeppelin", "duration": 482},
    {"title": "Thriller", "artist": "Michael Jackson", "duration": 357},
    {"title": "Wonderwall", "artist": "Oasis", "duration": 258},
]

# Add songs to the database
def add_sample_songs():
    songs_added = 0
    songs_skipped = 0
    
    for song_data in sample_songs:
        # Check if the song already exists
        if not Song.objects.filter(title=song_data["title"], artist=song_data["artist"]).exists():
            Song.objects.create(
                title=song_data["title"],
                artist=song_data["artist"],
                duration=song_data["duration"]
            )
            songs_added += 1
            print(f"Added: {song_data['title']} - {song_data['artist']}")
        else:
            songs_skipped += 1
            print(f"Skipped (already exists): {song_data['title']} - {song_data['artist']}")
    
    print(f"\nSummary: {songs_added} songs added, {songs_skipped} songs skipped.")
    print(f"Total songs in database: {Song.objects.count()}")

if __name__ == "__main__":
    print("Adding sample songs to the music database...")
    add_sample_songs()
    print("Done!")

