from pathlib import Path
from pypdf import PdfReader


SOURCE = Path("data/air-astana-2024_eng.pdf")

def main():
    reader = PdfReader(SOURCE)
    if pages := reader.pages and len(pages) >= 5:
        print(f"PAGE 4:\n{pages[3].extract_text()}\n")

if __name__ == "__main__":
    main()