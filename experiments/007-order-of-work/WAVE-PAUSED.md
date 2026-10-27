# Wave main7 paused

Paused at about 2026-10-26T20:17Z because the session's usage limit was reached. The /loop was stopped too.

- Launched: 20 of 288. Finished and snapshotted: 13.
- Stopped before handing back, by the experimenter, for a reason that has nothing to do with condition (conditions are still unknown to the experimenter): main7-0c70bd, main7-cd51af, main7-ab1538, main7-ea88a8, main7-23eef7, main7-bbf04a, main7-13350d. status.py still lists them as running.
- How to treat them must be decided blind, before unblinding, and recorded in the change log. Under the pre-registered rule a trial with no result is excluded. If they are reset and rerun instead (reset_trial.py), say so in the results reply.
- Next to launch: main7-11bdfc, main7-8e1636, main7-a22a04, main7-821a53, main7-7e6b54, main7-a7187e (`python3 harness/next_trials.py main7 N`).
- Then resume the wave and the post-wave steps as in PREREGISTRATION.md.

## Resumed 2026-10-27

- The wave resumed at about 07:40Z and again at 10:17Z. The 7 stopped trials stay excluded as having no result, under the pre-registered rule. They are not rerun. This was decided blind, before any assignment was opened, and is listed in harness/agents/main7.stopped.json.
- The analysis now treats a trial scored from its live directory (no snapshot, so it never handed back) as having no result. Before unblinding, check that this set is exactly the 7 stopped trials. This is change 3 for the results' change log.
- main7-11bdfc ran from 07:40Z to 10:17Z, with gaps of up to an hour between transcript entries. It had no API-error entries and no failed tool calls, so it was kept as a normal trial. Note it in the blind review.

## Correction, 2026-10-27 at about 11:46Z (still blind)

- The pre-registration's procedure says "a trial stopped mid-run is rebuilt from its unchanged assignment (`harness/reset_trial.py`) and relaunched." The earlier decision to exclude the 7 stopped trials missed that line.
- So the 7 were rebuilt with `reset_trial.py` and relaunched at the end of the wave, as pre-registered. Their first, stopped runs are not analyzed. The first runs' agent ids are in `harness/agents/main7.stopped.json`.
- `reset_trial.py` writes each rebuild time into the assignment file, so the file's hash changed. A byte copy of the file taken just before the rebuild is kept as `harness/assignments/main7.before-reset.json` (sha256 `1da2d6ae6894d52f6bdef4417abf14b6f07a1984c98cfb1262ab2d599da1634c`). Neither file was opened.
- Change 3 to `analyze.py` stays as a safeguard: a trial with no snapshot counts as "no result". Once the reruns hand back, that set should be empty.
- `status.py` and `finished.py` now count rerun trials as launched again.
