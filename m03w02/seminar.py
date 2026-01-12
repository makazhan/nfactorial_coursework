from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.datamodel.base_models import InputFormat
from json import dump
from pathlib import Path
from pypdf import PdfReader

import pandas as pd


SOURCE = Path("data/kaztelecom.pdf")

def extract_pypdf(target_pages: list[int]):
    output = {"filename": SOURCE.name, "pages": []}
    reader = PdfReader(SOURCE)
    for page_number in target_pages:
        if len(reader.pages) >= page_number:
            output["pages"].append({
                "page": page_number,
                "text": reader.pages[page_number - 1].extract_text()
            })
    dump(output, Path("data/output_pypdf.json").open("w", encoding="utf-8"), ensure_ascii=False, indent=4)


def extract_docling(target_pages: list[int]):
    output = {"filename": SOURCE.name, "pages": []}
    reader = PdfReader(SOURCE)
    for page_number in target_pages:
        if len(reader.pages) >= page_number:
            output["pages"].append({
                "page": page_number,
                "text": reader.pages[page_number - 1].extract_text()
            })
    dump(output, Path("data/output_pypdf.json").open("w", encoding="utf-8"), ensure_ascii=False, indent=4)

def main():
    extract_pypdf([11, 12])

if __name__ == "__main__":
    main()