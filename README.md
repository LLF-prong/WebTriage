# GuardGate

**Prompt-injection detection and defense gateway for LLM applications.**

[中文说明](README.zh-CN.md) · [Apache-2.0](LICENSE)

GuardGate sits between your application and the model. It inspects user input
and every retrieved context chunk before they reach the LLM, and audits the
model's output before it reaches the user.

> **Status: pre-alpha.** This is a scaffold. Nothing in here is production
> ready yet — see the [roadmap](#roadmap).

## Why

Applications built on large language models have a structural weakness: the
model cannot reliably distinguish instructions written by the developer from
text that merely *looks* like instructions. Two attack families follow from
this.

**Direct injection** — the user types an instruction designed to override the
system prompt ("ignore all previous instructions and ...").

**Indirect injection** — the malicious instruction is planted somewhere the
application will later retrieve and paste into the prompt: a web page, a PDF,
an email, a support ticket, a code comment. The user never types it; the
application delivers it.

Indirect injection is the harder problem and the one this project targets.
Most existing scanners inspect the final assembled prompt, where a single
malicious sentence is diluted among thousands of tokens of legitimate context.
GuardGate scores each retrieved chunk on its own, *before* assembly, and
aggregates those scores into a decision.

## How it works

```
                 user input ──┐
                              ├──► [ input layer ]  direct injection / jailbreak
   retrieved chunks ──────────┤
                              ├──► [ context layer ] per-chunk injection score  ◄── the interesting part
                              │
                              └──► [ decision layer ] allow / sanitize / block
                                        │
                                        ▼
                                     the model
                                        │
                                        ▼
                              [ output layer ]  PII leak / system-prompt leak
```

Every decision is written to a structured audit log, because a gateway that
blocks traffic without explaining itself is not deployable.

## Design goals

1. **Per-chunk scoring.** Catch injected instructions before they are buried
   in a long context window.
2. **Latency honesty.** A defense that adds 3 seconds to every request will be
   turned off. Cascaded rules-then-model inference keeps the common path cheap,
   and we publish the latency numbers rather than hiding them.
3. **Measured, not asserted.** Every claim in this repository should be backed
   by a reproducible evaluation. Detection rate alone is meaningless — false
   positives are what get a security control removed.
4. **Runs on a laptop.** The target development environment is a single 8 GB
   consumer GPU. No cluster required.

## Roadmap

| Version | Scope | Status |
|---|---|---|
| v0.1 | Project scaffold; dataset schema; baseline scan of public inputs | 🚧 in progress |
| v0.2 | Chinese indirect-injection dataset v1 with a published taxonomy | planned |
| v0.3 | LoRA-tuned classifier, cascaded with a rules layer | planned |
| v0.4 | HTTP gateway (FastAPI) with an OpenAI-compatible proxy endpoint | planned |
| v0.5 | Evaluation harness: detection rate, false-positive rate, latency, robustness | planned |
| v1.0 | Documented, tested, reproducible release | planned |

## Getting started

Not usable yet. Once v0.1 lands:

```bash
git clone https://github.com/LLF-prong/guardgate.git
cd guardgate
python -m venv .venv
.venv/Scripts/activate     # Windows
pip install -e ".[dev]"
pytest
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Issues and pull requests are welcome,
including small ones — typo fixes and added test cases are genuinely useful at
this stage.

## License

[Apache-2.0](LICENSE).
