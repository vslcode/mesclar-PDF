📄 Conteúdo do README.md para seu projeto “Mesclar PDF”
markdown
Copiar
Editar
# 📎 Mesclar PDF

Aplicativo desktop criado com **Python**, **CustomTkinter** e **PyPDF2** que permite selecionar, organizar e mesclar múltiplos arquivos PDF com uma interface moderna.

## 🔧 Funcionalidades

- Selecionar múltiplos arquivos PDF.
- Reorganizar a ordem dos PDFs.
- Modo Claro 🌞 e Escuro 🌙 com um clique.
- Definir onde salvar o PDF final.
- Ícone personalizado do aplicativo (`app.ico`).
- Interface construída com **CustomTkinter**.

## 🚀 Como Usar

### 📥 1. Executar o Executável

Se você já tem o `main.exe` gerado (em `dist/`), apenas **clique duas vezes em `main.exe`** para abrir o aplicativo.

### 🐍 2. Executar o Código Fonte (caso deseje usar o `main.py`)

Instale as dependências:

```bash
pip install customtkinter PyPDF2
E depois execute:

bash
Copiar
Editar
python main.py
🖼 Estrutura do Projeto
arduino
Copiar
Editar
MESCLAR PDF/
├── build/
│   └── main/ (arquivos de build do PyInstaller)
├── dist/
│   └── main.exe (executável do programa)
├── app.ico (ícone do aplicativo)
├── main.py (código-fonte principal)
├── main.spec (configuração do PyInstaller)
└── README.md (este arquivo)
🛠 Gerar o Executável Manualmente (opcional)
Para gerar o .exe novamente:

''' bash
Copiar
Editar
pyinstaller --noconfirm --onefile --windowed --icon=app.ico main.py
Isso vai gerar o executável em dist/main.exe.

👤 Autor
Desenvolvido por Vinicius Silva Lima — Sistema para mesclagem de PDFs com visual moderno e intuitivo.
