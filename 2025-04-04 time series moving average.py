"""Generated from Jupyter notebook: 2025-04-04 time series moving average

Magics and shell lines are commented out. Run with a normal Python interpreter."""


# --- code cell ---

import moving_average
import pandas as pd


def main():
    data = [10, 12, 14, 13, 15, 16, 14, 13, 17, 18]
    df = pd.DataFrame({"Value": data})

    ama = moving_average.arithmetic_moving_average(df["Value"], window=3)
    gma = moving_average.geometric_moving_average(df["Value"], window=3)

    moving_average.plot_moving_average(df["Value"], ama, gma)


    # --- code cell ---

    import neural_networks

    X, y, scaler = neural_networks.load_and_preprocess_data("ngram.csv", n_steps=30)
    model = neural_networks.build_lstm_model(n_steps=30)
    model.fit(X, y, epochs=10, batch_size=32)


    # --- code cell ---

    df = pd.read_csv("ngram.csv")


    # --- code cell ---

    df.head()


    # --- code cell ---

    import pandas as pd

    df = pd.read_csv("gold_oil_data.csv", parse_dates=["date"], index_col="date")

    # Test for stationarity
    print(cointegration_analysis.adf_test(df["gold"], "Gold Prices"))
    print(cointegration_analysis.adf_test(df["oil"], "Oil Prices"))

    # Test for cointegration
    print(cointegration_analysis.cointegration_test(df["gold"], df["oil"]))

    # Plot the series
    cointegration_analysis.plot_series(df)


if __name__ == "__main__":
    main()
