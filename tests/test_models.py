from app.models import LangChainModel

def test_generate_response(monkeypatch):
    class MockHuggingFaceEndpoint:
        def generate(self, prompt):
            return "Mock response"

    def mock_init(self, api_url, api_key):
        self.llm = MockHuggingFaceEndpoint()

    monkeypatch.setattr('app.models.LangChainModel.__init__', mock_init)

    model = LangChainModel(api_url='dummy_url', api_key='dummy_key')
    response = model.generate_response('Test prompt')
    assert response == "Mock response"
