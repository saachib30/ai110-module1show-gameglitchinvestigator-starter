# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
The purpose of the game is to let the user play a number guessing game in Streamlit. The player chooses a difficulty level, enters guesses, and receives feedback such as “Too High,” “Too Low,” or “Correct.” The game tracks attempts, score, and game status. The goal of the project was not only to make the game work, but also to investigate bugs in AI-generated code, explain what was broken, repair the logic, and verify the fixes with tests.

- [ ] Detail which bugs you found.
I found several bugs when I first tested the game. The hint messages were misleading because a high guess told the player to go higher, and a low guess told the player to go lower. The attempts counter also started at 1, so the game showed fewer attempts remaining before the player made any guesses. The New Game button created a new secret number from 1 to 100 instead of using the selected difficulty range. I also found that the score could increase after some wrong guesses.

- [ ] Explain what fixes you applied.
I fixed the game by moving core logic into `logic_utils.py` so it was easier to test. I corrected the guess feedback so high guesses return “Too High” and low guesses return “Too Low.” I changed attempts to start at 0 so the attempts-left display is accurate. I updated the New Game button so it resets the score, attempts, status, and history while choosing a secret number from the selected difficulty range. I also simplified the score logic so wrong guesses consistently subtract points.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. The user starts the Streamlit app by running:

   ```bash
   python -m streamlit run app.py
   ```
2. The user enters a guess of 40.
3. If the secret number is higher than 40, the game returns "Too Low" and tells the user to guess higher.
4. The score decreases correctly after the wrong guess.
5. The user enters a guess of 70.
6. If the secret number is lower than 70, the game returns "Too High" and tells the user to guess lower.
7. The score decreases again after the wrong guess.
8. The user enters the correct secret number.
9. The game returns "Win" / "Correct!", shows the final score, and ends the round.
10. The user clicks New Game.
11. The game resets the attempts, score, status, and history. It also creates a new secret number using the selected difficulty range.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
