# OFF THE GLASS 🎾

**A padel video game that doesn't exist (yet), starring my real padel crew from India and Germany.**

Concept art for an arcade padel game: 9 players, 9 signature shots, 4 rule cards and 10 courts from Mohali to Munich. Every image was generated with **Hy-Image-3.5-preview** (Tencent Hunyuan) on **GMI Cloud** for the [Hy Image Challenge](https://www.gmicloud.ai/hy-week), Game Art track.

![Title screen](images/screens/title.jpg)

> Posted on X: [the thread](https://x.com/Ashish_Soni08/status/2105362595956068652). Should I actually build it? 👀

---

## The idea

I play padel in India and Germany with a group of friends. Padel is always played in pairs, the glass walls are part of the game, and the shots have great names. It felt made for an arcade game, so I designed one:

- **The crew**: my friends are the roster, each playing their real side of the court (right or left).
- **The Academy**: every player teaches one real padel shot, and there are cards for the key rules, including the **new 2026 Star Point**.
- **The World Tour**: 10 courts across the two countries where we play.

![In-match screen](images/screens/in-match.jpg)

## The crew

| | |
|---|---|
| ![Ashish & Katharina](images/crew/ashish-katharina.jpg) | ![Ajish & Felix](images/crew/ajish-felix.jpg) |
| ![Martha & Josephine](images/crew/martha-josephine.jpg) | ![Esther & Danny](images/crew/esther-danny.jpg) |

**Vicky, the Wildcard**, is a free agent who can pair with anyone.

![Vicky](images/crew/vicky.jpg)

## The Academy: signature shots

| Shot | What it is | Player |
|---|---|---|
| **Smash Out (x3)** | A smash so hard it bounces out over the back wall | Ashish |
| **Lob** | A high ball over the net players that sends them back | Katharina |
| **Dip** | A soft, low ball at the opponents' feet | Ajish |
| **Topspin Smash** | A heavy-topspin smash that kicks high off the glass | Felix |
| **Viper** | A slice overhead with sidespin that bites the corner | Martha |
| **Tray** | A calm overhead that keeps you at the net | Josephine |
| **Drop Shot** | The slowest shot in padel: barely over, then it dies | Esther |
| **Side-Door Smash (x4)** | A smash angled out through the side door | Danny |
| **Back-Wall Shot** | Stuck deep? Hit it into your own back glass so it bounces back over the net | Vicky |

| | | |
|---|---|---|
| ![](images/shots/smash-out.jpg) | ![](images/shots/lob.jpg) | ![](images/shots/dip.jpg) |
| ![](images/shots/topspin-smash.jpg) | ![](images/shots/viper.jpg) | ![](images/shots/tray.jpg) |
| ![](images/shots/drop-shot.jpg) | ![](images/shots/side-door.jpg) | ![](images/shots/back-wall-shot.jpg) |

## The Academy: rules

| | |
|---|---|
| ![Star Point](images/rules/rule-star-point.jpg) | ![The serve](images/rules/rule-serve.jpg) |
| ![Ground first, then glass](images/rules/rule-ground-first.jpg) | ![Let the serve bounce](images/rules/rule-serve-bounce.jpg) |

- **Star Point (new in 2026):** at 40-40 you get at most two advantages. If it's still level after that, one deciding point, the Star Point, wins the game. It replaced the old Golden Point on the FIP and Premier Padel circuits.
- **The serve:** underhand. Bounce the ball behind the service line, hit it at waist height or lower, and serve diagonally.
- **Ground first, then glass:** the ball must bounce on the floor before it touches a wall. After that, the glass is fair game.
- **Let the serve bounce:** you can volley almost anything in padel, except the serve.

## The World Tour

| India | Germany |
|---|---|
| ![Mohali](images/courts/mohali.jpg) | ![Berlin](images/courts/berlin.jpg) |
| ![Delhi](images/courts/delhi.jpg) | ![Leipzig](images/courts/leipzig.jpg) |
| ![Mumbai](images/courts/mumbai.jpg) | ![Frankfurt](images/courts/frankfurt.jpg) |
| ![Bengaluru](images/courts/bengaluru.jpg) | ![Cologne](images/courts/cologne.jpg) |
| ![Goa](images/courts/goa.jpg) | ![Munich](images/courts/munich.jpg) |

---

## How it was made

Everything was made in about a day with an AI coding agent (Claude Code) driving Hy-Image-3.5-preview through GMI Cloud's API.

1. **Rules research.** Checked the current FIP rules and the names of the main shots, so the cards teach real padel (including the 2026 Star Point and serve changes).
2. **A style lock.** Every prompt shares one style line: *"stylized cel-shaded game art, bold clean line work, polished Riot/Supercell concept-sheet quality"*. Every prompt also spells out padel details the model otherwise gets wrong: stringless rackets with holes, a fuzzy felt ball with no holes, and glass back walls with black mesh on top.
3. **Characters first.** One text-to-image character sheet per duo, plus one for Vicky: turnarounds, expressions, stats and signature shot.
4. **Reference chaining.** Those sheets were passed back in as reference images (the model takes up to 5) for every shot card, rule card and game screen, so the same 9 people appear everywhere.
5. **Courts.** 10 text-to-image environment scenes, each built around real landmarks: the Mohali cricket stadium lights, Lodhi-era tombs in Delhi, Marine Drive in Mumbai, the Frauenkirche in Munich, and so on.
6. **Fixing with edit prompts.** Typos, hair colours and wrong details were fixed by passing the image back with a plain instruction, e.g. *"change Felix's hair and beard from ginger-red to golden brown; keep everything else exactly the same."*
7. **One post-processing step.** The city banners on the court images were added with [`scripts/add_city_banner.py`](scripts/add_city_banner.py), so they sit at the same size and position on every image. All the artwork itself is Hy Image output.

### Example prompt

```text
Academy shot card from the arcade padel game "OFF THE GLASS". Dark navy background
with teal and saffron-orange accents. Small label "ACADEMY · SHOT 01". Huge bold title
"SMASH OUT (x3)". Left side: ASHISH exactly as in the first reference image, leaping
high and smashing a fuzzy yellow felt ball overhead with full power. Right side: a
simple side-view diagram of a padel court with a glowing dotted ball path: smashed
steeply down, bounces once on the far side, then flies high and OUT over the top of
the back wall, with an "OUT!" burst. Ball and racket like the second reference image.
Stylized cel-shaded game art. Spell all text exactly.
```

References: `[crew sheet, props sheet]` · size `2560x1440`

## What I learned about Hy Image 3.5 preview

**Really good at:**
- **Short on-screen text.** Titles, names, stat panels and one-line captions were spelled right almost every time.
- **Character consistency across images** when you pass in a character sheet as a reference.
- **Instruction edits.** "Change X to Y, keep everything else the same" reliably fixed typos without losing the image.
- **Painterly environments** with a strong sense of place.

**Needs help with:**
- **Sports equipment it hasn't seen much.** It kept drawing a pickleball (a ball with holes) and strung tennis rackets. Spelling out "fuzzy felt ball, no holes" and passing a props sheet as a reference fixed it.
- **Exact geometry.** Top-down court diagrams came out wrong (service boxes in the wrong place), while side views worked well.
- **Ordered sequences.** The Star Point steps came out in the wrong order until I edited the labels on their own.
- **Several people in one image.** Characters sometimes merged or showed up in the wrong half of a two-person sheet.

**Practical tips:**
- Large PNG references (about 5 MB each) caused backend errors once there were 3 or more in a request. **Downscaled JPEG references (about 200 KB each) fixed it.**
- Expect about 2 attempts per image, and review every one: small text slips are easy to miss.

## Repo contents

```
images/
  screens/   title, in-match, overview board
  crew/      5 character sheets
  shots/     9 signature-shot cards
  rules/     4 rule cards
  courts/    10 World Tour courts
scripts/
  add_city_banner.py   the only post-processing step
```

---

Made with **Hy-Image-3.5-preview** on [GMI Cloud](https://www.gmicloud.ai) × [Tencent Hunyuan](https://x.com/TencentHunyuan) for the Hy Image Challenge, September 2026.
