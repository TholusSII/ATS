@echo off
setlocal
cd /d "%~dp0"

echo Nettoyage des fichiers auxiliaires de ALL_EXOS...
for %%F in (aux toc out idx ind ilg log lof lot fls fdb_latexmk synctex.gz) do (
  if exist "ALL_EXOS.%%F" del /q "ALL_EXOS.%%F"
)
if exist "ALL_EXOS.synctex(busy)" del /q "ALL_EXOS.synctex(busy)"

echo Premiere compilation...
pdflatex -interaction=nonstopmode -halt-on-error ALL_EXOS.tex
if errorlevel 1 goto :error

if exist ALL_EXOS.idx (
  echo Generation de l'index...
  makeindex ALL_EXOS.idx
)

echo Deuxieme compilation...
pdflatex -interaction=nonstopmode -halt-on-error ALL_EXOS.tex
if errorlevel 1 goto :error

echo Troisieme compilation pour stabiliser les references...
pdflatex -interaction=nonstopmode -halt-on-error ALL_EXOS.tex
if errorlevel 1 goto :error

echo.
echo Compilation terminee avec succes.
pause
exit /b 0

:error
echo.
echo La compilation s'est arretee sur une erreur LaTeX.
echo Consultez ALL_EXOS.log pour le detail.
pause
exit /b 1
