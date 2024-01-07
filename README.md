# HIT137-Assignment-02
[STUDENT NAME] - [STUDENT ID]  
[Sameer Basnet] - [S372941]  
[Samir Dhakal] - [S373048]  
[Susanti Djie] - [S375655]  
[Nishat Anjum] - [S374044]  

### configuration
1. setup venv(virtual environments) with Python<3.9, recommend 3.8.10
    - How to set up venv? [Python Docs](https://docs.python.org) › library › venv)
    - scispacy==0.5.3 uses nmslib which requires Python<3.9
    - reference: https://github.com/allenai/scispacy/issues/291#issuecomment-771076466
2. run following command to install libraries in requirements.txt
   ```python
   pip install -r .\requirements.txt
   ```
   - Following libraries are used for the project
       * spacy==3.6.1 : matched version with scispacy
       * :spacy module(en_coew_wev_sm)
       * scispacy==0.5.3 : newest version
       * :scispacy module(en_ner_bc5cdr_md)
       * transformers[biogpt] : biogpt as a bio-medical model https://huggingface.co/docs/transformers/model_doc/biogpt
3. copy 4 CSV Files from assessment 2 zip folder to q1 
    - CSV1.csv, CSV2.csv, CSV3.csv, CSV4.csv
    
