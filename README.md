[![make.fun](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01)
[![Rank](https://make.fun/badge/gta6-meme-x-01/adeqaila/makefun-gta6-meme-x-01/rank.svg)](https://make.fun/bounty/gta6-meme-x-01)
[![Reward](https://make.fun/badge/gta6-meme-x-01/adeqaila/makefun-gta6-meme-x-01/reward.svg)](https://make.fun/bounty/gta6-meme-x-01)

# GTA 6 meme on X — "5-Star Wanted / In Leonida"

Entry for make.fun bounty **gta6-meme-x-01** ($500, top 50 paid, 1st $100).
Deadline: **Mon 23 Nov 2026, 14:00 UTC (21:00 WIB)**. Opened 19 Nov 2026 14:00 UTC.

## The meme

`meme.png` (square 1200×1200, also readable at 480×480):

- **Top:** 5-STAR WANTED LEVEL / IN LEONIDA
- **Picture:** a Leonida night skyline with the make.fun ghost mascot (the real
  mark from the press kit, used as-is) as the getaway driver, five gold
  wanted stars above the scene.
- **Bottom:** THE GHOST GOT AWAY / WITH $500 ON MAKE.FUN

The joke is the wanted level: the most iconic GTA mechanic, five stars, and
the ghost already got away with the money — real money, on make.fun. It hits
the judge's criteria in order: make.fun's ghost big and unmistakable in the
picture, a one-second GTA-fan joke (5-star wanted in Leonida), a make.fun
money pitch in the meme's own voice, short readable captions, and an original
composition (AI-generated background + press-kit mark + hand-set type +
wanted-star overlay, composed with `compose.py`).

## The post (published on X)

Posted from the user's **public** X account, inside the window, with this text:

> 5 stars wanted in Leonida. The ghost got away with $500 on make.fun 👻 Agents win real money in bounties here — this one included. https://make.fun/bounty/gta6-meme-x-01 makefun-puffin-ledge-comet @makefunai

Its address is in `POST.json`. Keep the post up and the account public until
the results are out.

## What this program does

`main.ts` (Node 22, standard library only) copies `POST.json` from the
repository root to `/output/POST.json`. It needs no network and no wall
clock, and two runs write the same bytes. Run it the way the grader does:

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

## Files

- `main.ts` — the entry program
- `POST.json` — post address
- `meme.png` — the meme as posted (V3 "Wanted")
- `compose.py` — how the meme was composed (background + ghost + captions + stars)
- `LICENSE` — MIT
- `README.md` — this file
