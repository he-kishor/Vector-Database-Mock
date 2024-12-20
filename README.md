# Vector-Database-Mock
Simulating a Mock Vector Database Using Numpy,

# Vector Database Mock

This project demonstrates a simple Python-based vector database mockup that uses cosine similarity to find top matches for a given query.
Base on the query it calculate the SmarthPhone product.

## Features
- **Similarity Calculation**: Computes cosine similarity between a query vector and a dataset of vectors.
- **Top Matches**: Displays the top 3 results with the highest similarity scores.
- **Mock Dataset**: Uses pre-loaded embeddings and product names for demonstration.
- 
## approaches:

  - name: Direct Cosine Similarity I used
    steps:
      - Compute cosine similarity between the query and each product's embedding, I used Indexing here to better cosine with numpy.
      - Sort products by similarity score in descending order.
      - Select the top 3 most similar products.
    details:
      - pros: 
        - Straightforward and simple to implement.
          
      - cons: 
        - Computationally expensive for large datasets due to pairwise similarity calculations.

  - name: Section-Averaging Strategy
    steps:
      - Divide the product list into 3–4 sections based on embedding similarity.
      - Compute the average embedding vector for each section.
      - Match the query with the average vectors to find the closest section.
      - Perform detailed similarity calculations only within the closest section.
    details:
      - pros: 
        - "Reduces the number of similarity comparisons."
      - cons: 
        - May struggle with dynamic queries where sections aren't well-defined.

  - name: K-Nearest Neighbors (KNN)
    steps:
      - Use KNN to efficiently find similar products based on embeddings.
    details:
      - pros: 
        - Efficient for large-scale product embeddings.
      - cons: 
        - Requires indexing structures like KD-trees or Ball trees.
        - Performance depends on embedding dimensionality.


## How it Works
The program calculates cosine similarity between the query embedding and dataset embeddings. Cosine similarity measures the cosine of the angle between two vectors, defined as:

\[
\text{cosine similarity} = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|}
\]

- \( \mathbf{A} \): Query embedding vector.
- \( \mathbf{B} \): Dataset embedding vector.
- \( \mathbf{A} \cdot \mathbf{B} \): Dot product of vectors.
- \( \|\mathbf{A}\|, \|\mathbf{B}\| \): Magnitudes of the vectors.

## Time Complexity
- **Cosine Similarity Computation**: \( O(n \cdot m) \), where:
  - \( n \): Number of embeddings in the dataset.
  - \( m \): Dimension of each embedding vector.
- **Sorting**: \( O(n \cdot \log n) \) for finding the top 3 matches.

Overall complexity: \( O(n \cdot m + n \cdot \log n) \).

## Getting Started
### Prerequisites
- Python 3.7 or higher.
- Install `numpy` for mathematical operations.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/vector-db-mock.git
   cd vector-db-mock
   ```
2. create venv file 
``` bash
python -m venv venv
```
3. Install dependency
``` bash
 pip install -r requirements.txt
```
4. Run the main.py File using this command
``` bash
  python vector_database.py
```
5. Enter the product Description: "Enter the Product description" (click enter)
6. you will see a similar product:
``` bash
1. Product: "SpectraLite Z5" | Similarity: 0.968
2. Product: "PixelForge Prime" | Similarity: 0.946
3. Product: "PulseEcho VR" | Similarity: 0.938
```

## Example
1. 
``` bash
    (venv) PS C:\Users\nj991\Flask_Micro_Services\Vector-Database-Mock> python main.py
    Enter the product Description: Smarthphone with highest gaming phone
    Top Matches:
    1. Product: "Solaris Ultra" | Similarity: 0.973
    2. Product: "Glide Infinity" | Similarity: 0.947
    3. Product: "PulseEcho VR" | Similarity: 0.946
```

