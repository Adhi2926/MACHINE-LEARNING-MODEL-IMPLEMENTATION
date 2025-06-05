import random

# sample dataset of recipes
recipes = [
    "pasta with tomato sause: Boil pasta and mix with tomato sause. Add salt and pepper to taste.",
    "chiken stir-fry: heat oil in a pan. Add chiken, vegitables, and stir-fry sause, cook untl done.",
    "payasam: Boil the vermisely, add ghee, milk. keep it for some time, at last add some sugar.",
    "omelette: Beat eggs and pour into a hot, greased pan. Add cheese, onions, and bell peppers.",
    "vegetable soup: Boil the mixed vegetables in broth until soft. Blend until smooth.season with salt and pepper.",
]

# function to train a Markov chain model on dataset
def train_markov_chain(text):
    words = text.split()
    words_pairs = [(words[i], words[i + 1]) for i in range(len(words) - 1)]

    # create dictionary of words pairs and their following words
    markov_dict = {}
    for w1, w2 in words_pairs:
        if w1 in markov_dict:
            markov_dict[w1].append(w2)
        else:
            markov_dict[w1] = [w2]

            return markov_dict
        
        # generate a recipe using the markov chain model
        def generate_recipe(markov_dict, length=20):
            start_word = random.choice(list(markov_dict.keys()))
            recipe = [start_word]

            for _ in range(length - 1):
                next_word = random.choice(markov_dict[recipe[-1]])
                recipe.append(next_word)

                return " ".join(recipe)
            
            
            # train the model on the provided  recipes
            recipe_corpus = " ".join(recipes)
            markov_model = train_markov_chain(recipe_corpus)

            # generate and print recipe
            generated_recipe = generate_recipe(markov_model, length=15)
            print("Generated Recipe:")
            print("----------------------------------------")
            print(generate_recipe)