import os
import shutil

if __name__ == "__main__":
    # inputOntology = "datasets/pizza.owl"
    inputOntology = "datasets/einsteins_riddle.owl"
    # inputOntology = 'datasets/pizza_super_simple.owl'
    Ontology = (inputOntology + '&').split('&')[0]
    signature = "datasets/sig.txt"
    inputSubclassStatements = "results/subClasses.nt"
    Method_order = {'a': ['1','2','3'],
                    'b': ['1','3','2'],
                    'c': ['2','1','3'],
                    'd': ['2','3','1'],
                    'e': ['3','2','1'],
                    'f': ['3','1','2']}
    
    for order in Method_order: 
        methods = Method_order[order]
        print("_________ Order Starts ___________")

        if order == 'a':
            for method in methods:
                print("____________ Epoch Start ______________")
                print(f"Input ontology: {Ontology}")
                print(f"Mothod no: {method}.")

                # Create Subclasses
                os.system('java -jar kr_functions.jar ' + 'saveAllSubClasses' + " " + Ontology)
                
                # Create Explanations
                # os.system('java -jar kr_functions.jar ' + 'saveAllExplanations' + " " + Ontology + " " + inputSubclassStatements)
                os.system('java -jar kr_functions.jar ' + 'saveAllExplanations' + " " + Ontology + " " + inputSubclassStatements)
                # keep back up sub classes
                subclass_bk = 'results/'+ order + "_" + method +  Ontology.split('/')[1] + "_class.nt"
                shutil.copy("datasets/subClasses.nt", subclass_bk)
                # Forgetting 
        
                os.system('java -cp lethe-standalone.jar uk.ac.man.cs.lethe.internal.application.ForgettingConsoleApplication --owlFile ' + Ontology + ' --method ' + method  + ' --signature ' + signature) 
        
                output_name = 'results/'+ order + "_" + method + "_" + Ontology.split('/')[1]
                os.rename('result.owl', output_name )
        
                Ontology = output_name
        Ontology = (inputOntology + '&').split('&')[0]