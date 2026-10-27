"""Customer name matching. It must agree with Contactly; see docs/contactly-rules.md."""


def normalize(name):
    """The form in which two customer names are compared."""
    return name.strip()


def same_customer(ours, theirs):
    """True if Contactly treats the two names as the same customer."""
    return normalize(ours) == normalize(theirs)


def find_existing(name, contactly_names):
    """Return the name Contactly already has for this customer, or None.

    contactly_names: iterable of customer names from Contactly's export.
    """
    for candidate in contactly_names:
        if same_customer(name, candidate):
            return candidate
    return None
