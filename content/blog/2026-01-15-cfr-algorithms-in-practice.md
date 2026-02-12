---
title: "Counter-Factual Regret Minimization: From Poker AI to Enterprise"
date: 2026-01-15
tags: [ml-systems, counter-factual-reasoning]
description: "How I pitched and won funding for a CFR-based system at a Fortune 500, and what I learned about bringing game theory research into production."
draft: false
---

In 2019, I read the Libratus papers and became obsessed with Counter-Factual Regret Minimization (CFR). The algorithm that beat professional poker players had applications far beyond cards — any sequential decision-making problem with imperfect information was fair game.

I spent months diving deep into the theory, then did something unusual for a mid-level engineer: I pitched an R&D project to leadership to apply CFR to enterprise decision-making. They funded it.

## What is CFR?

At its core, CFR is an iterative algorithm for finding Nash equilibria in extensive-form games. In plain English: it's a way to make optimal decisions when you don't have complete information about what the other players are doing.

The key insight is *regret*. After each round, you compute how much better you *could* have done if you'd played differently. Over thousands of iterations, the strategy converges to one that minimizes this cumulative regret — and that strategy turns out to be approximately optimal.

```python
def update_strategy(regret_sum, strategy_sum):
    """Compute strategy proportional to positive regrets."""
    normalizing_sum = sum(max(r, 0) for r in regret_sum)
    if normalizing_sum > 0:
        strategy = [max(r, 0) / normalizing_sum for r in regret_sum]
    else:
        n = len(regret_sum)
        strategy = [1.0 / n] * n
    # Accumulate strategy for averaging
    for i in range(len(strategy)):
        strategy_sum[i] += strategy[i]
    return strategy
```

## From Theory to Production

The hardest part wasn't the algorithm — it was framing the problem. Enterprise stakeholders don't care about Nash equilibria. They care about costs, risks, and outcomes. I had to translate game theory into business language:

- **"Nash equilibrium"** became **"robust decision-making under uncertainty"**
- **"Regret minimization"** became **"minimizing worst-case cost overruns"**
- **"Extensive-form game"** became **"multi-stage supply chain decisions"**

The pitch worked because I could show concrete simulations: here's the current approach, here's what CFR recommends, and here's the expected cost savings across 10,000 Monte Carlo scenarios.

## Lessons Learned

1. **Research papers are necessary but not sufficient.** You need to understand the theory deeply enough to know what simplifications are acceptable for your domain.

2. **Start with the simplest possible game tree.** Our first prototype modeled a 3-stage decision with 2 choices per stage. That's only 8 terminal nodes. But it was enough to demonstrate value.

3. **Compute is not the bottleneck — data modeling is.** The hardest engineering challenge was encoding domain knowledge into the game tree structure. Getting the payoff functions right required dozens of conversations with domain experts.

4. **Management cares about confidence intervals, not point estimates.** CFR naturally gives you a distribution of strategies and outcomes. Lean into that — it's a feature, not a bug.

## What's Next

I've been exploring how CFR concepts apply to multi-agent systems and autonomous decision-making. The same framework that solves poker can inform how AI agents negotiate, bid, and cooperate. More on that in a future post.
