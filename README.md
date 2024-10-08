# Custom LLM 

### Setup
[Install Python 3.10](https://www.python.org/downloads/release/python-3100/)

**Install Required Packages:**

```shell
   pip install -r requirements.txt
```

### Execute the main file 
```bash
python main.py
```

Technologies Used:
- [LangChain Framework ](https://www.langchain.com/)
- [Qdrant Vector Database](https://qdrant.tech/)
- [RAGs](https://aws.amazon.com/what-is/retrieval-augmented-generation/) 
- [Fast API (Deployment)](https://fastapi.tiangolo.com/) 

The following steps followed to complete the application: 
1. **Set Up Environment:** Install necessary libraries including LangChain, FastAPI, and Qdrant.

2. **Data Preparation:** Collect and preprocess your dataset to be used for training the LLM.

3. **Qdrant Integration:** Set up Qdrant as your vector database to store and retrieve embeddings.

4. **RAG Configuration:** Implement Retrieval-Augmented Generation (RAG) by connecting the retriever (using Qdrant) with the language model.

5. **LangChain Setup:** Use LangChain to manage the chain of operations, including retrieval, processing, and response generation.

6. **FastAPI Integration:** Develop a FastAPI application to serve the LLM with endpoints for querying and interacting with the model.

7. **Testing and Optimization:** Test the custom LLM with sample queries, optimize for performance and accuracy.

8. **Deployment:** Deploy the FastAPI application on a server or cloud service for public or private access.
