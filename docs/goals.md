# Back-end design goals

- Target: small self-hosted user base
  - Expect less than 10 users per instance
  - No need for object storage / replication / etc.
  - Federation: not needed right now, but maybe ActivityPub if use case arises.
- Must handle multiple devices editing offline in parallel
  - Possibility: data as git repository (see [Jami Swarm](https://docs.jami.net/en_US/developer/jami-concepts/swarm.html))
  - Transaction data in git commits, no files (makes merges conflict-free)
  - Graph ordered by insertion date (not transaction date), ordered at load/display time
- All edits must be cryptographically signed
  - Maybe use GPG with elliptic curves?
  - Each device has its own private key (public key known by the server) and signs its own transactions (maybe resigned by the server when rebasing)
  - Data encryption at rest: not needed right now, maybe as a future improvement.
- Plain-text output/export must be supported (ledger/beancount syntax?)
- Plain-text input/import must be supported
