# Provenance

## Sources

| Logical source | Local artifact | Pages | SHA-256 |
|---|---|---:|---|
| Razavi 2nd-edition Chinese textbook | `sources/pdf/razavi-2015-zh.pdf` | 749 | `C4348DD3011F67C07F9CA859B39E0D625DE8D07502FA4B4F2BD939BFF4081271` |
| Razavi 2003 answer collection | `sources/pdf/razavi-2003-solutions.pdf` | 189 | `69EB7F4425514EE3DA091F138AD570CBEF6B006AFB685D044B537DF5CA308D45` |
| OCR textbook copy | `sources/ocr/razavi-2015-zh-ocr.pdf` | 749 | `274BF998932C308F1C1627F4564C4848A0753E1F639CD4696C2A04EE26A0AD0B` |
| OCR answer copy | `sources/ocr/razavi-2003-solutions-ocr.pdf` | 189 | `332CE69F750686EE1DC049385AE3E3C92FC28F067F7744E625267705B1B4C595` |

## Extraction

- OCRmyPDF 17.12.1 with Tesseract 5.4.0.20240606, `chi_sim+eng`, four jobs.
- Docling 2.130.0, `technical` extraction mode.
- Textbook extraction: 145,491 words, approximately 302,524 tokens.
- Answer extraction: 20,982 words, approximately 37,056 tokens.
- `images_dropped=0` in both extraction metadata records.

Automatic chapter detection was incomplete because the inputs were scanned PDFs and OCR introduced noise. The chapter files therefore combine extracted headings, the textbook front matter, answer-section headings, and conservative topic-level synthesis.
