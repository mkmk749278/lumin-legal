# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

The **public legal documents for the Lumin app** — plain Markdown, no build step, no code. Published via GitHub Pages (`.github/workflows/static.yml` deploys the repo root on every push to `main`) at `https://mkmk749278.github.io/lumin-legal`.

Documents: `privacy.md`, `terms.md`, `risk.md`, `delete-account.md`, with `index.md` as the landing page.

## Why edits here matter

These URLs are load-bearing in production:

- The **Lumin app** (`mkmk749278/lumin-app`, live on Google Play) links to them from Settings → Legal (`lib/data/legal_urls.dart`) and the onboarding consent flow.
- The **Google Play listing** points at the privacy policy and account-deletion page — Play policy requires them to stay reachable and accurate.

So: never delete or rename a published file (the app and Play Console link to exact paths), and keep content in sync with what the app and engine actually do. Business-rule facts (billing model, tiers, execution paths) come from `mkmk749278/360-v2` — check `ARCHITECTURE.md` (what the system actually does — §4.4 execution and key custody, §4.7 the app), then `OWNER_BRIEF.md` / `ACTIVE_CONTEXT.md` there before changing legal claims about product behaviour (e.g. terms were corrected to the Google Play Billing two-tier model when B16 shipped).

## Conventions

- Every change ships via PR to `main` (mirrors the other repos' protocol); the Pages deploy runs automatically on merge.
- Bump the "Last updated" date in any document you materially change (and in `index.md` if the set changes).
- Substantive legal-content changes are owner-sign-off territory — propose, don't auto-merge.
