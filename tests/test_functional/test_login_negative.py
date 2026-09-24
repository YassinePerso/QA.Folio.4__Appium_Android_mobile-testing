from tests.pages.login_page import LoginPage


def test_login_ignores_incorrect_password(driver):
    """
    Découverte : cette app de démo ne valide pas réellement le mot de passe,
    seul le username doit correspondre à un compte prédéfini. Documenté ici
    plutôt que supposé, après vérification via dumpsys que l'app atterrit
    bien sur MainActivity (post-connexion) malgré un mot de passe incorrect.
    """
    login_page = LoginPage(driver)
    login_page.login("bod@example.com", "azerty000_mot_de_passe_incorrect")

    assert driver.current_activity == ".view.activities.MainActivity"


def test_locked_out_label_does_not_actually_block_login(driver):
    """
    Découverte : malgré l'étiquette "(locked out)" affichée sur ce compte
    dans les données de démo de l'app, la connexion aboutit normalement.
    Vérifié manuellement via dumpsys avant d'écrire cette assertion.
    """
    login_page = LoginPage(driver)
    login_page.login("alice@example.com", "10203040")

    assert driver.current_activity == ".view.activities.MainActivity"