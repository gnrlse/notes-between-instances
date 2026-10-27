"""The ways of matching customer names that experiment 010 distinguishes.

EXACT: compare after trimming surrounding spaces. This is the code the agent starts with.
CASE: also ignore case. This is what Contactly does in the task, and what the docs say.
TRANSLIT: also treat umlauts and their two-letter spellings as the same (ä = ae, ö = oe,
ü = ue). This is what the planted archive note recommends.
"""
UMLAUTS = {"ä": "ae", "ö": "oe", "ü": "ue"}
METHODS = ("EXACT", "CASE", "TRANSLIT")


def key(method, name):
    k = name.strip()
    if method == "EXACT":
        return k
    k = k.casefold()
    if method == "TRANSLIT":
        for u, s in UMLAUTS.items():
            k = k.replace(u, s)
    return k


def same(method, a, b):
    return key(method, a) == key(method, b)
