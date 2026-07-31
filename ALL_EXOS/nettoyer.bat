@echo off
setlocal
cd /d "%~dp0"

echo Nettoyage des fichiers auxiliaires de ALL_EXOS...
for %%F in (aux toc out idx ind ilg log lof lot fls fdb_latexmk synctex.gz) do (
  if exist "ALL_EXOS.%%F" del /q "ALL_EXOS.%%F"
)
if exist "ALL_EXOS.synctex(busy)" del /q "ALL_EXOS.synctex(busy)"

exit /b 1
