codon_table = {
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'CUU': 'Leucine',
    'CUC': 'Leucine',
    'CUA': 'Leucine',
    'CUG': 'Leucine',
    'AUU': 'Isoleucine',
    'AUC': 'Isoleucine',
    'AUA': 'Isoleucine',
    'AUG': 'Methionine',
    'GUU': 'Valine',
    'GUC': 'Valine',
    'GUA': 'Valine',
    'GUG': 'Valine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'CCU': 'Proline',
    'CCC': 'Proline',
    'CCA': 'Proline',
    'CCG': 'Proline',
    'ACU': 'Threonine',
    'ACC': 'Threonine',
    'ACA': 'Threonine',
    'ACG': 'Threonine',
    'GCU': 'Alanine',
    'GCC': 'Alanine',
    'GCA': 'Alanine',
    'GCG': 'Alanine',
    'UAU': 'Tyrosine',
    'UAC': 'Tyrosine',
    'UAA': 'Stop',
    'UAG': 'Stop',
    'CAU': 'Histidine',
    'CAC': 'Histidine',
    'CAA': 'Glutamine',
    'CAG': 'Glutamine',
    'AAU': 'Asparagine',
    'AAC': 'Asparagine',
    'AAA': 'Lysine',
    'AAG': 'Lysine',
    'GAU': 'Aspartic Acid',
    'GAC': 'Aspartic Acid',
    'GAA': 'Glutamic Acid',
    'GAG': 'Glutamic Acid',
    'UGU': 'Cysteine',
    'UGC': 'Cysteine',
    'UGA': 'Stop',
    'UGG': 'Tryptophan',
    'CGU': 'Arginine',
    'CGC': 'Arginine',
    'CGA': 'Arginine',
    'CGG': 'Arginine',
    'AGU': 'Serine',
    'AGC': 'Serine',
    'AGA': 'Arginine',
    'AGG': 'Arginine',
    'GGU': 'Glycine',
    'GGC': 'Glycine',
    'GGA': 'Glycine',
    'GGG': 'Glycine',
}


# Dictionary mapping amino acids to their information
amino_acid_info = {
    'phenylalanine': [
        "Essential amino acid, meaning it must be obtained from the diet.",
        "Precursor for neurotransmitters like dopamine and norepinephrine.",
        "Found in protein-rich foods like meat, fish, eggs, and dairy products.",
        "Excess accumulation in individuals with phenylketonuria (PKU) can cause neurological problems.",
        "Used in supplements for conditions like chronic pain and depression, but effectiveness is debated."
    ],
    'leucine': [
        "Essential amino acid that must be obtained from the diet.",
        "Plays a key role in protein synthesis and muscle growth.",
        "Activates the mTOR pathway, a central regulator of cell growth and metabolism.",
        "Found abundantly in protein-rich foods like meat, poultry, fish, dairy products, legumes, nuts, and seeds.",
        "Often used by athletes and bodybuilders to support muscle recovery and growth."
    ],
    'isoleucine': [
        "Essential amino acid that must be obtained from the diet.",
        "Plays a vital role in protein synthesis and muscle metabolism.",
        "Along with leucine and valine, it is one of the branched-chain amino acids (BCAAs), important for muscle growth and repair.",
        "Used as a source of energy during prolonged exercise and times of stress.",
        "Found in protein-rich foods like meat, poultry, fish, eggs, dairy products, nuts, seeds, and legumes."
    ],
    'methionine': [
        "Essential amino acid, meaning it must be obtained from the diet.",
        "Plays a crucial role in protein synthesis and metabolism.",
        "Contains a sulfur atom, making it important for the formation of sulfur-containing compounds.",
        "Acts as a precursor for the synthesis of cysteine, carnitine, taurine, and other molecules.",
        "Found in protein-rich foods like meat, poultry, fish, eggs, dairy products, nuts, seeds, and legumes."
    ],
    'valine': [
        "Essential amino acid that must be obtained from the diet.",
        "One of the three branched-chain amino acids (BCAAs), along with leucine and isoleucine.",
        "Important for muscle metabolism, tissue repair, and energy production.",
        "Used as a source of energy during exercise and times of stress.",
        "Found in protein-rich foods like meat, poultry, fish, dairy products, eggs, nuts, seeds, and legumes."
    ],
    'serine': [
        "Nonessential amino acid, meaning the body can synthesize it.",
        "Plays key roles in protein synthesis, cell proliferation, and the synthesis of other amino acids.",
        "Acts as a precursor for important molecules like phospholipids, which are essential for cell membrane structure.",
        "Involved in the synthesis of neurotransmitters and other signaling molecules.",
        "Found in various dietary sources including meat, dairy products, nuts, seeds, and certain grains."
    ],
    'proline': [
        "Nonessential amino acid, meaning the body can synthesize it.",
        "Plays a crucial role in the structure and stability of proteins.",
        "Contains a unique cyclic side chain that forms a rigid structure, affecting protein folding and stability.",
        "Abundant in collagen, the main structural protein in connective tissues like skin, tendons, and bones.",
        "Found in protein-rich foods like meat, dairy products, eggs, nuts, and seeds."
    ],
    'threonine': [
        "Essential amino acid, meaning it must be obtained from the diet.",
        "Plays a crucial role in protein synthesis and maintaining proper protein structure.",
        "Involved in the formation of collagen, elastin, and other structural proteins in connective tissues and skin.",
        "Acts as a precursor for the synthesis of glycine and serine, as well as other important molecules.",
        "Found in protein-rich foods like meat, poultry, fish, dairy products, eggs, nuts, seeds, and legumes."
    ],
    'alanine': [
        "Nonessential amino acid, meaning the body can produce it.",
        "Important for energy production, especially during exercise.",
        "Acts as a building block for proteins and plays a role in glucose metabolism.",
        "Involved in the transfer of nitrogen between tissues.",
        "Found in protein-rich foods like meat, poultry, fish, dairy products, eggs, nuts, seeds, and legumes."
    ],
    'tyrosine': [
        "Nonessential amino acid synthesized from phenylalanine in the body.",
        "Important precursor for neurotransmitters such as dopamine, norepinephrine, and epinephrine.",
        "Plays a role in regulating mood, stress response, and cognitive function.",
        "Involved in the production of thyroid hormones, which regulate metabolism.",
        "Found in protein-rich foods like meat, fish, dairy products, eggs, nuts, seeds, and certain grains."
    ],
    'stop': [
        "UAA: This stop codon is known as 'ochre.' It is the least common of the three stop codons and is recognized by release factor 1 (RF1) during translation termination.",
        "UAG: This stop codon is known as 'amber.' It is more common than UAA and is also recognized by release factor 1 (RF1) during translation termination.",
        "UGA: This stop codon is known as 'opal.' It is the most common of the three stop codons and is recognized by release factor 2 (RF2) during translation termination."
    ],
    'tryptophan': [
        "Essential amino acid that the body cannot produce on its own and must obtain from the diet.",
        "Precursor for the synthesis of serotonin, a neurotransmitter that regulates mood, sleep, and appetite.",
        "Also a precursor for the synthesis of melatonin, a hormone involved in regulating sleep-wake cycles.",
        "Found in protein-rich foods such as meat, poultry, fish, eggs, dairy products, nuts, seeds, and certain grains.",
        "May have potential therapeutic effects in treating conditions like depression, insomnia, and anxiety, although more research is needed to confirm its efficacy."
    ],
    'cysteine': [
        "Nonessential amino acid that can also be obtained from dietary sources.",
        "Contains a sulfur atom, making it unique among amino acids.",
        "Plays a crucial role in the formation of disulfide bonds, which stabilize protein structures.",
        "Acts as an antioxidant, scavenging free radicals and protecting cells from oxidative damage.",
        "Found in protein-rich foods like meat, poultry, fish, eggs, dairy products, and legumes."
    ],
    'glycine': [
        "Nonessential amino acid, meaning the body can produce it.",
        "Simplest amino acid with just a hydrogen atom as its side chain.",
        "Important for the synthesis of proteins, collagen, and other important molecules.",
        "Acts as a neurotransmitter inhibitor in the central nervous system, contributing to relaxation and sleep.",
        "Found in protein-rich foods like meat, poultry, fish, dairy products, eggs, gelatin, and certain legumes."
    ],
    'arginine': [
        "Semi-essential amino acid, meaning the body can produce it, but under certain conditions, dietary intake may be necessary.",
        "Plays a role in various physiological processes including protein synthesis, wound healing, immune function, and hormone secretion.",
        "Precursor for the synthesis of nitric oxide (NO), a molecule involved in vasodilation and blood flow regulation.",
        "Found in protein-rich foods like meat, poultry, fish, dairy products, nuts, seeds, and legumes.",
        "Used as a supplement for conditions like erectile dysfunction, high blood pressure, and athletic performance enhancement, although its effectiveness is still under research."
    ],
    'glutamine': [
        "Nonessential amino acid, meaning the body can synthesize it.",
        "Abundant in the body, particularly in muscle tissue.",
        "Plays a key role in protein synthesis, immune function, and intestinal health.",
        "Acts as a primary fuel source for rapidly dividing cells, such as intestinal cells and certain immune cells.",
        "Found in protein-rich foods like meat, poultry, fish, dairy products, tofu, beans, and legumes."
    ],
    'histidine': [
        "Essential amino acid that must be obtained from the diet.",
        "Plays a crucial role in the formation of metal-binding sites in proteins and enzymes.",
        "Acts as a precursor for histamine, a neurotransmitter involved in immune response and allergic reactions.",
        "Involved in the regulation of pH balance in the body, particularly in the buffering of acidic environments.",
        "Found in protein-rich foods like meat, poultry, fish, dairy products, eggs, nuts, seeds, and certain grains."
    ],
    'asparagine': [
        "Nonessential amino acid, meaning the body can synthesize it.",
        "Important for protein synthesis and the maintenance of nervous system function.",
        "Acts as a precursor for the synthesis of other amino acids and nitrogen-containing compounds.",
        "Involved in the formation and stability of protein structures.",
        "Found in protein-rich foods like meat, poultry, fish, dairy products, eggs, nuts, seeds, and legumes."
    ],
    'lysine': [
        "Essential amino acid that must be obtained from the diet.",
        "Important for protein synthesis, growth, and tissue repair.",
        "Plays a crucial role in the production of collagen, enzymes, hormones, and antibodies.",
        "Involved in the absorption of calcium and the formation of collagen, which is essential for bone health.",
        "Found in protein-rich foods like meat, poultry, fish, dairy products, eggs, nuts, seeds, and legumes."
    ],
    'aspartic Acid': [
        "Nonessential amino acid, meaning the body can synthesize it.",
        "Involved in the urea cycle, which detoxifies ammonia in the body.",
        "Acts as a precursor for the synthesis of other amino acids and molecules, including asparagine and neurotransmitters like aspartate and glutamate.",
        "Plays a role in energy production and neurotransmission.",
        "Found in protein-rich foods like meat, fish, dairy products, eggs, nuts, seeds, and legumes."
    ],
    'glutamic Acid': [
        "Nonessential amino acid, meaning the body can synthesize it.",
        "Acts as a neurotransmitter in the central nervous system, playing a key role in excitatory signaling.",
        "Involved in various physiological processes including learning, memory, and cognition.",
        "Also plays a role in protein synthesis and metabolism.",
        "Found naturally in protein-rich foods like meat, poultry, fish, dairy products, and certain vegetables like tomatoes and mushrooms."
    ],

}
