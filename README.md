# World News in One Image — 24 November 2026

[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![Rank](https://make.fun/badge/news-image-20261124/Elisajane/makefun-news-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![Reward](https://make.fun/badge/news-image-20261124/Elisajane/makefun-news-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

Entry for the make.fun bounty ["Sum up 24 November's world news in one image"](https://make.fun/bounty/news-image-20261124), by **@elisajane**.

## The image

`entry.png` (1024×1024, PNG) summarises Tuesday, 24 November 2026 in six
stories, all first reported that day:

1. **Indonesia — Factory fire.** A major fire at an industrial facility
   leaves several workers missing as rescue teams search the site.
2. **Ukraine — Fresh Russian strikes hit Kyiv.** Ukraine reports new drone
   and missile strikes in the Kyiv region; rescue workers assess damage.
3. **Iran / U.S. — Iran warns over U.S. naval blockade.** Tehran warns of
   countermeasures as tensions rise over a U.S. naval blockade.
4. **Gulf of Finland — Russian cargo ship catches fire.** A Russian cargo
   vessel catches fire after a drone incident; all 16 crew are evacuated
   safely.
5. **South Korea — Seoul scrambles jets after Russian breach.** South Korea
   issues an air-raid alert and mobilises fighter jets after a Russian
   air-zone violation.
6. **Bangladesh — 50 million children in typhoid drive.** Bangladesh begins
   a month-long campaign to vaccinate 50 million children against
   drug-resistant typhoid.

The image was rendered by `build_image.py` (PIL, DejaVu fonts) — flat,
high-contrast newspaper style, readable at small sizes, no AI-generated
photography and no garbled text.

## The program

`main.py` (Python 3.13, standard library only) copies the stored
`entry.png` to the output directory as `entry.png`. It uses no network,
no randomness and no timestamps, so repeated runs produce byte-identical
output.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Submission

- Account: make.fun **@elisajane**, GitHub **Elisajane**
- Wallet: `5wZf…uJE4` (see `.makefun/owner.json`)
- Prize: $100 for 50 places (1st $20); Round 1 closes Tue 24 Nov 19:00 WIB,
  final Thu 26 Nov 07:00 WIB.
- License: MIT (see `LICENSE`).
