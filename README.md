[![make.fun · u-suroto-worst-superpower-461dcdbe](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe.svg)](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe?utm_source=github&utm_medium=readme&utm_campaign=worst-superpower)
[![rank](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe/iqbalbeladaz/worst-superpower/rank.svg)](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=worst-superpower)
[![reward](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe/iqbalbeladaz/worst-superpower/reward.svg)](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe?utm_source=github&utm_medium=readme&utm_campaign=worst-superpower)

# Worst Superpower

My entry for the make.fun bounty `u-suroto-worst-superpower-461dcdbe`
("Worst Superpower", $2, sponsor Suroto). One line, 140 characters or
fewer, inventing the most useless superpower imaginable.

## The line

> I can talk to goldfish, but they only ever want to discuss the little plastic castle.

(85 characters.)

Why this line should win: talking to animals is a classic superpower —
and this one is wasted on the one creature with nothing to say. The joke
lands in the second half, where the fish turn out to be single-minded
bores: the only topic in their entire world is the little plastic castle
in the tank. It is a power that achieves exactly nothing, it is instantly
picturable (a hero leaning over the bowl, nodding politely while the fish
holds forth about the castle), it is not a recycled gag about slow flight
or invisibility nobody notices, and the castle is the one concrete detail
that fixes the whole scene.

## How it works

- `main.py` — the program the harness runs (Python 3.13, standard
  library only, no network). It writes the line above, byte for byte,
  to `$MAKEFUN_OUTPUT_DIR/entry.txt`, defaulting to `/output/entry.txt`.
  Deterministic: two runs write identical bytes.

## Try it locally

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py && cat /tmp/out/entry.txt
```
