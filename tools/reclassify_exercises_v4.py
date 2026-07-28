#!/usr/bin/env python3
from __future__ import annotations

import reclassify_exercises_v3 as v3

base = v3.v2.base


def main() -> None:
    proposals = [base.classify(source) for source in base.exercise_sources()]
    resolved = [proposal for proposal in proposals if proposal.category is not None]
    unresolved = [proposal for proposal in proposals if proposal.category is None]

    if not unresolved:
        raise SystemExit("Aucun cas ambigu : utiliser l'application complète.")

    # Le seul ancien dossier autorisé à rester provisoirement est PPM.
    base.OLD_EXERCISE_ROOTS = set(base.OLD_EXERCISE_ROOTS) - {"PPM"}
    base.apply_moves(resolved)

    final_proposals = [base.classify(source) for source in base.exercise_sources()]
    base.write_report(final_proposals, applied=True)
    print(
        f"Reclassement partiel appliqué : {len(resolved)} exercices déplacés, "
        f"{len(unresolved)} exercices PPM laissés à arbitrer."
    )


if __name__ == "__main__":
    main()
