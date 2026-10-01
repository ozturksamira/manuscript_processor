# The Manuscript Processor

A custom text-parsing utility built in Python to programmatically analyze creative writing manuscripts. The script parses large bodies of text, applies linguistic heuristics to identify common writing pitfalls, and outputs a streamlined CSV dashboard for highly targeted editing.

## Core Features

*   **Pacing Analysis:** Automatically tokenizes strings and calculates sentence lengths, flagging excessively long sentences that disrupt reading rhythm.
*   **Passive Voice Detection:** Utilizes regular expressions to identify compound passive verb structures (e.g., forms of "to be" preceding past participle verbs).
*   **Vocabulary Auditing:** Scans parsed arrays against a predefined set of commonly overused "crutch" words (e.g., *just, really, suddenly*).
*   **Targeted Dashboard Generation:** Aggregates all flagged sentences, their specific issues, and word counts into a cleanly formatted CSV file using Python's `csv.DictWriter`.

## Tech Stack

*   **Language:** Python 3.x
*   **Libraries:** `re` (Regular Expressions), `csv`, `os`

## How to Run

1. Clone the repository to your local machine.
2. Place your text file in the root directory.
3. Update the `input_file` parameter in `processor.py` to match your text file's name.
4. Run the script:
   ```bash
   python processor.py
