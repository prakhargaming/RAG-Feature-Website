# GenAI Powered Smart Categorization Engine
Developed by Prakhar Sinha

## Introduction/Description
This is a full-stack web application designed to ingest the following data as structured JSON data:
1. **Product Title**
2. **Product Description**
3. **Associated Search Results** 

The engine will then output the search results that are actually relevant to the product title and description using GenAI and natural language processing (NLP).

## Data Processing Pipeline
Data is processed in a multistage pipeline:
1. JSON data is loaded into the system
2. Data is preprocessed according to standard NLP principles
3. Embeddings are generated
4. Heuristics are applied
5. Heuristics are cross-validated by an LLM

### Data Preprocessing
The data that is uploaded undergoes extensive preprocessing to make it ready for the embedding. Text is standarized by a combination of lowercasing, removing special characters, stopwords, and lemmatizing.

### Embeddings
Embeddings are generated from preprocessed data by one of two models:
1. **OpenAI text-embedding-3-small** This is the standard model and provides the best results
2. **Sentence Transformer all-MiniLM-L6-v2** This model is used if there are no OpenAI tokens available to use

### Heuristics
The main heuristic applied is **Cosine Similarity** where each search result is compared to its corresponding product title and description. This works very well most of the time and made me question the need to incorporate GenAI,

### LLM/GenAI Cross-Validation
Finally, the search results are cross-validated by an LLM. I originally opted to go for GPT-4 but after testing this is felt overkill. I ended up using a lighter model, GPT-4o Mini, with mixed results. 

## Full-Stack Application
Although only the development of a GenAI pipeline was asked in the project description, I opted to go the extra mile and design a full stack application around the pipeline as well.

### Tech Stack
These are the technologies I used in the development of this project

- **Frontend**
  - Next.js
  - TypeScript
  - Tailwind CSS
- **Backend**
  - Python
  - Flask
- **Communication**
  - Socket.io
  - JSON

## Known Bugs
- The first and most noticeable bug is that you must refresh the frontend webpage whenever you want to upload a new JSON file. I'm working on fixing this.

## Getting Started
There is a helpful bash script to help you run this script locally. You will need to make an `.env` file with an OpenAI key in the `./backend/app/engine` directory to get started. After this is done, installation should be straight forward. Run this command in your terminal to begin.

```sh
~ ./run.sh  
```
