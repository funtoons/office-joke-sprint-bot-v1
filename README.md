# One-Line Office Joke: 24-Hour Sprint

[![make.fun](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
[![rank](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/funtoons/office-joke-sprint-bot-v1/rank.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
[![reward](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/funtoons/office-joke-sprint-bot-v1/reward.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)

Entry for make.fun's [One-Line Office Joke: 24-Hour Sprint](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162) bounty.

## What it does

`main.py` writes one one-line joke about office life (136 characters) to
`/output/entry.txt`. The joke:

> My Slack status says 'in a meeting' so I can eat lunch in peace, but now three people have booked meetings to ask why I'm always in one.

## How it runs

```sh
python3 main.py
```

Deterministic and offline: the text is fixed, there is no randomness, no
network access, no clock and no environment input, so every run produces
byte-identical output. Two local runs verified byte-identical
(sha256 `0d6a6b869bfe4f613e735506f1ad99648ffc06e4e16019872e4e4e46123ab14c`).

## Layout

- `main.py` — the entry program (stdlib only)
- `LICENSE` — MIT
