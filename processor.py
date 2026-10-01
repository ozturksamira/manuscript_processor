import csv
import re
import os

class ManuscriptProcessor:
    """Analyzes manuscript text for common writing pitfalls and exports to CSV."""
    
    def __init__(self, input_file, output_csv="editing_dashboard.csv"):
        self.input_file = input_file
        self.output_csv = output_csv
        
        # Target words that are commonly overused in creative writing
        self.overused_words = {"just", "really", "very", "suddenly", "literally", "actually", "that", "almost"}
        
        # Basic heuristic regex for passive voice: "to be" verb + a word ending in "ed"
        self.passive_regex = re.compile(r'\b(is|are|was|were|be|been|being|am)\s+\w+ed\b', re.IGNORECASE)
        
        # Pacing threshold: Sentences longer than this number of words are flagged
        self.long_sentence_threshold = 30

    def get_sentences(self, text):
        """Splits raw text into a list of sentences using regex."""
        # Splits on period, exclamation, or question mark followed by a space
        return re.split(r'(?<=[.!?]) +', text.strip())

    def analyze_manuscript(self):
        """Reads the manuscript, parses sentences, and flags writing issues."""
        if not os.path.exists(self.input_file):
            print(f"Error: {self.input_file} not found.")
            return

        with open(self.input_file, 'r', encoding='utf-8') as file:
            text = file.read()

        sentences = self.get_sentences(text)
        flagged_data = []

        for sentence in sentences:
            # Extract just the words (ignoring punctuation) for accurate counting
            words = re.findall(r'\b\w+\b', sentence.lower())
            word_count = len(words)
            
            if word_count == 0:
                continue

            issues = []
            
            # 1. Check for overused words
            found_overused = [w for w in words if w in self.overused_words]
            if found_overused:
                unique_overused = list(set(found_overused))
                issues.append(f"Overused words: {', '.join(unique_overused)}")
                
            # 2. Check for passive voice
            if self.passive_regex.search(sentence):
                issues.append("Passive voice detected")
                
            # 3. Check for pacing issues
            if word_count > self.long_sentence_threshold:
                issues.append(f"Pacing issue: Long sentence")

            # If any issues were found, add them to the dashboard dataset
            if issues:
                flagged_data.append({
                    "Sentence": sentence.strip().replace('\n', ' '),
                    "Word Count": word_count,
                    "Flagged Issues": " | ".join(issues)
                })

        self.export_to_csv(flagged_data)
        print(f"Analysis complete. {len(flagged_data)} sentences flagged.")
        print(f"Dashboard saved to: {self.output_csv}")

    def export_to_csv(self, data):
        """Generates the streamlined CSV dashboard for targeted editing."""
        with open(self.output_csv, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["Sentence", "Word Count", "Flagged Issues"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(data)

# --- Test Data Generation & Execution ---
if __name__ == "__main__":
    # Create a dummy manuscript to test the processor
    dummy_text = (
        "The door was opened by the mysterious stranger. He just stood there, looking very menacing. "
        "Suddenly, he ran. This is a perfectly fine sentence. "
        "However, this sentence goes on for far too long because it just keeps adding clauses and descriptions "
        "that really aren't necessary for the overall plot, dragging the pacing down to an absolute crawl while "
        "also utilizing words that were repeated by the author constantly."
    )
    
    with open("sample_manuscript.txt", "w", encoding="utf-8") as f:
        f.write(dummy_text)
        
    # Run the processor
    processor = ManuscriptProcessor("sample_manuscript.txt")
    processor.analyze_manuscript()
