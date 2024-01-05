# Import the hashlib module
import hashlib
import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Define a function to split a text into sentences
def split_sentences(text):
    # Use spaCy to tokenize sentences
    doc = nlp(text)
    return [sent.text for sent in doc.sents]

# Rest of your code remains unchanged
# Define a function to create a fingerprint of a text
def create_fingerprint(text, hash_algorithm):
    # Split the text into sentences
    sentences = split_sentences(text)
    # Create an empty list to store the hashes
    hashes = []
    # Loop through each sentence
    for sentence in sentences:
        # Encode the sentence as bytes
        sentence_bytes = sentence.encode()
        # Apply the hashing algorithm and get the hexadecimal digest
        sentence_hash = hash_algorithm(sentence_bytes).hexdigest()
        # Append the hash to the list
        hashes.append(sentence_hash)
    # Return the list of hashes
    return hashes

# Define a function to compare two fingerprints and calculate the plagiarism score
def compare_fingerprints(fingerprint1, fingerprint2):
    # Find the length of the longest common subsequence of hashes
    common_hashes = [hash for hash in fingerprint1 if hash in fingerprint2]
    lcs_length = len(common_hashes)

    # Calculate the plagiarism score as the ratio of the LCS length to the total length of hashes
    plagiarism_score = lcs_length / max(len(fingerprint1), len(fingerprint2))

    # Return the plagiarism score
    return plagiarism_score

# Define the input text
input_text = "Plagiarism is defined in dictionaries as the \"wrongful appropriation,\" \"close imitation,\" or \"purloining and publication\" of another author's \"language, thoughts, ideas, or expressions,\" and the representation of them as one's own original work, but the notion remains problematic with nebulous boundaries."

# Define the source text
source_text = "Plagiarism is defined in dictionaries as the \"wrongful appropriation,\" \"close imitation,\" or \"purloining and publication\" of another author's \"language, thoughts, ideas, or expressions,\" and the representation of them as one's own original work, but the notion remains problematic with nebulous boundaries."

# Choose the MD5 hashing algorithm
hash_algorithm = hashlib.md5

# Create a fingerprint of the input text
input_fingerprint = create_fingerprint(input_text, hash_algorithm)

# Create a fingerprint of the source text
source_fingerprint = create_fingerprint(source_text, hash_algorithm)

# Compare the two fingerprints and get the plagiarism score
plagiarism_score = compare_fingerprints(input_fingerprint, source_fingerprint)

# Print the plagiarism score
print(f"The plagiarism score is {plagiarism_score:.2f}")
