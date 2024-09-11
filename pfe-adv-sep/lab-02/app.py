from flask import Flask, jsonify
import random

app = Flask(__name__)


dog_breeds = [
    "Labrador Retriever",
    "German Shepherd",
    "Golden Retriever",
    "French Bulldog",
    "Bulldog",
    "Poodle",
    "Beagle",
    "Rottweiler",
    "German Shorthaired Pointer",
    "Yorkshire Terrier"
]


cat_breeds = [
    "Persian Cat",
    "Maine Coon",
    "Ragdoll",
    "Siamese Cat",
    "British Shorthair",
    "Sphynx Cat",
    "Scottish Fold",
    "Abyssinian",
    "Bengal Cat",
    "Russian Blue"
]


@app.route('/random-pets', methods=['GET'])
def get_random_pet():
    if random.choice([True, False]):
        random_breed = random.choice(dog_breeds)
        animal_type = "dog"
    else:
        random_breed = random.choice(cat_breeds)
        animal_type = "cat"
    return jsonify({"animal": animal_type, "breed": random_breed})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
