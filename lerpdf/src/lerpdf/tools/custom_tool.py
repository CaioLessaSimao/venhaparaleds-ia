from crewai_tools import BaseTool
import os
import PyPDF2

class PDFReaderTool(BaseTool):
    name: str = "pdfReader"
    description: str = "Read multiple PDF files from a folder, extract their text, and save it to a single .txt file"

    def _run(self, pasta_pdf:str) -> str:
        try:
            
            # Verifica se o caminho da pasta é válido
            if not os.path.isdir(pasta_pdf):
                return f"Erro: O caminho {pasta_pdf} não é uma pasta válida."

            # Lista todos os arquivos PDF na pasta
            arquivos_pdf = [arquivo for arquivo in os.listdir(pasta_pdf) if arquivo.endswith(".pdf")]

            # Verifica se há arquivos PDF na pasta
            if not arquivos_pdf:
                return f"Nenhum arquivo PDF encontrado na pasta {pasta_pdf}."

            texto_final = ""

            # Processa cada arquivo PDF
            for arquivo_pdf in arquivos_pdf:
                caminho_completo = os.path.join(pasta_pdf, arquivo_pdf)
                with open(caminho_completo, 'rb') as f:
                    pdf = PyPDF2.PdfReader(f)
                    texto_final = '\n'.join(page.extract_text() for page in pdf.pages if page.extract_text())
            return texto_final

        except Exception as e:
            return f"Erro ao processar os arquivos PDF: {e}"
