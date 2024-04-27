from flask import Flask, render_template, request
from codon_table import codon_table, amino_acid_info

app = Flask(__name__)


def generate_all_codons(sequence):
    sequence = set(sequence.upper())
    all_codons = codon_table.keys()
    matching_codons = [(codon, codon_table.get(codon, "Unknown")) for codon in all_codons if set(codon) == sequence]
    return matching_codons


def calculate_anticodon(codon):
    anticodon_table = {
        'A': 'U',
        'U': 'A',
        'C': 'G',
        'G': 'C'
    }

    anticodon = ''
    for base in codon:
        anticodon += anticodon_table.get(base, '')

    return anticodon


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
    matching_codons = []
    amino_acid_information = ""

    amino_acid_lower = amino_acid.lower()

    for codon, acid in codon_table.items():
        if acid.lower() == amino_acid_lower:
            matching_codons.append(codon)

    if amino_acid_lower in amino_acid_info:
        amino_acid_information = amino_acid_info[amino_acid_lower]

    return matching_codons, amino_acid_information

# Update the Flask route for mrna_chain
@app.route("/mrna_chain", methods=["GET", "POST"])
def mrna_chain():
    if request.method == "POST":
        mrna_sequence = request.form["mrna_sequence"].upper()


        codons = []
        errors = []


        if len(mrna_sequence) % 3 != 0:
            errors.append("Invalid input: MRNA sequence length should be a multiple of 3.")

        start_codon = "AUG"
        if not mrna_sequence.startswith(start_codon):
            errors.append("Invalid input: MRNA sequence should start with 'AUG' (start codon).")


        stop_codons = ["UAA", "UAG", "UGA"]
        if not any(mrna_sequence.endswith(stop_codon) for stop_codon in stop_codons):
            errors.append("Invalid input: MRNA sequence should end with a stop codon ('UAA', 'UAG', 'UGA').")


        if any(codon in mrna_sequence[3:-3] for codon in [start_codon] + stop_codons):
            errors.append("Invalid input: Start and stop codons should not appear in the middle of the MRNA sequence.")


        for i in range(0, len(mrna_sequence), 3):
            codon = mrna_sequence[i:i + 3]
            if codon_table.get(codon):
                codons.append(codon + ": " + codon_table[codon])
            else:
                errors.append(codon + ": Invalid codon")

        return render_template("mrna_chain_result.html", mrna_sequence=mrna_sequence, codons=codons, errors=errors)
    else:
        return render_template("mrna_chain_input.html")

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


        amino_acid_information = "Information not available"
        amino_acid_lower = amino_acid.lower()
        if amino_acid_lower in amino_acid_info:
            amino_acid_information = amino_acid_info[amino_acid_lower]


        anticodon = calculate_anticodon(codon)

        return render_template("exact_codon.html", codon=codon, amino_acid=amino_acid,
                               amino_acid_info=amino_acid_information, anticodon=anticodon)
    else:

        return render_template("exact_codon_input.html")

@app.route("/possible_combinations", methods=["GET", "POST"])
def possible_combinations():
    if request.method == "POST":
        sequence = request.form["sequence"].upper()
        all_codons = generate_all_codons(sequence)
        all_codons_dict = dict(all_codons)
        return render_template("possible_combinations.html", sequence=sequence, all_codons=all_codons_dict)
    else:
        return render_template("possible_combinations_input.html")

@app.route("/codon_by_name", methods=["GET", "POST"])
def codon_by_name():
    if request.method == "POST":
        amino_acid = request.form["amino_acid"].upper()
        matching_codons, amino_acid_information = find_matching_codons_by_name(amino_acid)
        return render_template("codon_by_name.html", amino_acid=amino_acid, matching_codons=matching_codons,
                               amino_acid_info=amino_acid_information)
    else:
        return render_template("codon_by_name_input.html")


if __name__ == "__main__":
    app.run(debug=True)


