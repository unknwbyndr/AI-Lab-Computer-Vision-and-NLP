# Sentiment Vision Project

Welcome to the Sentiment Vision Project! This repository contains the code for a facial emotion recognition system using Convolutional Neural Networks (CNN) with Keras and TensorFlow. The project includes data preprocessing, model training, evaluation, and visualization functionalities.

## Table of Contents

- [Install Dependencies](#install-dependencies)
- [Data Preparation](#data-preparation)
- [Model Training](#model-training)
- [Model Evaluation](#model-evaluation)
- [Saving and Loading Models](#saving-and-loading-models)
- [Visualization](#visualization)
- [License](#license)
- [Authors](#authors)
- [Acknowledgements](#acknowledgements)

## Install Dependencies

To install the dependencies for this project, you have two options:

1. **Using Poetry** (recommended):

    Poetry is required to install the dependencies using the `pyproject.toml` file. You can find Poetry and its installation instructions [here](https://python-poetry.org/docs/).

    ```sh
    poetry install
    ```

2. **Using Pip**:

    You can also install the dependencies with pip from the requirements file.

    ```sh
    pip install -r requirements.txt
    ```

## Data Preparation

Define the paths for training and testing images and apply data augmentation:

- **Data Paths**:
  - Located at: `src/data/data_paths.py`
- **Data Augmentation**:
  - Located at: `src/data/data_augmentation.py`
- **Load Data**:
  - Located at: `src/data/load_data.py`

## Model Training

The training code and data are organized as follows:

- **Training Script**:
  - Located at: `src/models/model_training.py`
- **Training Data Generator**:
  - Located at: `src/data/data_generators.py`

## Model Evaluation

Evaluate the model using:

- **Evaluation Script**:
  - Located at: `src/models/evaluate_model.py`

## Saving and Loading Models

Save and load the model and weights using:

- **Save Model**:
  - Located at: `src/models/save_model.py`
- **Save Weights**:
  - Located at: `src/models/save_weights.py`
- **Make Predictions**:
  - Located at: `src/models/make_predictions.py`

## Visualization

Visualize the training results and processed images:

- **Plot Training Results**:
  - Located at: `src/visualization/plot_training_results.py`
- **Image Processing**:
  - Located at: `src/visualization/image_processing.py`
- **Display Predictions**:
  - Located at: `src/visualization/display_predictions.py`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Authors

- Tanvir
- Kapil

## Acknowledgements

- Keras and TensorFlow documentation
- Kaggle datasets for FER2013
- [FER2013 Dataset](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data)

---

Feel free to explore the repository and make sure to follow the instructions for setting up the dependencies and running the different components of the project. If you have any questions or issues, please open an issue or reach out to the project maintainers.
