import pynecone as pc

config = pc.Config(
    app_name="credit_card_selector",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
