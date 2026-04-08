import pandas as pd
import os
import logging

# 日志设置
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_FILE = os.path.join(BASE_DIR, "data", "sample.xlsx")
OUTPUT_FILE = os.path.join(BASE_DIR, "output", "result.xlsx")

def load_data(file_path):
    logging.info("Loading data...")
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        logging.error(f"Failed to load data: {e}")
        return None

def clean_data(df):
    logging.info("Cleaning data...")
    df = df.dropna()
    df['weight'] = pd.to_numeric(df['weight'], errors='coerce')
    df = df.dropna(subset=['weight'])
    return df

def detect_anomalies(df):
    logging.info("Detecting anomalies...")

    mean = df['weight'].mean()
    std = df['weight'].std()

    df['is_abnormal'] = abs(df['weight'] - mean) > 3 * std
    return df

def save_data(df, output_path):
    logging.info("Saving results...")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_excel(output_path, index=False)

def generate_report(df):
    abnormal_df = df[df['is_abnormal'] == True]

    logging.info("===== REPORT =====")
    logging.info(f"Total records: {len(df)}")
    logging.info(f"Abnormal records: {len(abnormal_df)}")

    print("\nabnormal data：")
    print(abnormal_df)

def main():
    df = load_data(INPUT_FILE)
    if df is None:
        return

    df = clean_data(df)
    df = detect_anomalies(df)

    save_data(df, OUTPUT_FILE)
    generate_report(df)

    logging.info("Process completed successfully.")

if __name__ == "__main__":
    main()

