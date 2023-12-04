@echo off
SET THEFILE=d:\seleksi_pemilu\hiting1sampai5.exe
echo Linking %THEFILE%
c:\dev-pas\bin\ldw.exe  D:\Seleksi_Pemilu\rsrc.o -s   -b base.$$$ -o d:\seleksi_pemilu\hiting1sampai5.exe link.res
if errorlevel 1 goto linkend
goto end
:asmend
echo An error occured while assembling %THEFILE%
goto end
:linkend
echo An error occured while linking %THEFILE%
:end
