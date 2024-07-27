def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"LLM Interface" in response.data

def test_generate_response(client, monkeypatch):
    class MockLangChainModel:
        def generate_response(self, prompt):
            return "Mock response"

    def mock_init(self, api_url, api_key):
        pass

    monkeypatch.setattr('app.models.LangChainModel.__init__', mock_init)
    monkeypatch.setattr('app.models.LangChainModel.generate_response', MockLangChainModel.generate_response)

    response = client.post('/api/llm/generate', json={'prompt': 'Test prompt'})
    assert response.status_code == 200
    assert response.json == {'response': 'Mock response'}
