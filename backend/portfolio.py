import pandas as pd
import chromadb
import uuid
from chromadb.config import Settings

class Portfolio:
    def __init__(self, file_path="resources/my_portfolio.csv"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)

        settings = Settings() 
        self.chroma_client = chromadb.PersistentClient(path='vectorstore', settings=settings)
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        if not self.collection.count():
            for _, row in self.data.iterrows():
                techstack = str(row.get("Techstack", "")).strip()
                links = str(row.get("Links", "")).strip()
                if not techstack:
                    continue
                self.collection.add(
                    documents=[techstack],
                    metadatas=[{"links": links}],
                    ids=[str(uuid.uuid4())]
                )

    def query_links(self, skills):
        if not skills:
            return []
        result = self.collection.query(query_texts=skills, n_results=2)
        metadatas = result.get("metadatas", [])
        flattened = []
        for entry in metadatas:
            if isinstance(entry, list):
                for sub in entry:
                    if isinstance(sub, dict):
                        flattened.append(sub)
            elif isinstance(entry, dict):
                flattened.append(entry)
        return flattened
