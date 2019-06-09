cd ..\emsdk-master\
call .\emsdk activate latest

cd %1
for /f "delims=" %%a in ('dir /s /b *.cpp') do (
 call set concat=%%concat%% %%a
 )

call em++ %concat% -o %2 --preload-file code/code.txt

cd %~dp0
python -m SimpleHTTPServer 8080
