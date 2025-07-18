@echo off
:: 📌 Arquivo: estimatron.bat
:: 🚀 Finalidade: ativar o ambiente virtual e executar o Streamlit (main.py)
:: 📍 Local esperado: pasta raiz do projeto (onde está o main.py)

:: 🧠 Ativa o ambiente virtual
call venv\Scripts\activate.bat

:: ▶️ Roda o Estimatron via Streamlit
python estimatron_gera_estrutarvore.py

:: ⏸️ Mantém o terminal aberto após encerramento
pause
