from PyPDF2 import PdfReader
import os
from pdf_analyzer import PdfAnalyzer
from tqdm import tqdm
import pandas as pd
from tabulate import tabulate 
from datetime import datetime

print('[INFO] Initializing process. Press CTRL C anytime to abort.')
pdf = PdfAnalyzer()
docs_list = os.listdir("docs")
final_df = pd.DataFrame({'Disciplinas': [], 'Carga Horaria': [], 'Doc': []})
start_time = datetime.now()

for doc in docs_list:
    disciplinas = []
    ch = []
    pags = []
    page_count = 1
    print(f"[INFO] Analyzing document: {doc}")
    document = PdfReader(f"docs/{doc}") # If document is NOT scanned
    for i in tqdm(range(len(document.pages)-2)):
        text = pdf.page_to_string(document.pages[i].extract_text()+document.pages[i+1].extract_text())
        keyword = pdf.search_key_words(text)
        if keyword:
            hours_class = pdf.ask_to_gemini(text, keyword)
            if hours_class:
                ch.append(hours_class[0])
                disciplinas.append(hours_class[1])
                pags.append(i)
        page_count += 1
    dict = {'Disciplinas': disciplinas, 'Carga Horaria': ch,'Pag': pags, 'Doc': [doc.replace('.pdf', '').upper() for _ in range(len(disciplinas))]}
    df = pd.DataFrame(dict).drop_duplicates(subset=['Disciplinas', 'Carga Horaria'], keep="first")
    print(f'[INFO] {doc} analyzed successfully. {len(df)} occurrences found.')
    final_df = pd.concat([final_df, df], ignore_index=True)
print(tabulate(final_df, headers="keys", tablefmt="fancy_grid"))
final_df.to_csv('results.csv')
print('[INFO] Done!')
print(f'[INFO] The script took {datetime.now()-start_time} to execute.')