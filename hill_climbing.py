
import pandas as pd         #data manipulation
import numpy as np          #numerical operations
import matplotlib.pyplot as plt     #plotting 

# Load Tesla stock price dataset
data = pd.read_csv(r'D:\AI Lab\archive\Tesla.csv - Tesla.csv.csv')

# Simplified objective function that implements a trading strategy
def evaluate_strategy(parameter):
    # Buy if the closing price is above the moving average with a window of 'parameter' days
    data['Signal'] = np.where(data['Close'] > data['Close'].rolling(window=parameter).mean(), 1, 0)
    
    # Calculate daily returns
    data['Daily_Return'] = data['Close'].pct_change()
    
    # Calculate strategy returns
    data['Strategy_Return'] = data['Signal'].shift(1) * data['Daily_Return']
    
    # Calculate cumulative returns
    cumulative_return = (1 + data['Strategy_Return']).cumprod().dropna().iloc[-1]
    
    return cumulative_return

# Hill Climbing algorithm it explores neighboring parameters and moves towards better performin parameter
def hill_climbing(initial_parameter, iterations):
    current_parameter = initial_parameter
    current_evaluation = evaluate_strategy(current_parameter)

    for _ in range(iterations):
        # Generate neighboring parameters (e.g., increase/decrease by a fixed amount)
        neighbor_parameter = current_parameter + np.random.choice([-1, 1]) * 1  

        # Evaluate the neighbor
        neighbor_evaluation = evaluate_strategy(neighbor_parameter)

        # Move to the neighbor if it improves the evaluation
        if neighbor_evaluation > current_evaluation:
            current_parameter = neighbor_parameter
            current_evaluation = neighbor_evaluation

    return current_parameter, current_evaluation

# Example usage
# applies hill climbing algorithm to find optimal parameter 
initial_parameter = 10  # Replace with an appropriate initial value for your parameter
iterations = 100        #steps to find optimal parameter

final_parameter, best_evaluation = hill_climbing(initial_parameter, iterations)

print(f"Optimal Parameter: {final_parameter}")
print(f"Best Evaluation: {best_evaluation}")

# Visualize the strategy performance with the optimal parameter
data['Optimal_Signal'] = np.where(data['Close'] > data['Close'].rolling(window=int(final_parameter)).mean(), 1, 0)
data['Optimal_Strategy_Return'] = data['Optimal_Signal'].shift(1) * data['Daily_Return']

plt.figure(figsize=(10, 6))
plt.plot(data['Close'], label='Tesla Stock Price')
plt.plot(data['Optimal_Strategy_Return'].cumsum(), label='Optimal Strategy Returns')
plt.legend()
plt.show()
