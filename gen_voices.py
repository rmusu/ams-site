# Generates the film's neural voiceover clips into ./voice/vNN.mp3
# One-off tool (no build step for the site itself). Requires internet.
#
#   pip install edge-tts
#   python gen_voices.py
#
# Voice options (very natural, free, Microsoft neural):
#   en-US-AndrewNeural  – warm male, default
#   en-US-AriaNeural    – clear female
#   en-GB-RyanNeural    – British male
#   en-GB-SoniaNeural   – British female
# To change voice: edit VOICE below and re-run (overwrites the mp3s).
import asyncio
import pathlib

import edge_tts

VOICE = "en-US-AndrewNeural"
RATE = "-4%"   # a touch calmer than default

# MUST stay in sync with LINES in video.html (index = file number)
LINES = [
    "Three organisations. Seventy rooms. One hundred requested.",
    "Here is how the acmOS engine decides — and how you stay in charge.",
    "Each organisation submits what it needs. A wants forty rooms, B thirty, C thirty.",
    "One hundred requested, seventy available. Someone decides — the question is how.",
    "The engine weighs four things, and you control all of them.",
    "Your ranking: who is served first. Never first come, first served.",
    "Entitlements: a hard cap on what each organisation may draw.",
    "Group blocks: rooms reserved per client group. Nobody crosses them.",
    "And the fairness floor: a guaranteed share for everyone, before winners win.",
    "Pass one. Every organisation is guaranteed thirty percent of its own request.",
    "Twelve, nine, and nine rooms are locked in. Forty remain.",
    "Pass two. Above the floor, your ranking rules the top-ups.",
    "A is first: topped up to all forty rooms. Full.",
    "B gets twelve more — and the inventory runs dry at twenty-one.",
    "C keeps its guaranteed nine. Nobody leaves with zero.",
    "Without the floor? Pure ranking. A takes forty, B takes thirty, and C gets nothing.",
    "With acmOS, scarcity is a policy you set — not an accident of timing.",
    "The result is a proposal, with a reason on every line. Not a decision.",
    "Disagree with a line? Move it.",
    "Approve what convinces you — and only then, allocate.",
    "Only your approval writes to the ledger: named, timestamped, auditable.",
    "acmOS. The engine proposes. Your team decides.",
]


async def main() -> None:
    out = pathlib.Path(__file__).parent / "voice"
    out.mkdir(exist_ok=True)
    for i, text in enumerate(LINES):
        path = out / f"v{i:02d}.mp3"
        await edge_tts.Communicate(text, VOICE, rate=RATE).save(str(path))
        print(f"ok v{i:02d}  {text[:52]}")
    print(f"\n{len(LINES)} clips in {out} — commit the voice/ folder and push.")


if __name__ == "__main__":
    asyncio.run(main())
