# Diet Optimization Project

This project aims to optimize the cost of a diet while meeting specific nutritional requirements using linear programming.

## Key Features

- **Linear Programming**: Uses OR-Tools to solve the diet optimization problem.
- **Cloud Deployment**: Includes scripts to deploy and run the optimization on Google Cloud Run.
- **Data Handling**: Outputs results in pandas DataFrames for easy analysis.

## Project Structure

- `deploy-cloud-run-service/`: Contains the version of the optimization diet deployed as a Cloud Run service.
- `deploy-cloud-run-job/`: Contains the version of the project using Cloud Run jobs.


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
