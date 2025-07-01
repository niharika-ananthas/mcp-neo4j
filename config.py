from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import os
import dotenv

dotenv.load_dotenv()

deltails = DefaultAzureCredential()
vault_url = os.environ["vault_url"]
vault_secrets = SecretClient(vault_url=vault_url, credential=deltails)

graphdb_url = vault_secrets.get_secret("db_conncection_string")
graphdb_un = vault_secrets.get_secret("db_un")
graph_key = vault_secrets.get_secret("db_key")
llm_api_key = vault_secrets.get_secret("llm_api_key")
embedder_api_key = vault_secrets.get_secret("txt_embedder_api_key")

os.environ["db_url"] = graphdb_url.value
os.environ["db_un"] = graphdb_un.value
os.environ["db_key"] = graph_key.value
os.environ["azure_api_key"]=llm_api_key.value
os.environ["embedder_api_key"]=embedder_api_key.value
