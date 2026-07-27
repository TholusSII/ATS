#!/usr/bin/env python3
r"""Crée un fichier corrige.tex par exercice et l'inclut à la fin de la source.

Les éléments existants sont extraits des branches professeur/correction. Lorsqu'une
question identique existe dans un exercice homonyme de la banque, sa réponse peut être
réutilisée avec une indication de provenance. Les réponses absentes restent signalées :
le script ne transforme jamais une hypothèse en corrigé validé.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os
import re

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "CORRECTIONS_REPORT.md"
EXPECTED_EXERCISES = 383
EXCLUDED_TOP_LEVEL = {
    ".git", ".github", "ALL_EXOS", "FULL_PDF", "Style", "framework",
    "resources", "scripts", "tools", "xx_Figures",
}
BEGIN_MARKER = "% BEGIN AUTO CORRIGE INCLUDE"
END_MARKER = "% END AUTO CORRIGE INCLUDE"
TARGET_CONDITIONALS = {r"\ifprof", r"\ifcorrection"}
TOKEN_RE = re.compile(r"\\if[a-zA-Z@]+|\\else\b|\\fi\b")
QUESTION_RE = re.compile(r"\\question\b")
EXPLICIT_ENV_RE = re.compile(
    r"\\begin\{(?:corrige|solution)\}(.*?)\\end\{(?:corrige|solution)\}",
    re.DOTALL,
)


@dataclass
class QuestionBlock:
    number: int
    prompt: str
    answer: str | None
    borrowed_from: Path | None = None


@dataclass
class ExerciseData:
    source: Path
    questions: list[QuestionBlock]


def strip_comments(text: str) -> str:
    output: list[str] = []
    for line in text.splitlines(keepends=True):
        cut = None
        for index, char in enumerate(line):
            if char != "%":
                continue
            backslashes = 0
            cursor = index - 1
            while cursor >= 0 and line[cursor] == "\\":
                backslashes += 1
                cursor -= 1
            if backslashes % 2 == 0:
                cut = index
                break
        output.append(line if cut is None else line[:cut] + ("\n" if line.endswith("\n") else ""))
    return "".join(output)


def inspect_exercise(path: Path) -> bool:
    relative = path.relative_to(ROOT)
    if len(relative.parts) < 4 or relative.parts[0] in EXCLUDED_TOP_LEVEL:
        return False
    if path.name.endswith("_old.tex") or "_Colle_" in path.name or path.name == "corrige.tex":
        return False
    content = path.read_text(encoding="utf-8", errors="ignore")
    return (
        r"\documentclass" not in content
        and (r"\exer" in content or r"\subsection*" in content)
    )


def sort_key(path: Path) -> tuple[str, ...]:
    return tuple(part.casefold() for part in path.relative_to(ROOT).parts)


def balanced_argument(text: str, start: int) -> tuple[str, int]:
    if start >= len(text) or text[start] != "{":
        return "", start
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


def extract_target_true_branches(text: str) -> str:
    r"""Conserve uniquement les branches vraies de \ifprof et \ifcorrection."""
    output: list[str] = []
    stack: list[dict[str, object]] = []
    cursor = 0

    def collecting() -> bool:
        targets = [frame for frame in stack if frame["target"]]
        return bool(targets) and all(bool(frame["active"]) for frame in targets)

    for match in TOKEN_RE.finditer(text):
        if collecting():
            output.append(text[cursor : match.start()])
        token = match.group(0)
        if token.startswith(r"\if"):
            stack.append({"target": token in TARGET_CONDITIONALS, "active": True})
        elif token == r"\else":
            if stack and stack[-1]["target"]:
                stack[-1]["active"] = not bool(stack[-1]["active"])
        elif token == r"\fi":
            if stack:
                stack.pop()
        cursor = match.end()
    if collecting():
        output.append(text[cursor:])
    return "".join(output)


def clean_answer(text: str) -> str:
    text = text.replace(r"\begin{corrige}", "").replace(r"\end{corrige}", "")
    text = text.replace(r"\begin{solution}", "").replace(r"\end{solution}", "")
    text = re.sub(r"\\marginnote(?:\[[^\]]*\])?\{[^{}]*(?:Corrig|corrig)[^{}]*\}", "", text)
    text = re.sub(r"\\(?:index|label)\{[^{}]*\}", "", text)
    text = re.sub(r"\\setcounter\{[^{}]*\}\{[^{}]*\}", "", text)
    text = re.sub(
        r"\\begin\{figure\*?\}(?:\[[^\]]*\])?",
        r"\\par\\medskip\\begin{center}\\captionsetup{type=figure}",
        text,
    )
    text = re.sub(
        r"\\end\{figure\*?\}",
        r"\\end{center}\\par\\medskip",
        text,
    )
    text = re.sub(
        r"\\begin\{table\*?\}(?:\[[^\]]*\])?",
        r"\\par\\medskip\\begin{center}\\captionsetup{type=table}",
        text,
    )
    text = re.sub(
        r"\\end\{table\*?\}",
        r"\\end{center}\\par\\medskip",
        text,
    )
    text = re.sub(r"(?m)^\s*~?\\\\\s*$", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def substantive(text: str) -> bool:
    if not text:
        return False
    if r"\includegraphics" in text or r"\begin{tikzpicture}" in text:
        return True
    probe = re.sub(r"\\[a-zA-Z@]+\*?(?:\[[^\]]*\])?", " ", text)
    probe = re.sub(r"[{}$&_^~\\]", " ", probe)
    probe = re.sub(r"\s+", " ", probe).strip()
    return len(probe) >= 18


def deduplicate(chunks: list[str]) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for chunk in chunks:
        cleaned = clean_answer(chunk)
        key = re.sub(r"\s+", " ", cleaned).strip()
        if not substantive(cleaned) or key in seen:
            continue
        seen.add(key)
        result.append(cleaned)
    return result


def normalize_prompt(prompt: str) -> str:
    prompt = re.sub(r"\\(?:label|index)\{[^{}]*\}", "", prompt)
    prompt = re.sub(r"\s+", " ", prompt).strip().casefold()
    return prompt


def parse_questions(text: str) -> list[QuestionBlock]:
    text = strip_comments(text)
    matches = list(QUESTION_RE.finditer(text))
    questions: list[QuestionBlock] = []
    for index, match in enumerate(matches):
        cursor = match.end()
        while cursor < len(text) and text[cursor].isspace():
            cursor += 1
        prompt = ""
        if cursor < len(text) and text[cursor] == "{":
            prompt, answer_start = balanced_argument(text, cursor)
        else:
            answer_start = cursor
        answer_end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        segment = text[answer_start:answer_end]
        chunks = [extract_target_true_branches(segment)]
        chunks.extend(env.group(1) for env in EXPLICIT_ENV_RE.finditer(segment))
        answers = deduplicate(chunks)
        questions.append(
            QuestionBlock(index + 1, prompt, "\n\n".join(answers) if answers else None)
        )
    return questions


def enrich_from_homonymous_exercises(exercises: list[ExerciseData]) -> int:
    """Complète les réponses strictement identiques d'exercices portant le même nom."""
    bank: dict[tuple[str, str], list[tuple[str, Path]]] = {}
    for exercise in exercises:
        system_name = exercise.source.parent.name.casefold()
        for question in exercise.questions:
            prompt = normalize_prompt(question.prompt)
            if question.answer and prompt:
                bank.setdefault((system_name, prompt), []).append(
                    (question.answer, exercise.source)
                )

    borrowed = 0
    for exercise in exercises:
        system_name = exercise.source.parent.name.casefold()
        for question in exercise.questions:
            if question.answer:
                continue
            candidates = bank.get((system_name, normalize_prompt(question.prompt)), [])
            candidates = [(answer, source) for answer, source in candidates if source != exercise.source]
            unique = {
                re.sub(r"\s+", " ", answer).strip(): (answer, source)
                for answer, source in candidates
            }
            if len(unique) == 1:
                answer, source = next(iter(unique.values()))
                question.answer = answer
                question.borrowed_from = source.relative_to(ROOT)
                borrowed += 1
    return borrowed


def relocate_borrowed_assets(answer: str, borrowed_from: Path, target_source: Path) -> str:
    """Réécrit les images relatives pour qu'elles restent accessibles après reprise."""
    source_images = (ROOT / borrowed_from).parent / "images"
    target_dir = (ROOT / target_source).parent
    relative_images = os.path.relpath(source_images, target_dir).replace(os.sep, "/")

    def replace_graphic(match: re.Match[str]) -> str:
        options = match.group(1) or ""
        filename = match.group(2)
        if filename.startswith(("/", "../", "./")) or "/" in filename:
            return match.group(0)
        return rf"\includegraphics{options}{{{relative_images}/{filename}}}"

    return re.sub(
        r"\\includegraphics(\[[^\]]*\])?\{([^{}]+)\}",
        replace_graphic,
        answer,
    )


def correction_content(relative: Path, questions: list[QuestionBlock]) -> tuple[str, str]:
    answered = sum(question.answer is not None for question in questions)
    total = len(questions)
    borrowed = sum(question.borrowed_from is not None for question in questions)
    if answered == 0:
        status = "absent"
        title = "Corrigé à rédiger"
    elif answered < total:
        status = "partiel"
        title = "Corrigé partiel extrait de la banque"
    else:
        status = "complet"
        title = "Corrigé extrait de la banque"

    lines = [
        "% Fichier généré automatiquement par tools/generate_corrections.py.",
        f"% Source : {relative.as_posix()}",
        f"% Statut : {status} ({answered}/{total} question(s) renseignée(s), {borrowed} reprise(s)).",
        rf"\begin{{corrigebox}}[{title}]",
    ]
    if total == 0:
        lines.append(
            r"\CorrigeACompleter{Aucune question n'a été détectée automatiquement dans cet exercice.}"
        )
    elif answered == 0:
        lines.append(
            r"\CorrigeACompleter{La source d'origine ne contient aucun élément de solution exploitable. "
            r"Le fichier séparé est créé afin de recevoir un corrigé pédagogique validé.}"
        )
    else:
        for question in questions:
            lines.append(rf"\CorrigeQuestion{{{question.number}}}")
            if question.answer:
                answer = question.answer
                if question.borrowed_from:
                    lines.append(
                        r"\CorrigeSource{Réponse reprise d'un exercice homonyme de la banque ; "
                        r"la provenance exacte est indiquée dans le commentaire du fichier.}"
                    )
                    lines.append(f"% Réponse reprise de : {question.borrowed_from.as_posix()}")
                    answer = relocate_borrowed_assets(answer, question.borrowed_from, relative)
                lines.append(answer)
            else:
                lines.append(
                    r"\CorrigeACompleter{Aucun élément de réponse n'est présent dans la source d'origine "
                    r"pour cette question.}"
                )
    lines.extend([r"\end{corrigebox}", ""])
    return "\n".join(lines), status


def append_include(source: Path) -> None:
    text = source.read_text(encoding="utf-8")
    pattern = re.compile(
        re.escape(BEGIN_MARKER) + r".*?" + re.escape(END_MARKER), re.DOTALL
    )
    text = pattern.sub("", text).rstrip()
    include = (
        f"\n\n{BEGIN_MARKER}\n"
        r"\InclureCorrige{corrige.tex}" + "\n"
        f"{END_MARKER}\n"
    )
    source.write_text(text + include, encoding="utf-8")


def main() -> None:
    sources = sorted(
        (path for path in ROOT.rglob("*.tex") if inspect_exercise(path)),
        key=sort_key,
    )
    if len(sources) != EXPECTED_EXERCISES:
        raise SystemExit(
            f"Nombre d'exercices inattendu : {len(sources)} (attendu : {EXPECTED_EXERCISES})."
        )

    exercises = [
        ExerciseData(source, parse_questions(source.read_text(encoding="utf-8", errors="ignore")))
        for source in sources
    ]
    borrowed = enrich_from_homonymous_exercises(exercises)

    statuses: dict[str, list[str]] = {"complet": [], "partiel": [], "absent": []}
    for exercise in exercises:
        relative = exercise.source.relative_to(ROOT)
        content, status = correction_content(relative, exercise.questions)
        (exercise.source.parent / "corrige.tex").write_text(content, encoding="utf-8")
        append_include(exercise.source)
        statuses[status].append(relative.as_posix())

    report = [
        "# État des corrigés",
        "",
        f"- Exercices traités : **{len(exercises)}**",
        f"- Corrigés complets : **{len(statuses['complet'])}**",
        f"- Corrigés partiels : **{len(statuses['partiel'])}**",
        f"- Corrigés absents et fichiers créés : **{len(statuses['absent'])}**",
        f"- Réponses reprises d'exercices homonymes : **{borrowed}**",
        "",
        "Les reprises ne sont effectuées que lorsque le nom du système et le texte de la question "
        "sont identiques et qu'une réponse unique existe dans la banque.",
        "",
        "Les fichiers `corrige.tex` marqués *à rédiger* sont des emplacements explicites ; "
        "ils ne sont pas présentés comme des solutions validées.",
        "",
    ]
    for status, title in (("partiel", "Corrigés partiels"), ("absent", "Corrigés à rédiger")):
        report.extend([f"## {title}", ""])
        report.extend(f"- `{path}`" for path in statuses[status])
        report.append("")
    REPORT.write_text("\n".join(report), encoding="utf-8")
    print(
        f"{len(exercises)} fichiers corrige.tex créés : "
        f"{len(statuses['complet'])} complets, "
        f"{len(statuses['partiel'])} partiels, "
        f"{len(statuses['absent'])} absents, {borrowed} réponses reprises."
    )


if __name__ == "__main__":
    main()
