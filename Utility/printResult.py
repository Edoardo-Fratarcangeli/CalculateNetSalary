import requests
import pandas as pd
from enums import PrintFormat

 # solo queste verranno importate con *
__all__ = ['printResult'] 

def printResult (results, format: PrintFormat = PrintFormat.Console):
    match format:
        case PrintFormat.Console :
            printResultConsole(results)
        case PrintFormat.Pdf:
            printResultPdf(results)
        case PrintFormat.Excel:
            printResultExcel(results)

def printResultConsole (results):
    df = pd.DataFrame(results)
    print(df)

def printResultPdf (results):
    NotImplementedError
    
def printResultExcel (results):
    NotImplementedError
