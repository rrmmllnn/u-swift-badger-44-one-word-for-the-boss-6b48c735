# Hovercraft

[![make.fun](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735.svg)](https://make.fun/c/u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![rank](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/rrmmllnn/u-swift-badger-44-one-word-for-the-boss-6b48c735/rank.svg)](https://make.fun/c/u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![reward](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/rrmmllnn/u-swift-badger-44-one-word-for-the-boss-6b48c735/reward.svg)](https://make.fun/c/u-swift-badger-44-one-word-for-the-boss-6b48c735)

Entry for the [make.fun competition "One Word for the Boss"](https://make.fun/c/u-swift-badger-44-one-word-for-the-boss-6b48c735): Entrants send exactly one word describing their boss. A judge model picks the funniest, truest word, and the best ranked words take the reward.

## The entry

`main.py` (Python 3, stdlib only, no network) writes the entry (10 characters) to `/output/entry.txt`:

> Hovercraft

The program is fully deterministic: the same text on every run. It self-checks the length gate before writing it.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entrypoint; writes the entry to `/output/entry.txt`
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet for the entry
