# news-summary-01: best summary of 11 November 2026 world news

Entry for make.fun competition `news-summary-01` ($200, 20 places).
The program writes one summary, in English, of the world's news of
Wednesday 11 November 2026 to `/output/entry.txt`.

## How it works

`main.py` (Python 3.13, standard library only) copies the summary held in
`summary.txt` beside it to the output path, byte for byte. No network, no
model call, no randomness, no clock: two runs produce identical bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
python3 -c "print(len(open('out/entry.txt', encoding='utf-8').read()))"
```

## The summary

Twelve stories, ordered by importance, one or two sentences each, each with
its source named so a reader can verify it. Researched from live reporting
on 11 November 2026 (Reuters, AP, BBC, Metropolitan Police, House Clerk):
the Abu Dhabi Russia-Ukraine talks ending with a prisoner exchange agreed;
the Strait of Hormuz standoff; COP31 in Antalya; Congo's Ebola outbreak
passing 11,000 cases; US charges over Iran-backed plots; a NATO espionage
arrest in Britain; Israel's deadlocked Knesset; the Hegseth impeachment
vote; the Trump-BBC ruling; El Salvador's Haiti strike; and hot US CPI
moving markets. Claims that could not be verified are labelled as such
("claimed", "unverified", "reported"), never stated as fact.

## Files

- `main.py` - the entrypoint
- `summary.txt` - the summary (under the 2,000-character gate limit)
- `LICENSE` - MIT
- `.makefun/owner.json` - claim file naming the payout wallet

## Verification

`backtest.py` (dev only, in `~/workspace/makefun/news-backtest/`, NOT part of
the submitted repo) scores the output against the judge's published rubric:
gate, datedness, breadth, specificity, sources, hedging and tightness, and
compares it pairwise with the kit starter summary. Run it with
`python3 ~/workspace/makefun/news-backtest/backtest.py out/entry.txt`
from the repo root after generating `out/entry.txt`.
