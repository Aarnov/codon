# main.py
from flask import Flask, render_template, request
from codon_table import codon_table

app = Flask(__name__)

def generate_all_codons(sequence):
    sequence = set(sequence.upper())
    all_codons = codon_table.keys()
    matching_codons = [(codon, codon_table.get(codon, "Unknown")) for codon in all_codons if set(codon) == sequence]
    return matching_codons

def find_matching_codons(sequence):
    sequence = sequence.capitalize()
    if sequence in (acid.lower() for acid in codon_table.values()):
        matching_codons = [codon for codon, amino_acid in codon_table.items() if amino_acid.lower() == sequence.lower()]
    else:
        sequence = set(sequence.upper())
        all_codons = codon_table.keys()
        matching_codons = [codon for codon in all_codons if set(codon) == sequence]
    return matching_codons

def find_matching_codons_by_name(amino_acid):
    return [codon for codon, acid in codon_table.items() if acid.lower() == amino_acid.lower()]

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/exact_codon", methods=["GET", "POST"])
def exact_codon():
    if request.method == "POST":
        first_base = request.form["first_base"]
        second_base = request.form["second_base"]
        third_base = request.form["third_base"]
        codon = first_base + second_base + third_base
        amino_acid = codon_table.get(codon, "Unknown")
        return render_template("exact_codon.html", codon=codon, amino_acid=amino_acid)
    return render_template("exact_codon_input.html")

@app.route("/possible_combinations", methods=["GET", "POST"])
def possible_combinations():
    if request.method == "POST":
        sequence = request.form["sequence"]
        all_codons = generate_all_codons(sequence)
        return render_template("possible_combinations.html", sequence=sequence, all_codons=all_codons)
    else:
        return render_template("possible_combinations_input.html")

@app.route("/codon_by_name", methods=["GET", "POST"])
def codon_by_name():
    if request.method == "POST":
        amino_acid = request.form["amino_acid"]
        matching_codons = find_matching_codons_by_name(amino_acid)
        return render_template("codon_by_name.html", amino_acid=amino_acid, matching_codons=matching_codons)
    else:
        return render_template("codon_by_name_input.html")

if __name__ == "__main__":
    app.run(debug=True)



#write the anticodon for the given codon.
#take an mrna chain and display all the amino acids formed inside it .
#considerr the start codon and then display all the combinations after it untill stop comes .
