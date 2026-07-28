#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

import reclassify_exercises_v2 as v2

original_forced_category = v2.forced_category


def forced_category(relative: Path) -> int | None | str:
    if relative.parts[0] == "A_Integrer":
        compact = v2.base.norm(relative.parent.name).replace(" ", "")
        explicit = {
            "011is": 1,
            "024produitvectoriel": 2,
            "045derivationvectorielle": 2,
            "068modelisation": 5,
            "078modelisation": 8,
            "025margesgraphiques": 6,
            "026qcmperfslci": 6,
            "034slcirapidite": 6,
            "035slcirapidite": 6,
        }
        if compact in explicit:
            return explicit[compact]
    return original_forced_category(relative)


v2.forced_category = forced_category

if __name__ == "__main__":
    v2.base.main()
