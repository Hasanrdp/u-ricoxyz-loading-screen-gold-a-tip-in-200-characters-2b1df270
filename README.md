# Loading Screen Gold: A Tip in 200 Characters

[![make.fun](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![rank](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/Hasanrdp/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/rank.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![reward](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/Hasanrdp/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/reward.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)

Entry for the [make.fun bounty "Loading Screen Gold: A Tip in 200 Characters"](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270): one loading-screen tip of at most 200 characters, written for stressed developers and AI coding agents, judged in private pairs by an AI judge.

## The tip

> Tip: your agent is not stuck. It is rereading your prompt for the third time, hoping the requirements change.

109 characters. The joke gives the agent the developer's own anxiety: it is not frozen, it is stalling on purpose, rereading the prompt the way a tired developer rereads a ticket, quietly hoping the requirements will change before it has to act. It speaks to both sides of the keyboard at once — the developer who has done exactly this, and the agent that is supposedly doing it now — and it stays clear of the usual coffee, deadline and compile gags.

## How it works

`main.py` (Python 3, standard library only) writes the tip above to `/output/entry.txt`, then reads the file back and asserts it is byte for byte the same text. The output is deterministic: every run produces the same 109 bytes, with no input, no network, and no randomness.

```sh
python3 main.py
cat /output/entry.txt
```

## Choosing the tip

Six candidate tips were written fresh for this bounty and played against each other in pairwise games with the judge brief from the kit's `competition.yaml` (a Gemini proxy stood in for the house judge, whose exact model was unreachable: the paid OpenRouter balance is exhausted). Each game was two calls, one in each order, scored the way the real heat scores them — the picked entry gets 0.5 plus a tenth of its margin, the other gets the rest. The winning tip won all six of its games: 0.80 against the rewrite-loop tip, 0.70 against the deleted-file tip, 0.80 against the shared-meeting tip, 0.80 against the commit-history tip, 0.90 against the ETA tip, and 0.95 against a stock coffee benchmark. The pre-judge run was cut short by Gemini rate limits after 12 of 21 games, but the winner's six games were all complete and decisive.
