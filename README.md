# paladin-demo

**Everything in this repository is fake.** It is a deliberately insecure demo app with synthetic data, made for
testing [Paladin / Attack Path Compiler](https://github.com/Manipal-Hackathon-2026) during the Manipal Hackathon 2026
(scans, the bug-bounty round and judging). Do not deploy it and do not reuse any of its code.

- `app/` - a tiny Flask service with intentional weaknesses (hard-coded credential, weak hashing, debug mode,
  `eval`, shell commands, SQL built from strings, TLS verification off).
- `web/` - a static page with an unsafe link and a script loaded over plain HTTP.
- `data/` - synthetic customers and log lines. Names, emails and IPs are invented
  (`example.com` addresses, documentation IP ranges 192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24).

Paladin opens pull requests with fixes on a separate `fixes` branch. `main` is never changed directly.
