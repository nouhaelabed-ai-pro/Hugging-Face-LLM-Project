from langchain_huggingface import HuggingFaceEndpoint

class LangChainModel:
    def __init__(self, repo_id, api_key):
        self.llm = HuggingFaceEndpoint(repo_id=repo_id, api_key=api_key)

    def generate_response(self, prompt):
        return self.llm.invoke(prompt)
