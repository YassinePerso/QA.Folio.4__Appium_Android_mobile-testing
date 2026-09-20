import subprocess
import time
from tests.pages.login_page import LoginPage

# Test pour vérifier que le formulaire de connexion reste intact après un appel entrant
def test_form_survives_incoming_call(driver):
    login_page = LoginPage(driver)
    login_page.navigate_to_login()
    login_page.type_text(login_page.USERNAME_FIELD, "bod@example.com")
    # Lancer un appel entrant simulé
    subprocess.run(["adb", "emu", "gsm", "call", "0123456789"])
    time.sleep(3)
    # Annuler l'appel entrant simulé
    subprocess.run(["adb", "emu", "gsm", "cancel", "0123456789"])
    time.sleep(2)
    # Vérifier que le texte saisi dans le champ de nom d'utilisateur est toujours présent
    field = login_page.find(login_page.USERNAME_FIELD)
    assert field.text == "bod@example.com"