@echo off
color 02
echo loop:) if wrong 
set comp=
set /p comp=whats the computer called? 
if /I NOT "%comp%"=="computer" (
	:a 
start www.learnbatchfile.weebly.com
goto :a 
)


