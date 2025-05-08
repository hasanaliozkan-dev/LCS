import random

# XOR dataset
data = [
    ([0, 0], 0),
    ([0, 1], 1),
    ([1, 0], 1),
    ([1, 1], 0)
]

class Classifier:
    def __init__(self, condition=None, action=None):
        self.condition = condition or self.random_condition()
        self.action = action if action is not None else random.choice([0, 1])
        self.prediction = 10.0
        self.fitness = 10.0
        self.experience = 0

    def random_condition(self):
        return [random.choice(['0', '1', '#']) for _ in range(2)]

    def matches(self, input_bits):
        return all(c == '#' or int(c) == bit for c, bit in zip(self.condition, input_bits))

    def __str__(self):
        return f"Cond:{''.join(self.condition)} Act:{self.action} Pred:{self.prediction:.2f} Fit:{self.fitness:.2f} Exp:{self.experience}"

class MichiganLCS:
    def __init__(self, population_size=30, beta=0.2, mutation_rate=0.1):
        self.population_size = population_size
        self.classifiers = [Classifier() for _ in range(population_size)]
        self.beta = beta
        self.mutation_rate = mutation_rate

    def run(self, epochs=100):
        for epoch in range(epochs):
            x, y = random.choice(data)
            match_set = [cl for cl in self.classifiers if cl.matches(x)]

            if not match_set:
                self.classifiers.append(Classifier(self.cover_condition(x), y))
                continue

            prediction_array = {act: sum(cl.prediction for cl in match_set if cl.action == act) for act in [0, 1]}
            selected_action = max(prediction_array, key=prediction_array.get)
            reward = 1000 if selected_action == y else 0

            for cl in match_set:
                if cl.action == selected_action:
                    cl.experience += 1
                    cl.prediction += self.beta * (reward - cl.prediction)
                    acc = reward / 1000
                    cl.fitness += self.beta * (acc - cl.fitness)

            self.evolve()
            if epoch % 10 == 0:
                acc = self.evaluate()
                print(f"Epoch {epoch:3d} Accuracy: {acc*100:.1f}%")

    def cover_condition(self, x):
        return [str(bit) if random.random() > 0.3 else '#' for bit in x]

    def evolve(self):
        # Apply genetic algorithm
        if len(self.classifiers) >= self.population_size:
            parents = random.sample(self.classifiers, 2)
            child1 = self.mutate(Classifier(parents[0].condition[:], parents[0].action))
            child2 = self.mutate(Classifier(parents[1].condition[:], parents[1].action))
            self.classifiers += [child1, child2]

        # Delete low-fitness classifiers
        self.classifiers = sorted(self.classifiers, key=lambda cl: cl.fitness / (1 + cl.experience))[-self.population_size:]

    def mutate(self, cl):
        for i in range(len(cl.condition)):
            if random.random() < self.mutation_rate:
                cl.condition[i] = random.choice(['0', '1', '#'])
        if random.random() < self.mutation_rate:
            cl.action = 1 - cl.action
        return cl

    def evaluate(self):
        correct = 0
        for x, y in data:
            match_set = [cl for cl in self.classifiers if cl.matches(x)]
            if not match_set:
                continue
            prediction_array = {act: sum(cl.prediction for cl in match_set if cl.action == act) for act in [0, 1]}
            selected_action = max(prediction_array, key=prediction_array.get)
            if selected_action == y:
                correct += 1
        return correct / len(data)

    def print_population(self):
        print("\nFinal Population:")
        for cl in sorted(self.classifiers, key=lambda c: -c.fitness):
            print(cl)


lcs = MichiganLCS()
lcs.run(epochs=100000)
lcs.print_population()
