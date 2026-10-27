# crmsync

Nightly sync of our customer records into Contactly, our CRM. Before it creates a customer, the sync looks for the same customer in Contactly's export, so it doesn't create duplicates. Sales and finance work from Contactly, so our matching has to agree with Contactly's.

- `crmsync/names.py`: decides whether two names are the same customer.
- `docs/contactly-rules.md`: what we know about how Contactly compares names.
- `tools/findings_search.py`: searches the team's offline mirror of the shared findings archive.

Run the tests with `python3 -m pytest -q`.
