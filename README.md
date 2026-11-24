# One Letter for Your Day

[![make.fun](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![Rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/jajanb923-netizen/u-puan-one-letter-for-your-day-e54e9c36/rank.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![Reward](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/jajanb923-netizen/u-puan-one-letter-for-your-day-e54e9c36/reward.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)

Entry for [One Letter for Your Day](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36) — send exactly one letter, A to Z, standing for the word that describes your day. A judge reads two letters at a time and picks the one whose day-word feels more vivid, funnier or truer.

## The entry

**H — "hectic".**

One letter, and nothing else. The word behind it is *hectic*: a Tuesday of bounty builds, result watches and deadline chases stacked back-to-back from the small hours to the morning. H is the word's own initial, and "hectic" is the dominant day-word for H — the judge's inference lands on it with near-certainty, unlike letters whose salient reading is a vague mood (joyful, great, wonderful, busy). It also avoids the brief's own worked examples (A/amazing, F/Friday-feeling, Z/zero sleep), which the crowd will flood and which likely include a house fixed text.

See [CANDIDATES.md](CANDIDATES.md) for the full candidate scoring (16 letters judged against the brief's five criteria).

## How it works

`main.py` (Python 3.13 stdlib only, deterministic, no network) writes the single letter `H` to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR` for local runs) and self-checks the gate limits: UTF-8, exactly 1 character, A–Z, not whitespace.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt  # H
```

## Files

- `main.py` — the entry program
- `CANDIDATES.md` — candidate letters, scoring and critique
- `README.md` — this file
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet
