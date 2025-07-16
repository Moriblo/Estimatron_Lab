@echo off
:: 📌 Arquivo: estimatron-dev.bat
:: 🛠️ Finalidade: ativar o ambiente virtual e rodar testes com cobertura de código
:: 📍 Local esperado: mesma raiz do projeto

:: 🧠 Ativa o ambiente virtual
call venv\Scripts\activate.bat

:: 🧪 Roda os testes com pytest + cobertura
pytest --cov=modules --cov-report=term --cov-report=html tests/

:: ⏸️ Mantém o terminal aberto após execução
pause
