# MVT project in Django within the context of the Python course taught by Coderhouse

## Development branches and description
- 'master': personal branch. In this branch I usually push code from other branches.
- 'mvt_forms_and_search': branch for practicing forms and basic search.
- 'mvt_18_coderhouse': branch with requirements for class 18 delivery
- 'mvt_21_coderhouse': branch with requirements for delivery of class 21

## Branch for class delivery 21
- Assuming you have the project installed, with the required add-ons and the virtual environment activated (see topic "How to start the project on a local server" further down in this document)

### Start the project
1. In your bash, go to the root of the project
2. Type the following commands in the terminal
```bash
git checkout mvt_21_coderhouse
cd first_mvt
python manage.py runserver
```
3. Visit the address "127.0.0.1:8000" in your browser
- There are 3 classes: Adventures, Family_members and Possessions.
- It is possible to insert new objects from each specific button within the web.
- It is possible to search for family members being in the root of the url.

## How to start the project on local server
### If you already have the project downloaded:
1. Go to the project folder, and open bash (or in the terminal of your code editor).
2. At the root of the repository, run the command in terminal
```bash
git pull
```
to update the repository to the latest version.

### If you don't have the project downloaded:
1. Choose a destination where you will download the project
2. Open a bash on that path
3. Run the command in the terminal
```bash
git clone https://github.com/pablofontaine/MVT.git
```
4. At the root of the project, create a virtual environment
```bash
python -m venv venv
```
5. Start the virtual environment
```bash
./venv/Scripts/activate
```
6. Download the files required for the project
```bash
pip install -r requirements.txt
```
