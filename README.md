# Diet Optimization Project

This project aims to optimize the cost of a diet while meeting specific nutritional requirements using linear programming.

## Project Structure

- `diet.py`: Main script that defines and solves the diet optimization problem.
- `run.sh`: Shell script to execute the job using Google Cloud Run.
- `deploy.sh`: Shell script to deploy the Cloud Run job.
- `README.md`: Project documentation (this file).

## Requirements

- Python
- pip
- Google Cloud SDK
- Docker

## Setup

1. **Clone the repository:**
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Running the Optimization

1. **Set the environment variable for optimization ID:**
    ```sh
    export OPTIMIZATION_ID=1
    ```

2. **Run the Python script:**
    ```sh
    python diet.py
    ```

### Using Google Cloud Run

1. **Set the region:**
    ```sh
    export REGION=us-central1
    ```

2. **Execute the job:**
    ```sh
    ./run.sh
    ```

### Deploying to Google Cloud Run

1. **Set the project ID and region:**
    ```sh
    export PROJECT_ID=YOUR_PROJECT_ID
    export REGION=us-central1
    ```

2. **Deploy the Cloud Run job:**
    ```sh
    ./deploy.sh
    ```

## Output

The script will output the optimal annual cost of foods and the nutrients per day. It will also return the results in two pandas DataFrames: one for nutrients and one for foods.

## Example

```sh
python diet.py


Number of variables = ...
Number of constraints = ...
Solving with ...
...
Optimal annual price: $...
Nutrients per day:
...