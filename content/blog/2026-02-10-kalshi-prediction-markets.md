---
title: "What Kalshi's Volume Data Tells Us About Prediction Markets"
date: 2026-02-10
tags: [prediction-markets, data-viz]
description: "Sports betting dwarfs everything else on Kalshi. Here's the breakdown and what it means for the future of prediction markets."
draft: false
viz:
  - kalshi_treemap
---

Prediction markets have been around for decades in various forms, but Kalshi's CFTC-regulated exchange has brought them into the mainstream. I pulled their public volume data to see where the money actually flows.

The answer? Sports. Overwhelmingly sports.

{{viz:kalshi_treemap}}

## The Numbers

Sports betting accounts for over 73% of total notional volume on Kalshi. That's $13.18 billion in sports contracts versus $2.45 billion in politics — the next largest category.

This shouldn't be surprising. Sports betting is a massive, well-understood market with clear outcomes, frequent resolution, and deep liquidity. What's interesting is what it tells us about where prediction markets are headed.

## Why This Matters

The conventional narrative around prediction markets focuses on their potential for information aggregation — forecasting elections, economic indicators, geopolitical events. And they *are* good at that. But the volume data tells a different story about what drives adoption:

1. **Frequency matters.** Sports events happen daily. Elections happen every 2-4 years. More events = more trading opportunities = more volume.

2. **Expertise is distributed.** Millions of people have strong opinions about sports outcomes. Fewer people have informed views on Fed rate decisions.

3. **Entertainment drives liquidity.** Sports betting is *fun*. That emotional engagement creates the liquidity that makes markets efficient.

## What I'm Watching

The interesting question is whether the sports volume creates enough infrastructure and user acquisition to bootstrap the less liquid, more socially valuable markets. If Kalshi uses sports revenue to subsidize prediction markets for pandemics, climate events, and policy outcomes, that's a net positive.

I'll be tracking these numbers over time and building out more detailed breakdowns by sport and market type. Stay tuned for the next post in this series.

## Methodology

Data sourced from Kalshi's public API and aggregated by event category. Volume figures represent total notional value of contracts traded, not open interest. Data as of February 2026.
