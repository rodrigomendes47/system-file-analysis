import google.generativeai as genai
import time
import os

class PdfAnalyzer:
    def __init__(self):
        with open('cred.txt','r') as file:
            token = file.readlines()[0]
        genai.configure(api_key=token)
        self.model = genai.GenerativeModel('gemini-pro')
        with open('keywords.txt', "r") as file:
            self.keywords = [line.strip().lower() for line in file.readlines()]
            print("[INFO] Keywords file loaded successfully!")

    def search_key_words(self, page_text):
        if any(word in page_text for word in self.keywords):
            found_keyword = [word for word in self.keywords if word in page_text][0]
            return found_keyword
        else:
            return False

    def page_to_string(self, text):
        text = text.replace('\n',' ').split(' ')
        text = [x for x in text if x != '']
        text =  ' '.join(text).lower()
        return text
    
    def ask_to_gemini(self, text, keyword):
        time.sleep(0.2)
        prompt = f'resposta curta, sem justificativa, caso nao tenha esas informacao, responda "--/--". baseado no texto a seguir (pode conter erros de espacamento), qual a  carga horaria para disciplina que possua o termo "{keyword}": {text}. responda no formato carga horaria total(somente numero)/disciplina(em uppercase, nao é o codigo da disciplina). Cuidado para nao confundir com numero da pagina!'
        try:
            response = self.model.generate_content(prompt).text
            response = self.validate_gemini_response(response)
        except:
            print('\n[WARNING] Gemini API is overloaded! Waiting 60 secs to cooldown')
            time.sleep(60)
            try:
                response = self.model.generate_content(prompt).text
                response = self.validate_gemini_response(response)
            except:
                print('\n[ERROR] An unexpected error occurred: Gemini API')
                response = '--/--'
        return response

    def validate_gemini_response(self, response):
        try:
            response = response.split('/')
            hours = response[0]
            class_name = response[1]
            hours = int(hours)
            if hours < 250:
                return [hours, class_name]
            else: 
                return False
        except:
            return False
