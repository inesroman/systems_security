import matplotlib.pyplot as plt

def total_time(num_digits):
    return 10**num_digits

num_digits = [3, 4, 5, 6]
times = [total_time(digit) for digit in num_digits]

plt.plot(num_digits, times, marker='o')
plt.title('Time to Test All Combinations vs. Number of Digits')
plt.xlabel('Number of Digits')
plt.ylabel('Time (milliseconds)')
plt.grid(True)
plt.show()