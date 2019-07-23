# Running the program
```bash
git clone https://github.com/Anudeep07/NLP-PoC.git
pip3 install nltk
cd NLP-PoC/ && python3 POC.py
```

# Program Information
* Recognizes named entities using the provided NLTK classifier.
* The output is a tree structure. Use the draw() method to show the structure in a GUI
* A node can be either a tagged word or a named entity.
* If it's a named entity, then the child nodes represent the tagged word.