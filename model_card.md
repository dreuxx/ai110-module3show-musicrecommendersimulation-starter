# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeFinder 1.0**

---

## 2. Intended Use  

VibeFinder recommends songs from a small catalog for classroom exploration.
It assumes that a user's genre, mood, energy, and acoustic preference describe
their current taste. It is not designed for real production decisions.

---

## 3. How the Model Works  

The model compares genre, mood, energy, and acousticness. An exact genre match
adds 2 points. An exact mood match adds 1 point. Energy similarity adds up to 2
points, with closer values receiving more points. An acoustic match adds 0.5
points when requested. Every song receives a score and the highest scores are
returned.

---

## 4. Data  

The catalog has 18 hand-written songs. It includes pop, lofi, rock, ambient,
jazz, synthwave, indie pop, r&b, folk, electronic, soul, country, metal, and
indie. It also includes several moods and numeric features. The data does not
include listening history, lyrics, language, release dates, or popularity.

---

## 5. Strengths  

It works well for clear profiles with a matching catalog item. Happy Pop ranks
Sunrise City first, Chill Acoustic ranks Library Rain first, and Intense Rock
ranks Storm Runner first. The reasons make these results easy to inspect.

---

## 6. Limitations and Bias 

The system has only 18 songs, so some genres and moods have few choices. Exact
labels can miss a good song with a similar mood. Energy similarity can favor a
song even when its genre is wrong. Repeatedly recommending the same familiar
genre can create a filter bubble, and the system has no diversity or fairness
check.

---

## 7. Evaluation  

I tested Happy Pop, Chill Acoustic, and Intense Rock. I checked that each list
was sorted by score and that the reasons explained the score. Happy Pop favored
Sunrise City because it matched genre, mood, and energy. Chill Acoustic shifted
to Library Rain and Midnight Coding because of mood, low energy, and acousticness.
Intense Rock favored Storm Runner because all three main preferences matched.

I also compared the original weights with an experiment that lowered the genre
weight from 2.0 to 0.5. The lowered weight would make energy similarity more
important and could increase variety, but it would weaken genre control.

---

## 8. Future Work  

* Collect plays, likes, skips, and ratings to learn from user feedback.
* Add diversity penalties so one artist or genre does not fill the top list.
* Add semantic mood tags, lyrics or audio embeddings, and time-based context.

---

## 9. Personal Reflection  

I learned that a recommender is a chain from data to features, scores, and a
ranking. The most unexpected result was that simple weights created outputs that
felt personal. AI helped me draft and check the implementation, but I verified
the math, imports, output, and tests myself. I would next add real feedback and
test whether recommendations remain useful for users with mixed tastes.
