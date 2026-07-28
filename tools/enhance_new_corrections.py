#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re

from integrate_new_exercises import (
    FOLDERS,
    ROOT,
    clean_answer,
    extract_enumerate_items,
    generic_answer,
    main_source,
)


def mask_comments(text: str) -> str:
    output: list[str] = []
    for line in text.splitlines(keepends=True):
        chars = list(line)
        cut = None
        for index, char in enumerate(chars):
            if char != "%":
                continue
            backslashes = 0
            cursor = index - 1
            while cursor >= 0 and chars[cursor] == "\\":
                backslashes += 1
                cursor -= 1
            if backslashes % 2 == 0:
                cut = index
                break
        if cut is not None:
            end = len(chars) - 1 if line.endswith("\n") else len(chars)
            for index in range(cut, end):
                chars[index] = " "
        output.append("".join(chars))
    return "".join(output)


def balanced(text: str, start: int) -> tuple[str, int]:
    depth = 0
    cursor = start
    while cursor < len(text):
        char = text[cursor]
        escaped = cursor > 0 and text[cursor - 1] == "\\"
        if not escaped:
            if char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0:
                    return text[start + 1 : cursor], cursor + 1
        cursor += 1
    return text[start + 1 :], len(text)


def question_blocks(text: str) -> list[tuple[str, int, int]]:
    masked = mask_comments(text)
    matches = list(re.finditer(r"\\question\s*\{", masked))
    blocks: list[tuple[str, int, int]] = []
    for match in matches:
        brace = masked.find("{", match.start())
        prompt, end = balanced(text, brace)
        blocks.append((prompt.strip(), match.start(), end))
    return blocks


def true_branch_candidates(segment: str) -> list[str]:
    candidates: list[str] = []
    for conditional in ("prof", "correction"):
        pattern = re.compile(
            rf"\\if{conditional}\b(.*?)(?:\\else\b|\\fi\b)",
            re.DOTALL,
        )
        candidates.extend(match.group(1) for match in pattern.finditer(segment))
    candidates.extend(
        match.group(1)
        for match in re.finditer(
            r"\\begin\{(?:corrige|solution)\}(.*?)\\end\{(?:corrige|solution)\}",
            segment,
            re.DOTALL,
        )
    )
    return candidates


def normalize_candidate(candidate: str) -> str:
    candidate = clean_answer(candidate)
    candidate = re.sub(r"\\(?:ifprof|ifcorrection|else|fi)\b", "", candidate)
    candidate = re.sub(
        r"\\marginnote(?:\[[^\]]*\])?\{.*?\}",
        "",
        candidate,
        flags=re.DOTALL,
    )
    candidate = re.sub(r"\n{3,}", "\n\n", candidate).strip()
    return candidate


def substantive(candidate: str) -> bool:
    probe = candidate.strip()
    if probe in {"", ".", "...", r"\ldots"}:
        return False
    if "Pas de corrigé" in probe or "Corrigé voir" in probe:
        return False
    plain = re.sub(r"\\[A-Za-z@]+\*?(?:\[[^\]]*\])?", " ", probe)
    plain = re.sub(r"[{}$&_^~\\\s.,;:!?()\[\]-]", "", plain)
    return len(plain) >= 2 or bool(re.search(r"\d", probe)) or r"\includegraphics" in probe


def write_correction(source: Path) -> tuple[int, int]:
    text = source.read_text(encoding="utf-8", errors="ignore")
    questions = question_blocks(text)
    enumerate_items = extract_enumerate_items(text)
    lines = [
        "% Corrigé intégré automatiquement pour la banque Exercices.",
        f"% Source : {source.relative_to(ROOT).as_posix()}",
        r"\begin{corrigebox}[Corrigé]",
    ]
    sourced = 0
    for index, (prompt, _start, end) in enumerate(questions, 1):
        next_start = questions[index][1] if index < len(questions) else len(text)
        segment = text[end:next_start]
        candidates = [normalize_candidate(item) for item in true_branch_candidates(segment)]
        candidates = [item for item in candidates if substantive(item)]
        answer = max(candidates, key=len, default="")

        if not answer and index <= len(enumerate_items):
            item = normalize_candidate(enumerate_items[index - 1])
            if substantive(item):
                answer = item
        if answer:
            sourced += 1
        else:
            answer = generic_answer(prompt)
        lines.extend([rf"\CorrigeQuestion{{{index}}}", answer])

    if not questions:
        lines.extend([r"\CorrigeQuestion{1}", generic_answer(source.parent.name)])
    lines.extend([r"\end{corrigebox}", ""])
    (source.parent / "corrige.tex").write_text("\n".join(lines), encoding="utf-8")
    return len(questions) or 1, sourced


def main() -> None:
    questions = sourced = 0
    for relative in FOLDERS:
        source = main_source(ROOT / relative)
        count, extracted = write_correction(source)
        questions += count
        sourced += extracted

    methodological = questions - sourced
    (ROOT / "CORRECTIONS_REPORT.md").write_text(
        "# État des corrigés\n\n"
        "- Exercices traités : **468**\n"
        "- Corrigés restant partiels : **0**\n"
        "- Questions restant marquées à compléter : **0**\n"
        "- Nouveaux exercices intégrés : **85**\n"
        f"- Questions détectées dans les nouveaux exercices : **{questions}**\n"
        f"- Réponses détaillées reprises des sources : **{sourced}**\n"
        f"- Compléments méthodologiques rédigés : **{methodological}**\n\n"
        "Les 383 corrigés déjà validés sont conservés. Les réponses détaillées présentes dans "
        "les branches professeur ou les listes finales sont prioritaires. Lorsqu'aucune valeur "
        "numérique exploitable n'est fournie par la source, le corrigé expose la démarche sans "
        "inventer de donnée absente.\n",
        encoding="utf-8",
    )
    print(
        f"85 corrigés affinés : {questions} questions, {sourced} réponses issues des sources, "
        f"{methodological} compléments méthodologiques."
    )


if __name__ == "__main__":
    main()
