"""Runtime configuration for bip39chk."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class WalletConfig:
    """Local wallet settings. No remote credentials are stored."""

    network: str = "mainnet"
    rpc_endpoint: str = "offline"
    storage_dir: str = ".wallets"
    derivation_path: str = "m/44'/0'/0'"
    coin: str = "BIP39"
    address_prefix: str = "seed"

    def storage_path(self) -> Path:
        """Return the vault directory, created on first use."""
        path = Path(self.storage_dir)
        path.mkdir(parents=True, exist_ok=True)
        return path
