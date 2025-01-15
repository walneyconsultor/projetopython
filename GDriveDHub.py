import os
import io
import base64
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from github import Github

# Configurações do Google Drive
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
SERVICE_ACCOUNT_FILE = 'path/to/credentials.json'

# Configurações do GitHub
GITHUB_TOKEN = 'your_github_token'
REPO_NAME = 'your_username/your_repo'
COMMIT_MESSAGE = 'Adicionando arquivos do Google Drive'

# Autenticação no Google Drive
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
drive_service = build('drive', 'v3', credentials=credentials)

# Autenticação no GitHub
g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

# Função para baixar arquivo do Google Drive
def download_file(file_id, file_name):
    request = drive_service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
    fh.seek(0)
    return fh.read()

# Lista de arquivos para copiar (IDs do Google Drive)
file_ids = ['file_id_1', 'file_id_2']

for file_id in file_ids:
    # Obter metadados do arquivo
    file_metadata = drive_service.files().get(fileId=file_id).execute()
    file_name = file_metadata['name']
    
    # Baixar arquivo
    file_content = download_file(file_id, file_name)
    
    # Codificar conteúdo do arquivo em base64
    content_base64 = base64.b64encode(file_content).decode('utf-8')
    
    # Criar ou atualizar arquivo no GitHub
    try:
        contents = repo.get_contents(file_name)
        repo.update_file(contents.path, COMMIT_MESSAGE, content_base64, contents.sha)
    except:
        repo.create_file(file_name, COMMIT_MESSAGE, content_base64)

print("Arquivos copiados com sucesso!")