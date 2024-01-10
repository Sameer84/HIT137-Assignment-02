from collections import Counter
import spacy, scispacy

# Load the 'en_core_sci_sm' model
nlp_sci_sm = spacy.load('en_core_sci_sm')

# Load the 'en_ner_bc5cdr_md' model
nlp_bc5cdr_md = spacy.load('en_ner_bc5cdr_md')

# Read the text file
with open('./q1/merged_csv.txt', 'r') as file:
    text = file.read()

# Process the text using the 'en_core_sci_sm' model
doc_sci_sm = nlp_sci_sm(text)

# Process the text using the 'en_ner_bc5cdr_md' model
doc_bc5cdr_md = nlp_bc5cdr_md(text)

# Extract 'diseases' entities using 'en_core_sci_sm' model
diseases_sci_sm = [ent.text for ent in doc_sci_sm.ents if 'disease' in ent.text]

# Extract 'drugs' entities using 'en_core_sci_sm' model
drugs_sci_sm = [ent.text for ent in doc_sci_sm.ents if 'drug' in ent.text]

# Extract 'diseases' entities using 'en_ner_bc5cdr_md' model
diseases_bc5cdr_md = [ent.text for ent in doc_bc5cdr_md.ents if ent.label_ == 'DISEASE']

# Extract 'drugs' entities using 'en_ner_bc5cdr_md' model
drugs_bc5cdr_md = [ent.text for ent in doc_bc5cdr_md.ents if ent.label_ == 'DRUG']

# Compare the differences between the two models
total_entities_sci_sm = len(diseases_sci_sm) + len(drugs_sci_sm)
total_entities_bc5cdr_md = len(diseases_bc5cdr_md) + len(drugs_bc5cdr_md)
difference = total_entities_sci_sm - total_entities_bc5cdr_md

doc_sci = nlp_sci_sm(text)
doc_bc5cdr = nlp_bc5cdr_md(text)

# Print or analyze the results as needed

def write_file(content, file_name):
    with open('./q1/results/' + file_name, 'w') as f_out:
        # Iterate over each CSV file
        f_out.write(content)

write_file(str(diseases_sci_sm + drugs_sci_sm), 'en_core_sci_sm.txt')
write_file(str(diseases_bc5cdr_md + drugs_bc5cdr_md), 'en_ner_bc5cdr_md.txt')
write_file(str(Counter(diseases_sci_sm + drugs_sci_sm).most_common()), 'en_core_sci_sm_most_common.txt')
write_file(str(Counter(diseases_bc5cdr_md + drugs_bc5cdr_md).most_common()), 'en_ner_bc5cdr_md_most_common.txt')
write_file(str(difference), 'difference.txt')
