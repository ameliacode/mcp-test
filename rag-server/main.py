import logging
import os

from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO)

mcp = FastMCP("PDF-RAG")

PDF_PATH = os.path.join(os.path.dirname(__file__), "스마트팜.pdf")
loader = PyPDFLoader(PDF_PATH)
pages = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.split_documents(pages)

embeddings = OpenAIEmbeddings()
llm = ChatOpenAI(model="gpt-5")
vectorstore = Chroma.from_documents(docs, embeddings)
qa_chain = RetrievalQA.from_chain_type(llm, etriever=vectorstore.as_retriever())


@mcp.tool()
def ask_pdf(query: str) -> str:
    logging.info(f"Received query: {query}")
    return qa_chain.run(query)


if __name__ == "__main__":
    mcp.run(transport="stdio")
