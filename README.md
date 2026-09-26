# QA Mobile Portfolio - Appium & Android

Un portfolio de test automatisé mobile, 100% open source, 100% local, sans device farm ni service payant.

## Pourquoi ce projet

Après trois portfolios centrés sur le web (Selenium E2E/API/BDD, Playwright + Agile, k6 + observabilité), celui-ci explore un terrain différent : le test mobile natif Android, avec ses propres contraintes (permissions runtime, rotation, cycle de vie de l'app, interruptions système) qu'aucun outil web ne couvre.

## Stack

- Node.js + Appium 3.x (serveur) + driver UiAutomator2
- Android SDK command-line tools + émulateur AVD
- Python + Appium-Python-Client + pytest
- Pillow, pour les vérifications d'accessibilité (mesure de contraste)
- GitHub Actions avec `reactivecircus/android-emulator-runner` pour le CI
- Allure pour le reporting

## L'app testée

[My Demo App Android](https://github.com/saucelabs/my-demo-app-android) de Sauce Labs, une app native pensée pour l'automatisation, avec un vrai flow e-commerce (login, catalogue, panier, checkout) et une fonctionnalité caméra (scanner QR) qui déclenche une permission runtime.

Point de transparence : le repo est public mais ne porte aucune licence open source explicite. Le code est consultable et l'app est utilisée ici uniquement comme cible d'automatisation, pas redistribuée. Une alternative strictement licenciée (Wikipedia Android, Apache 2.0) a été évaluée mais écartée : moins adaptée à l'automatisation, sans scénarios de permission ou de flow métier prêts à l'emploi.

## Structure

```
tests/
├── pages/                  Page Object Model (locators + actions)
├── test_functional/        login, panier, checkout
├── test_mobile_specific/   permissions, rotation, background/foreground, interruptions
├── test_accessibility/     étiquettes, taille des zones interactives, contraste, titres
└── conftest.py             fixture driver partagée
```

## Ce que ce projet démontre

**Setup environnement Linux sans Android Studio**
Appium et émulateur configurés en ligne de commande, avec de vrais obstacles rencontrés et résolus : GPU AMD blacklisté par l'émulateur, crash de snapshot incompatible avec le mode GPU, faux positifs GNOME sur la fenêtre émulateur.

**Rigueur sur les assertions**
Un premier test d'ajout au panier ne vérifiait qu'un clic, pas le résultat réel. Corrigé pour valider le badge panier, le titre produit et le compteur : la différence entre "le code s'exécute" et "le comportement est validé". Le même principe a mis au jour deux comportements réels de l'app : la connexion accepte n'importe quel mot de passe, et l'étiquette "(locked out)" affichée sur certains comptes est purement visuelle.

**Spécificités mobiles couvertes**, avec à chaque fois la question posée avant d'écrire le test :

- Permissions runtime : que se passe-t-il en cas de refus (deux refus nécessaires, comportement Android depuis l'API 23) ? Et en cas d'acceptation ?
- Background/foreground : l'état d'un formulaire et d'un panier survit-il à une mise en arrière-plan ? Et à plusieurs cycles consécutifs ?
- Interruption système : un appel entrant fait-il perdre une saisie en cours ?
- Rotation d'écran : fonctionne en manuel via l'UI de l'émulateur, mais échoue en programmatique sur cette configuration (rendu logiciel SwiftShader/AMD). Documenté comme limitation d'environnement plutôt que masqué : le test existe, marqué `skip`, avec l'explication du diagnostic.

**Accessibilité**, avec la même logique de preuve avant conclusion : quatre axes vérifiés (étiquettes pour lecteur d'écran, taille des zones cliquables, contraste des couleurs, structuration par titres), sur une grille de lecture inspirée du RGAA (informelle, sans portée légale sur une app native). Résultat publié tel quel : 4 vérifications sur 7 conformes, 3 documentent un manquement réel. Détail complet dans `accessibility-audit.md`.

**CI/CD**
Chaque push déclenche la suite de tests sur un émulateur Android hébergé par GitHub Actions. Les tests partagent une seule session Appium par exécution (au lieu d'une session par test), avec une réinitialisation légère de l'app entre chaque test : ce choix a résolu un crash système rencontré lors des premières exécutions en CI. Le démarrage de l'émulateur reste parfois instable de façon intermittente (limitation connue de l'action utilisée) ; une reprise automatique à trois tentatives absorbe une partie de cette instabilité, sans la garantir à 100%.

## Lancer les tests

```
# Terminal 1
emulator -avd pixel_test -gpu host

# Terminal 2
appium

# Terminal 3
pytest tests/ -v
```

Rapport Allure :

```
pytest tests/ --alluredir=allure-results
allure generate allure-results --clean -o allure-report
allure open allure-report
```