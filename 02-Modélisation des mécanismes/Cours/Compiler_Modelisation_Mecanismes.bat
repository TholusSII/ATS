@echo off
setlocal
cd /d "%~dp0"

echo Nettoyage des fichiers auxiliaires potentiellement corrompus...
for %%F in (
  "00_Modelisation_Mecanismes.aux"
  "00_Modelisation_Mecanismes.toc"
  "00_Modelisation_Mecanismes.out"
  "00_Modelisation_Mecanismes.mw"
  "00_Modelisation_Mecanismes.lof"
  "00_Modelisation_Mecanismes.lot"
  "00_Modelisation_Mecanismes.idx"
  "00_Modelisation_Mecanismes.ilg"
  "00_Modelisation_Mecanismes.ind"
  "00_Modelisation_Mecanismes.fdb_latexmk"
  "00_Modelisation_Mecanismes.fls"
  "00_Modelisation_Mecanismes.synctex.gz"
) do if exist %%F del /q %%F

echo Premiere compilation...
pdflatex -interaction=nonstopmode -halt-on-error 00_Modelisation_Mecanismes.tex
if errorlevel 1 goto :error

if exist 00_Modelisation_Mecanismes.idx (
  echo Construction de l'index...
  makeindex 00_Modelisation_Mecanismes.idx
  if errorlevel 1 goto :error
)

echo Deuxieme compilation...
pdflatex -interaction=nonstopmode -halt-on-error 00_Modelisation_Mecanismes.tex
if errorlevel 1 goto :error

echo Troisieme compilation pour stabiliser les references...
pdflatex -interaction=nonstopmode -halt-on-error 00_Modelisation_Mecanismes.tex
if errorlevel 1 goto :error

echo.
echo Compilation terminee : 00_Modelisation_Mecanismes.pdf
exit /b 0

:error
echo.
echo La compilation a echoue. Consulter 00_Modelisation_Mecanismes.log.
exit /b 1
