python -m venv fastapi-env
fastapi-env\Scripts\activate.bat

pip install -r requirements.txt



//how to activate virtual environment

fastapi-env\Scripts\activate.bat


pip install -r requirements.txt

to run program
uvicorn main:app --reload

uvicorn books:app --reload

http://127.0.0.1:8000

for swagger ui use following command

http://127.0.0.1:8000/docs



//for crypt purpose
pip install "passlib[bcrypt]"


// for authentication purpos
pip install python-multipart

//for json web token
pip install "python-jose[cryptoraphy]"

//for secret key go for cmd 
// and type below code
//openssl rand -hex 32


// for pgadmin(doubt) for better understanding search it

pip install psycopg2-binary

//for mysql install 
pip install pymysql

//for installation of alembic
pip install alembic

//to setup alembic in our project type following command on terminal
alembic init alembic

//create script for migration (for example add phone number) by using alembic upgrade
alembic revision -m "create phone number for user column"

// activate create phone number column
alembic upgrade db3fd711d365


// there is some error in bcrypt version so i put following in requirements.txt file
bcrypt==4.0.1
passlib[bcrypt]



 Make sure that you haven't already committed the files from that folder before adding the .gitignore rule, as Git will not untrack files that have already been committed. If you have already committed the files, you may need to follow up with additional steps to remove them from the repository.

If you've already committed the files and want to stop tracking them without deleting them, you can use the following commands:

git rm -r --cached src2/app/resource/
git commit -m "Stop tracking src2/app/resource/"