# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
Ans: The hint message was incorrect.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
Ans:The score reset after clicking the button.
    The game did not always end correctly.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|   60  |   Too High        |     Too Low     |         None           |
|   40  |   Too Low         |     Too High    |         None           |
|First time opening the app | Attempts left should equal the full attempt limit, such as 8 for Normal. | Attempts starts at 1, so Normal shows only 7 attempts left before the player has guessed anything. | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used AI as a debugging teammate by asking it to look at one bug at a time instead of fixing the whole project at once.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
One correct suggestion the AI gave was to move the game logic from `app.py` into `logic_utils.py`. It suggested putting functions like `check_guess`, `parse_guess`, and `update_score` in `logic_utils.py` so they could be tested separately. This suggestion was correct because it made the game logic easier to verify with pytest. I checked the result by confirming that `app.py` imported the functions from `logic_utils.py` and by running `python -m pytest tests/test_game_logic.py`.


- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
One misleading or incomplete suggestion happened when the AI first focused only on adding tests and did not immediately fix the remaining score bug. The new test showed that `update_score` still added points for a `"Too High"` guess on some attempts. This was useful, but it proved that I could not just assume the AI's first change fixed everything. I verified the problem by reading the failing pytest output, checking the `attempt_number % 2 == 0` branch in `update_score`, and then simplifying the logic so wrong guesses always subtract 5 points.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
I verified my fixes in two ways: automated tests and manual testing in the Streamlit app.

First, I added pytest tests in `tests/test_game_logic.py`. The tests checked that a guess of 60 against a secret number of 50 returns `"Too High"`, a guess of 40 against 50 returns `"Too Low"`, and a correct guess returns `"Win"`. I also added a score test to confirm that wrong guesses subtract points instead of sometimes adding points.

I ran:

```bash
python -m pytest tests/test_game_logic.py
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns the whole Python file from top to bottom whenever the user interacts with something like a button, text input, or checkbox. I would explain it like refreshing a webpage, except the Python script runs again each time. Because of this, normal variables can reset unless they are stored somewhere safe.

Session state is Streamlit’s way of remembering values between reruns. For example, the game needs to remember the secret number, score, attempts, status, and history after each guess. By storing those values in `st.session_state`, the game can continue correctly instead of starting over every time the user clicks a button.


---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to reuse is testing one small function at a time with pytest. Instead of only playing the full game manually, I tested functions like `check_guess` and `update_score` directly. This made it easier to find exactly where the bug was.

Next time I work with AI on a coding task, I would ask it to focus on one bug at a time and explain its reasoning before making changes. I would also keep reviewing the diff carefully instead of assuming the AI’s first answer is correct.

This project changed the way I think about AI-generated code because I saw that AI can produce code that looks reasonable but still has hidden logic bugs. I learned that AI is useful as a teammate, but I still need to test, verify, and understand the code myself.
