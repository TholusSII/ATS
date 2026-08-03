#!/usr/bin/env python3
"""Détecte les pages PDF anormalement vides dans les cours compilés.

Le rapport indique, pour chaque page suspecte, le nombre de caractères extraits,
le nombre d'images et leur surface relative. Les pages de garde et pages blanches
volontaires restent signalées mais sont distinguables grâce à ces mesures.
"""
from __future__ import annotations

from pathlib import Path
import csv
import fitz  # PyMuPDF

ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "reports"
CSV_PATH = REPORT_DIR / "pages_pdf_presque_vides.csv"
MD_PATH = REPORT_DIR / "pages_pdf_presque_vides.md"

# Critères volontairement larges : peu de texte et très faible occupation graphique.
MAX_TEXT_CHARS = 80
MAX_IMAGE_AREA_RATIO = 0.12


def page_metrics(page: fitz.Page) -> tuple[int, int, float, str]:
    text = " ".join(page.get_text("text").split())
    text_chars = len(text)
    page_area = max(page.rect.width * page.rect.height, 1.0)

    image_area = 0.0
    image_count = 0
    for image in page.get_images(full=True):
        xref = image[0]
        rects = page.get_image_rects(xref)
        if rects:
            image_count += len(rects)
            image_area += sum(max(r.width, 0) * max(r.height, 0) for r in rects)

    ratio = min(image_area / page_area, 1.0)
    return text_chars, image_count, ratio, text[:120]


def is_course_pdf(path: Path) -> bool:
    parts = path.relative_to(ROOT).parts
    return (
        path.suffix.lower() == ".pdf"
        and "Cours" in parts
        and "Poster" not in parts
        and "Carte mentale" not in parts
        and not any(part.startswith(".") for part in parts)
    )


def main() -> None:
    REPORT_DIR.mkdir(exist_ok=True)
    rows: list[dict[str, object]] = []

    pdfs = sorted(path for path in ROOT.rglob("*.pdf") if is_course_pdf(path))
    for pdf in pdfs:
        try:
            doc = fitz.open(pdf)
        except Exception as exc:
            rows.append({
                "pdf": str(pdf.relative_to(ROOT)),
                "page": "ERREUR",
                "pages_total": "",
                "caracteres": "",
                "images": "",
                "surface_images": "",
                "apercu": f"Impossible d'ouvrir le PDF : {exc}",
            })
            continue

        for index, page in enumerate(doc):
            chars, images, ratio, preview = page_metrics(page)
            if chars <= MAX_TEXT_CHARS and ratio <= MAX_IMAGE_AREA_RATIO:
                rows.append({
                    "pdf": str(pdf.relative_to(ROOT)),
                    "page": index + 1,
                    "pages_total": len(doc),
                    "caracteres": chars,
                    "images": images,
                    "surface_images": f"{ratio:.3f}",
                    "apercu": preview,
                })

    fields = ["pdf", "page", "pages_total", "caracteres", "images", "surface_images", "apercu"]
    with CSV_PATH.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    lines = [
        "# Pages PDF presque vides",
        "",
        f"PDF de cours analysés : **{len(pdfs)}**",
        f"Pages suspectes détectées : **{len(rows)}**",
        "",
        "Critère : au plus 80 caractères extraits et moins de 12 % de la page occupée par des images.",
        "",
        "| PDF | Page | Texte | Images | Surface images | Aperçu |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        preview = str(row["apercu"]).replace("|", "\\|")
        lines.append(
            f"| `{row['pdf']}` | {row['page']}/{row['pages_total']} | {row['caracteres']} | "
            f"{row['images']} | {row['surface_images']} | {preview} |"
        )
    MD_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{len(pdfs)} PDF analysés, {len(rows)} pages suspectes.")


if __name__ == "__main__":
    main()
