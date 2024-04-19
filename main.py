from data_collection import data_collection
from data_preprocessing import data_preprocessing
from feature_engineering import feature_engineering
from model_selection import model_selection
from model_training import model_training
from model_evaluation import model_evaluation
from model_optimization import model_optimization
from deployment import deployment


def main():
    # Run the data collection script
    data_collection.main()

    # Run the data preprocessing script
    data_preprocessing.main()

    # Run the feature engineering script
    feature_engineering.main()

    # Run the model selection script
    model_selection.main()

    # Run the model training script
    model_training.main()

    # Run the model evaluation script
    model_evaluation.main()

    # Run the model optimization script
    model_optimization.main()

    # Run the deployment script
    deployment.main()

if __name__ == "__main__":
    main()
