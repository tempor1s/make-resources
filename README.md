# 📚 Make Resources

## [Deployed Version](https://make-resources.herokuapp.com)

## 🚀 Getting Started

### Installation and Requirements

Requirements:

```bash
python3
pipenv
```

Installation:

```bash
# clone the repository
git clone https://github.com/tempor1s/make-resources.git
# cd into the project
cd make-resources
# create a virtual environment and install the required packages
pipenv shell
pipenv install
```

Congrats you should now have a working install of Make Resources

### Running The Project Locally

If you have not yet followed the installation steps, go and do so before continuing.

Once you have everything installed, you need to rename `.env.example` to `.env` and populate the fields with real data.

```bash
# cd into the src folder
cd make_resources
# rename .env.example to .env
mv .env.example .env
# populate the .env file with correct data
vim .env
```

Once you have renamed the `.env` file and populate it with correct data, all you need to do is run the server!

```bash
# run the the server
python3 manage.py runserver
# navigate to the url to see your running application!
http://localhost:8000
```

## 🤓 Specs

### Proposal

[Proposal](/docs/proposal.md)

### Requirements

- [x] At least 2 apps in project
- [ ] At least 2 tests in tests.py in each app
- [x] Modular design
- [ ] RESTful API using Django Rest Framework
- [x] Template-based front-end interface
- [ ] Has purpose and fulfills purpose
- [x] Integrates an open source app
- [x] Deployed and usable
- [x] Includes database migrations in each app
- [x] README with documentation
- [x] Public Github Repo
- [x] No exposed secrets

## Built With

- [Django](https://www.djangoproject.com/) - For pretty much everything
- [python-dotenv](https://pypi.org/project/python-dotenv/) - To keep secrets secret
- [djangorestframework](https://www.django-rest-framework.org/) - For the API
- [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms) - To keep the forms crispy
