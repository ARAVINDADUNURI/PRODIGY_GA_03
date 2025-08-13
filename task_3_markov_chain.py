import random

def build_markov_chain(text, n=1):
    words = text.split()
    markov_chain = {}

    for i in range(len(words) - n):
        key = tuple(words[i:i+n])
        next_word = words[i+n]
        if key not in markov_chain:
            markov_chain[key] = []
        markov_chain[key].append(next_word)
    
    return markov_chain

def generate_text(chain, n=1, max_words=50):
    start_key = random.choice(list(chain.keys()))
    output = list(start_key)

    for _ in range(max_words - n):
        if start_key in chain:
            next_word = random.choice(chain[start_key])
            output.append(next_word)
            start_key = tuple(output[-n:])
        else:
            break

    return ' '.join(output)

# Sample usage
sample_text = """
Markov chains are a simple and effective way to generate text.
They use probabilities based on previous words to predict the next word.
This makes them great for generating random but somewhat coherent text.
"""

chain = build_markov_chain(sample_text, n=2)
generated = generate_text(chain, n=2, max_words=30)
print("Generated Text:\n", generated)
