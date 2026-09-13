# bip39-checksum

> bip39 · checksum · 12/24

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-3776AB)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Build](https://img.shields.io/badge/build-passing-brightgreen)]()

BIP39 checksum helper — generate and validate a local word list.

## Features

- HD derivation along m/44'/0'/0' for BIP39
- Passphrase-wrapped vault stored as local JSON
- Deterministic address codec (SHA-256 simulation, no live keys)
- Fee estimator with low / medium / high presets
- Balance sync against a stub RPC client
- Click CLI with vault, account and portfolio commands

## Prerequisites

- Python 3.11+
- Git

## Getting Started

```bash
git clone <repo-url>
cd bip39-checksum
python -m pip install -e .
python -m bip39chk --help
```

## CLI Usage

```bash
bip39chk create-vault --name "Main"
# Create an encrypted local vault

bip39chk list-vaults
# List vault files in the storage directory

bip39chk add-account --label Savings
# Derive the next HD account

bip39chk sync
# Refresh stub balances

bip39chk balance
# Print account table

bip39chk portfolio
# Show coin + stub USD total
```

## Project Structure

```
bip39chk/
  crypto/          seed, derive, address
  chain/           stub RPC and fee table
  storage/         vault JSON
  services/        wallet + sync
  cli.py           click entry
tests/             pytest
```

## Configuration

Defaults live in `bip39chk/config.py` (`WalletConfig`).

| Setting | Default | Description |
|---------|---------|-------------|
| `network` | `mainnet` | mainnet / testnet |
| `rpc_endpoint` | `offline` | BIP39 node URL (unused in stub mode) |
| `storage_dir` | `.wallets` | Local vault directory |
| `derivation_path` | `m/44'/0'/0'` | BIP path |

## Tests

```bash
python -m pytest -q
```

## Background

Recovery macros link checksum, not another seed-phrase-tool.

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.


---

## Topics

![bip39](https://img.shields.io/badge/bip39-111827?style=flat-square) ![checksum](https://img.shields.io/badge/checksum-111827?style=flat-square) ![bip39-checksum](https://img.shields.io/badge/bip39%20checksum-111827?style=flat-square) ![cryptocurrency](https://img.shields.io/badge/cryptocurrency-111827?style=flat-square) ![wallet](https://img.shields.io/badge/wallet-111827?style=flat-square) ![blockchain](https://img.shields.io/badge/blockchain-111827?style=flat-square) ![web3](https://img.shields.io/badge/web3-111827?style=flat-square) ![bitcoin](https://img.shields.io/badge/bitcoin-111827?style=flat-square)

`bip39` `checksum` `bip39-checksum` `cryptocurrency` `wallet` `blockchain` `web3` `bitcoin` `ethereum` `hd-wallet` `open-source` `python`

Search: bip39-checksum · bip39 · checksum · 12/24 · BIP39 checksum helper — generate and validate a local word list.

---

<sub>BIP39 checksum helper — generate and validate a local word list.</sub>
