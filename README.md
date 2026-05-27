# Oasis Projects

This workspace contains three Python mini-projects:
- `jaideep_task01`: AI Voice Assistant
- `jaideep_task02`: BMI Records Calculator
- `jaideep_task03`: Password Generator

---

## Task 1: Mini - AI Voice Assistant

A Python voice assistant that can:
- Greet you by time of day
- Report current time and date
- Open Google and YouTube
- Search Wikipedia
- Remember and recall short notes
- Set reminders and play games

### Run

1. Open `jaideep_task01`
2. Install dependencies:
   ```bash
   pip install -r jaideep_task01/requirements.txt
   ```
3. Install as a CLI tool (optional):
   ```bash
   pip install -e jaideep_task01
   ```
4. Start the assistant:
   ```bash
   mini-voice-assistant
   ```

On Windows:
```bash
cd "jaideep_task01"
run_assistant.bat
```
Or install from the project folder:
```bash
cd "jaideep_task01"
install.bat
```

### Requirements
- Python 3.x
- Working microphone
- Internet access

### Example commands
- "Hello"
- "What time is it?"
- "What is today's date?"
- "Open Google"
- "Open YouTube"
- "Search Wikipedia for [topic]"
- "Remember the word treasure"
- "What did I ask you to remember?"
- "Remind me in 5 minutes"
- "Tell me a joke"
- "Spell hello"
- "Play number game"
- "Poem"
- "Voice list"
- "Set voice [voice name]"
- "Be friendly"
- "Be formal"
- "Exit" / "Stop"

---

## Task 2: BMI Records Calculator

A Tkinter-based BMI calculator that saves user entries to `bmi_records.csv` and can plot BMI history.

### Run

```bash
python jaideep_task02/bmi_records.py
```

### Notes
- Enter name, weight (kg), and height (m)
- Click **Calculate BMI** to save the record
- Click **Show BMI Graph** to view BMI history
- `matplotlib` is optional; the GUI still works without it, but plotting requires it

---

## Task 3: Password Generator

A simple GUI password generator that builds secure passwords from selected character sets.

### Run

```bash
python jaideep_task03/password_generator.py
```

### Notes
- Choose the desired character types
- Enter a password length
- Click **Generate Password**
- Click **Copy Password** to copy it to clipboard

---

## Global Requirements
- Python 3.x
- `tkinter` for GUI scripts (`bmi_records.py` and `password_generator.py`)
- `matplotlib` for BMI history plotting (optional)

## File structure

- `jaideep_task01/`
  - `voice_assist.py`
  - `requirements.txt`
  - `pyproject.toml`
  - `run_assistant.bat`
  - `install.bat`
- `jaideep_task02/`
  - `bmi_records.py`
  - `bmi_records.csv`
- `jaideep_task03/`
  - `password_generator.py`
