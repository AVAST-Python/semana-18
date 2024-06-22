import random









































def multi_armed_bandit(arm):
    if arm < 0 or arm > 4:
        raise ValueError("Arm parameter must be between 0 and 4")

    # Define the reward distributions for each arm
    distributions = [
        lambda: 2 * random.random() + 1,  # 2   Arm 0: Uniform linear distribution from 1 to 3
        lambda: 3 * random.random() + 2,  # 3.5 Arm 1: Uniform linear distribution from 2 to 5
        lambda: random.gauss(1, 0.5),     # 1   Arm 2: Normal distribution with mean 1 and std dev 0.5
        lambda: random.gauss(2, 1.0),     # 2   Arm 3: Normal distribution with mean 2 and std dev 1.0
        lambda: 5                         # 5   Arm 4: Constant value of 5
    ]

    # Select the corresponding distribution for the chosen arm and generate a reward
    reward = distributions[arm]()

    return reward

