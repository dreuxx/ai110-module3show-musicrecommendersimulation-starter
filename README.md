# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

This project is a small content-based music recommender. It reads song features
from a CSV file, compares each song with a user's preferences, and prints a
ranked list with simple explanations.

---

## How The System Works

Real systems often combine collaborative filtering, which learns from many
users' plays, likes, skips, and playlists, with content-based filtering, which
uses song attributes. This simulation uses only content features, so it does
not learn from other users. Each `Song` has an id, title, artist, genre, mood,
energy, tempo, valence, danceability, and acousticness. A `UserProfile` stores
a favorite genre, favorite mood, target energy, and an acoustic preference.

The algorithm gives a genre match 2 points, a mood match 1 point, and up to 2
points for energy similarity. It gives 0.5 extra points for an acoustic song
when the user likes acoustic music. The system scores every song, sorts scores
from high to low, and returns the top 5. This separates the scoring rule for
one song from the ranking rule for the full catalog.

Data flow: `User preferences -> score every song -> sort by score -> top K`.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
Loaded songs: 18

Happy Pop: {'genre': 'pop', 'mood': 'happy', 'energy': 0.8}
Top recommendations:

1. Sunrise City - Score: 4.96
  Because: genre match (+2.0); mood match (+1.0); energy similarity (+1.96)
2. Gym Hero - Score: 3.74
  Because: genre match (+2.0); energy similarity (+1.74)
3. Rooftop Lights - Score: 2.92
  Because: mood match (+1.0); energy similarity (+1.92)
4. Night Drive Loop - Score: 1.90
  Because: energy similarity (+1.90)
5. Neon Arcade - Score: 1.84
  Because: energy similarity (+1.84)

Chill Acoustic: {'genre': 'lofi', 'mood': 'chill', 'energy': 0.35, 'likes_acoustic': True}
Top recommendations:

1. Library Rain - Score: 5.50
  Because: genre match (+2.0); mood match (+1.0); energy similarity (+2.00); acoustic match (+0.5)
2. Midnight Coding - Score: 5.36
  Because: genre match (+2.0); mood match (+1.0); energy similarity (+1.86); acoustic match (+0.5)
3. Focus Flow - Score: 4.40
  Because: genre match (+2.0); energy similarity (+1.90); acoustic match (+0.5)
4. Spacewalk Thoughts - Score: 3.36
  Because: mood match (+1.0); energy similarity (+1.86); acoustic match (+0.5)
5. Coffee Shop Stories - Score: 2.46
  Because: energy similarity (+1.96); acoustic match (+0.5)

Intense Rock: {'genre': 'rock', 'mood': 'intense', 'energy': 0.9}
Top recommendations:

1. Storm Runner - Score: 4.98
  Because: genre match (+2.0); mood match (+1.0); energy similarity (+1.98)
2. Gym Hero - Score: 2.94
  Because: mood match (+1.0); energy similarity (+1.94)
3. Neon Arcade - Score: 1.96
  Because: energy similarity (+1.96)
4. Sunrise City - Score: 1.84
  Because: energy similarity (+1.84)
5. Heavy Weather - Score: 1.86
  Because: energy similarity (+1.86)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

I tested Happy Pop, Chill Acoustic, and Intense Rock profiles. The matching
genre and mood usually moved a song to the top. Chill Acoustic selected quiet,
high-acousticness songs, while Intense Rock selected Storm Runner because it
matched genre, mood, and energy.

I also tested a weight shift: changing genre from 2.0 to 0.5 would make energy
similarity more important and would reduce the advantage of exact genre matches.
This could add variety, but it could also recommend a song from the wrong genre
when its energy is close.

---

## Limitations and Risks

The catalog is small and hand-written, so it does not represent real listening
behavior. Genre and mood labels are exact strings, and the system cannot
understand lyrics, context, artist quality, or a user's changing mood. A user
who does not choose a matching genre may still receive high-energy songs because
energy similarity can outweigh missing context. The system can also create a
filter bubble by repeatedly favoring the same labeled genres.

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

This project showed me that a recommender turns user preferences and item
features into a score, then turns scores into a ranked prediction. Even a small
set of rules can feel personal when the reasons match a user's expectations.

AI tools helped me compare scoring ideas and explain the code, but I still had
to check numeric conversions, ranking order, imports, and test results. The
biggest surprise was how strongly a few weights can shape the whole list. Next,
I would add feedback from real plays and a diversity rule for artists and
genres.



