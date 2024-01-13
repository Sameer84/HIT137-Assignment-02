import os
from collections import Counter
import spacy, scispacy
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline


PRE_DIR_NAME = './q1'
INPUT_FILE = PRE_DIR_NAME + '/merged_csv.txt'
OUTPUT_DIR = PRE_DIR_NAME + '/results'
MODEL_NAME = 'dmis-lab/biobert-v1.1'


def count_and_top_words(doc, chunk_size=900000, top_n=30):
    entities = [ent.text for ent in doc.ents]
    total_entities = len(entities)
    # Extract 'diseases' entities
    diseases_ent = [ent.text for ent in doc.ents if ent.label_ == 'DISEASE']
    # Extract 'drugs' entities
    drugs_ent = [ent.text for ent in doc.ents if ent.label_ == 'DRUG']
    # Extract entities length
    extract_entities = len(diseases_ent) + len(drugs_ent)
    # Tokenize the chunk and update token counts
    top_tokens = Counter(entities)

    return entities, total_entities, diseases_ent, drugs_ent, extract_entities, top_tokens


def run():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Load the 'en_core_sci_sm' model
    en_core_sci_sm = "en_core_sci_sm"
    nlp_sci_sm = spacy.load(en_core_sci_sm)
    entities_sci_sm = []
    total_entities_sci_sm = 0
    diseases_model_sci_sm = []
    drugs_model_sci_sm = []
    tokens_sci_sm = Counter()

    # Load the 'en_ner_bc5cdr_md' model
    en_ner_bc5cdr_md = "en_ner_bc5cdr_md"
    nlp_bc5cdr_md = spacy.load(en_ner_bc5cdr_md)
    entities_bc5cdr_md = []
    total_entities_bc5cdr_md = 0
    diseases_model_bc5cdr_md = []
    drugs_model_bc5cdr_md = []
    tokens_bc5cdr_md = Counter()

    
    # Load the NER pipeline with biobert model
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForTokenClassification.from_pretrained(MODEL_NAME)

    # Extract entities using the NER pipeline
    nlp = pipeline("ner", model=model, tokenizer=tokenizer)

    # Load the 'en_core_sci_sm' model
    entities_biobert = []
    total_biobert = 0
    filtered_biobert = []
    tokens_biobert = Counter()
    

    with open(OUTPUT_DIR + '/t4_result.txt', 'w') as f_out:
        with open(INPUT_FILE, 'r', encoding='utf-8') as file:
            # Read the text from the file in chunks
            chunk_size = 900000
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                entities, total_entities, diseases_ent, drugs_ent, extract_entities, top_tokens = \
                    count_and_top_words(nlp_sci_sm(chunk), chunk_size=chunk_size)
                entities_sci_sm += entities
                total_entities_sci_sm += total_entities
                diseases_model_sci_sm += diseases_ent
                drugs_model_sci_sm += drugs_ent
                tokens_sci_sm += top_tokens

                entities, total_entities, diseases_ent, drugs_ent, extract_entities, top_tokens = \
                    count_and_top_words(nlp_bc5cdr_md(chunk), chunk_size=chunk_size)
                entities_bc5cdr_md += entities
                total_entities_bc5cdr_md += total_entities
                diseases_model_bc5cdr_md += diseases_ent
                drugs_model_bc5cdr_md += drugs_ent
                tokens_bc5cdr_md += top_tokens
        
            print(f'Total entities detected {en_core_sci_sm}: {total_entities_sci_sm}')
            print(f'Total entities detected {en_ner_bc5cdr_md}: {total_entities_bc5cdr_md}')
            
            f_out.write(f'Total entities detected {en_core_sci_sm}: {total_entities_sci_sm}')
            f_out.write(f'Total entities detected {en_ner_bc5cdr_md}: {total_entities_bc5cdr_md}')
            f_out.write(f'Top 30 entities {en_core_sci_sm}: {len(tokens_bc5cdr_md.most_common(30))}')
            f_out.write(f'Top 30 entities {en_ner_bc5cdr_md}: {len(tokens_sci_sm.most_common(30))}')
            f_out.write(f'Total extracted entities {en_core_sci_sm}: {len(diseases_model_sci_sm) + len(drugs_model_sci_sm)}')
            f_out.write(f'Total extracted entities {en_ner_bc5cdr_md}: {len(diseases_model_bc5cdr_md) + len(drugs_model_bc5cdr_md)}')
            f_out.write(f'All entities {en_core_sci_sm}: {entities_sci_sm}')
            f_out.write(f'All entities {en_ner_bc5cdr_md}: {entities_bc5cdr_md}')

            # Read the text from the file in chunks
            chunk_size = 700
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                doc_biobert = nlp(chunk)
                entities_biobert += [entity['word'] for entity in doc_biobert]
                filtered_biobert = [entity['word'] for entity in doc_biobert if entity['entity'] == 'DRUG' or entity['entity'] == 'DISEASE']
                total_biobert += len(entities_biobert)
                tokens_biobert += Counter(filtered_biobert)
            
            print(f'Total entities detected {MODEL_NAME}: {total_biobert}')
            f_out.write(f'Total entities detected {MODEL_NAME}: {total_biobert}')
            f_out.write(f'Top 30 entities {MODEL_NAME}: {tokens_biobert.most_common(30)}')
            f_out.write(f'Total extracted entities {MODEL_NAME}: {len(filtered_biobert)}')
            f_out.write(f'All entities {MODEL_NAME}: {entities_biobert}')

        file.close()
    f_out.close()

run()
