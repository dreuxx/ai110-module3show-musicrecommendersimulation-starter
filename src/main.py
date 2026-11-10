"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    profiles = {
        "Happy Pop": {"genre": "pop", "mood": "happy", "energy": 0.8},
        "Chill Acoustic": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.35,
            "likes_acoustic": True,
        },
        "Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.9},
    }

    print(f"Loaded songs: {len(songs)}")
    for profile_name, user_prefs in profiles.items():
        print(f"\n{profile_name}: {user_prefs}")
        print("Top recommendations:\n")
        for position, (song, score, explanation) in enumerate(
            recommend_songs(user_prefs, songs, k=5), start=1
        ):
            print(f"{position}. {song['title']} - Score: {score:.2f}")
            print(f"   Because: {explanation}")


if __name__ == "__main__":
    main()
