import subprocess
import sys

class Matrix:

    def __init__(self):
        subprocess.check_call([sys.executable, "-m", "pip", "install", "tensorflow"])
        subprocess.check_call([sys.executable, "-m", "pip", "install", "transformers"])
        from transformers import pipeline
        self.generator = pipeline('text-generation', model='facebook/opt-iml-max-1.3b', device=0)

    def printar(self):
        print("oi")
    
    def geradorXY(self,description,input):
        max_len = 1000

        if(len(description)<max_len):
            max_len = len(description)-1

        prompt = description[0:max_len] + input #concatena

        result = self.generator(prompt,max_length=1000)#inicializa
        output = result[0]['generated_text']#gera texto

        words = output.split()#divide o texto em palavras
        answer = words[-1]#escolhe apenas a ultima
        
        return answer
    
    def getImpact(self,description):
        input1 = '''

            How would the impact of this incident be described?

            OPTIONS:
            - Critical
            - Major
            - Moderate
            - Minor
            - Negligible

            Output:
            '''
        return self.geradorXY(description,input1)

    def getFrequency(self,description):
        input2 = '''

            How would the likelihood of this incident be described?

            OPTIONS:
            - Rare
            - Remote
            - Occasional
            - Probable
            - Frequent

            Output:
            '''
        return self.geradorXY(description,input2)