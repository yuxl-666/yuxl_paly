import getpass
import os

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
#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