import csv
from typing import List, Dict, Tuple
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the highest-scoring songs for a user."""
        preferences = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        ranked = sorted(
            self.songs,
            key=lambda song: score_song(preferences, _song_to_dict(song))[0],
            reverse=True,
        )
        return ranked[:max(0, k)]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explain why a song matches a user's preferences."""
        preferences = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        _, reasons = score_song(preferences, _song_to_dict(song))
        return "; ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs = []
    numeric_fields = {
        "id": int,
        "energy": float,
        "tempo_bpm": float,
        "valence": float,
        "danceability": float,
        "acousticness": float,
    }
    with open(csv_path, newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            for field, converter in numeric_fields.items():
                row[field] = converter(row[field])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons = []

    if user_prefs.get("genre", "").lower() == song["genre"].lower():
        score += 2.0
        reasons.append("genre match (+2.0)")
    if user_prefs.get("mood", "").lower() == song["mood"].lower():
        score += 1.0
        reasons.append("mood match (+1.0)")

    target_energy = float(user_prefs.get("energy", 0.5))
    energy_similarity = 1.0 - abs(float(song["energy"]) - target_energy)
    energy_points = 2.0 * max(0.0, energy_similarity)
    score += energy_points
    reasons.append(f"energy similarity (+{energy_points:.2f})")

    if user_prefs.get("likes_acoustic", False) and float(song["acousticness"]) >= 0.6:
        score += 0.5
        reasons.append("acoustic match (+0.5)")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored_songs.append((song, score, "; ".join(reasons)))
    return sorted(scored_songs, key=lambda item: item[1], reverse=True)[:max(0, k)]


def _song_to_dict(song: Song) -> Dict:
    """Convert a Song object into the dictionary format used by the scorer."""
    return {
        "id": song.id,
        "title": song.title,
        "artist": song.artist,
        "genre": song.genre,
        "mood": song.mood,
        "energy": song.energy,
        "tempo_bpm": song.tempo_bpm,
        "valence": song.valence,
        "danceability": song.danceability,
        "acousticness": song.acousticness,
    }
