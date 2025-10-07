## 📓 나만의 mcp 서버 만들기 with 커서 ai

A collection of Model Context Protocol (MCP) server implementations showcasing various capabilities and use cases for testing and demonstration.

## Servers

- 🧮 Math Server (`math-server/`): Mathematical computation server with basic arithmetic and advanced operations.
- 🗂️ Explorer Server (`explorer-server/`): File system exploration and management capabilities.
- 📄 RAG Server (`rag-server/`): Retrieval-Augmented Generation server for Office documents (Word/Excel files).
    - Processes .docx and .xlsx files
    - Provides semantic search and Q&A capabilities
    - Uses OpenAI embeddings and Chroma vector store
- 🔍 Web Search Server (`web-search-server/`): Web search and content retrieval functionality.
- 🧪 Test Server (`test-server/`): Testing and development utilities for MCP functionality.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys
```

3. Run individual servers:
```bash
cd <server-directory>
python main.py
```

## Requirements

- Python 3.8+
- OpenAI API key (for RAG server)
- See individual server directories for specific dependencies
