git add *
git commit -m "%DATE:~-4%-%DATE:~4,2%-%DATE:~7,2%"
git push

@echo delpoy heroku
rem git push heroku master

pause