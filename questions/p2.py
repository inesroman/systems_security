import matplotlib.pyplot as plt

def unique_challenge_probability(k):
    probability = 1
    for i in range(1, k + 1):
        probability *= (2**32 - i) / (2**32)
    return probability

# Calculate probabilities for k from 10 to 10^8
k_values = [10**i for i in range(1, 9)]
probabilities = [unique_challenge_probability(k) for k in k_values]

# Plot the result
plt.plot(k_values, probabilities, marker='o')
plt.title('Probability of All Challenges Being Unique')
plt.xlabel('Number of Challenges (k)')
plt.ylabel('Probability')
plt.xscale('log')  # Logarithmic scale on the x-axis
plt.grid(True)
plt.show()
