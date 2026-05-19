# Lancer les tests
pytest tests/ -v

# Lancer les tests avec couverture de code
pytest --cov=calculs --cov-report=term-missing

# Créer l'exécutable
pyinstaller --onefile --name calculs main.py

# Vérifier le style du code
flake8 src/ tests/

# Formater le code
black src/ tests/

# Vérifier les types
mypy src/

pip install -r requirements.txt


# Activer l'environnement virtuel
source venv/bin/activate  # Windows : venv\Scripts\activate


couverture minimal : pytest --cov=calculs --cov-report=term-missing --cov-fail-under=95




# Exécutable
pyinstaller --onefile --name calculs main.py

sudo apt install python3-venv
