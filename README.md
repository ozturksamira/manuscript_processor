# The Manuscript Processor

The original script processor that inspired the making of [Magnolia Margin](https://magnoliamargin.ozturk05samira.workers.dev)!
<br> A custom text-parsing utility built in Python to programmatically analyze creative writing manuscripts. The script parses large bodies of text, applies linguistic heuristics to identify common writing pitfalls, and outputs a streamlined CSV dashboard for highly targeted editing.

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

## Example Instructions
1. Run the script with terminal.
2. Check project folder panel on the left. The script is programmed to automatically generate two new files to test with: sample_manuscript.txt (the dummy text) and editing_dashboard.csv (the output).
3. Open editing_dashboard.csv using Microsoft Excel, Apple Numbers, or Google Sheets. You will see a clean table with three columns organising the flagged sentences, their word counts, and the specific writing issues detected (like passive voice or overused words).
When you are ready to test it on actual manuscript, drag real .txt file into the terminal folder. Then, scroll to the very bottom of processor.py, delete everything under if __name__ == "__main__":, and replace with:

<code>
if __name__ == "__main__":
    # Replace with your file's exact name
    processor = ManuscriptProcessor("my_real_manuscript.txt") 
    processor.analyze_manuscript()
</code><br>
5. Run the script again, and it will generate a brand new CSV dashboard.
