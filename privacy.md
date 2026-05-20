# Privacy Policy

**Effective date:** 2026-05-20
**Last updated:** 2026-05-20

This Privacy Policy explains how Lumin ("we", "us") collects, uses, stores, and protects information when you use the Lumin Android application (the "App") and the related signal-delivery services (the "Service"). By using the App you consent to the practices described below.

## 1. Who we are

Lumin is operated by an individual developer based in India. The App and Service are provided as a personal project; there is no incorporated company at this time. For all privacy inquiries, data deletion requests, or other matters under this policy, contact **mulakapati446@gmail.com**.

## 2. Information we collect

We collect only the information needed to operate the App and Service:

### 2.1 Account information
- Mobile phone number — used for sign-in via Firebase Authentication (OTP-based).
- Display name, country, timezone, preferred currency — collected during sign-up to personalise the App.
- Telegram chat identifier — when you subscribe to the paid signal channel, your Telegram account ID is linked to your Lumin account so we can deliver signals.

### 2.2 Binance API key information *(only if you opt into auto-execution)*
If — and only if — you choose to enable server-side auto-execution on your Binance Futures account, you provide us a Binance API key. This key:

- Must be **trade-enabled** (for placing futures orders)
- Must have **withdrawals DISABLED** (our connect-time validation rejects keys with withdrawals enabled)
- Must be **IP-whitelisted** to our execution server

We **never** receive or store funds, custody assets, or hold private keys to any wallet. Your funds remain in your Binance account at all times. The API key is a revocable trade-authorisation token, not a custody instrument.

The API key is encrypted using Google Cloud KMS envelope encryption at the point of receipt, and is only decrypted in-memory by an isolated signing service when placing a single order on your behalf. Plaintext keys are never written to disk, logs, or error traces.

### 2.3 Trading activity
- Signals dispatched to you, with outcome (placed / rejected / skipped) and the exchange's error code if rejected.
- Per-user preferences: position notional, leverage cap, max concurrent positions, symbol allowlist.
- Order placement events: timestamp, symbol, direction, qty, status.

### 2.4 Technical information
- App version, Android version, device locale.
- Approximate region (derived from your IP address at the API server) — used to enforce regional availability of the auto-execution feature.
- Crash reports and basic usage analytics via Firebase Crashlytics.

### 2.5 What we DO NOT collect
- Your Binance password or 2FA codes (we never see these — you create the API key on Binance directly).
- Wallet private keys or seed phrases.
- Precise device location.
- Contacts, call history, SMS messages.
- Photos, files, or other on-device content beyond what you explicitly enter into the App.

## 3. How we use the information

- **Account information** — to authenticate you, deliver signals to your Telegram, and provide customer support.
- **Binance API key** — exclusively to place orders matching dispatched signals on your account, with per-user safety caps (symbol allowlist, position notional cap, rate limits, global kill switch).
- **Trading activity** — to surface the Recent Activity card in the App, debug issues, and generate the aggregate signal-quality reports we use to improve the Service.
- **Technical information** — to detect crashes, debug platform-specific issues, and enforce regional availability per Section 9.

We do **not** use your personal information for advertising, do not sell it to third parties, and do not share it with marketing networks.

## 4. Legal basis (GDPR / UK GDPR)

Where you are located in the UK or EU, our legal bases for processing are:
- **Performance of a contract** — most processing (delivering signals, executing orders) is necessary to provide the Service you signed up for.
- **Consent** — the consent gate inside the App captures your affirmative consent to first-launch terms; you may withdraw consent by deleting your account.
- **Legitimate interest** — crash reporting and basic usage analytics, balanced against your privacy.

## 5. Sharing your information

We share information with the following processors only to the extent necessary:

- **Google (Firebase Auth, Crashlytics, Cloud KMS, Cloud Firestore)** — authentication, crash reporting, encryption-key management, encrypted-key blob storage.
- **Binance** — order placement against your account (using the API key you provided).
- **Telegram** — signal delivery to your Telegram account.

We do not share your information with any other third party except where legally compelled (e.g. valid court order).

## 6. Data retention

- **Account information** — retained while your account is active; deleted within 30 days of account deletion request.
- **Binance API key** — deleted immediately upon account deletion or upon disconnection via the in-app "Disconnect Binance" action.
- **Trading activity history** — retained for 12 months from event date for audit purposes; aggregated thereafter (no per-user identifiability).
- **Crash reports** — retained for 90 days by Firebase Crashlytics.

## 7. Your rights

You may exercise the following rights:

- **Access** — request a copy of the personal data we hold about you.
- **Correction** — request correction of inaccurate data.
- **Deletion** — request deletion of your account and associated data, either via the **Settings → Delete account** option in the App or by emailing mulakapati446@gmail.com. The in-app option performs the deletion immediately; email requests are completed within 30 days.
- **Portability** — request a machine-readable export of your data.
- **Object** — object to processing based on legitimate interest.

If you are in the UK or EU, you also have the right to lodge a complaint with your national data protection authority.

## 8. Security

We follow industry-standard practices:

- All network traffic uses TLS 1.2+.
- Binance API keys are encrypted with Google Cloud KMS (envelope encryption); plaintext keys never persist to disk and never appear in logs or error traces.
- The signing service that decrypts keys to place orders is isolated on its own Unix socket and is the only process with KMS Decrypt permission.
- Per-user blast-radius caps (symbol allowlist, position-size cap, rate limit, global kill switch) bound damage in the unlikely event our infrastructure is compromised.

No security measure is perfect. You are responsible for the security of your own Binance account — including ensuring the API key you provide has withdrawals disabled and IP whitelisting enabled.

## 9. Regional availability

The auto-execution feature is enabled only in selected regions to comply with local financial regulations. As of this policy's effective date, auto-execution is available in **India, the United Kingdom, and the European Union**. It is NOT available in the United States, China, or Bangladesh. The signals-viewer feature is available in all regions where the App is distributed via Google Play.

## 10. Children

The App is intended for users aged 18 and older. We do not knowingly collect information from children under 18. If you believe a child under 18 has provided us with personal information, contact us and we will delete it.

## 11. Changes to this policy

We may update this Privacy Policy from time to time. The "Last updated" date at the top reflects the most recent change. Material changes will be notified to users via the App's consent gate (you will be re-prompted to acknowledge the updated terms before continuing).

## 12. Contact

For all privacy inquiries, including data access / correction / deletion requests:

**mulakapati446@gmail.com**
