from pydantic_settings import BaseSettings, SettingsConfigDict


class OllieSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    OPENAI_API_KEY: str | None = None
    OLLIE_MODEL: str = "astra-research-preview"
    LEAN_PROJECT: str = "./formal/ollie"
    OLLIE_SOLANA_ADDRESS: str = "AgTeY89y1cfPxn5t5fxY6quWW4cjsi937LzTma5zJtuZ"
    OLLIE_EVM_ADDRESS: str = "0x1e370583abaD95Fb641592b2FDD071ed5b525D01"
    SOLANA_RPC_URL: str = "https://api.devnet.solana.com"
    EVM_RPC_URL: str = "https://sepolia.base.org"
    REQUIRE_LEAN_VERIFICATION: bool = True
    REQUIRE_HUMAN_SIGNOFF: bool = True
    REQUIRE_REPRODUCTION_FOR_BOUNTY: bool = True
    MAINNET_ENABLED: bool = False
    LOG_LEVEL: str = "info"
    LEDGER_DIR: str = "./.data/ledger"


def load_settings() -> OllieSettings:
    return OllieSettings()
