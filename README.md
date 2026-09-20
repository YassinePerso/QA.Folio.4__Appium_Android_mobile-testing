# QA Mobile Portfolio - Appium & Android

Un portfolio de test automatisé mobile, 100% open source, 100% local, sans device farm ni service payant.

## Pourquoi ce projet

Après trois portfolios centrés sur le web (Selenium E2E/API/BDD, Playwright + Agile, k6 + observabilité), celui-ci explore un terrain différent : le test mobile natif Android, avec ses propres contraintes (permissions runtime, rotation, cycle de vie de l'app, interruptions système) qu'aucun outil web ne couvre.

## Stack

- Node.js + Appium 3.x (serveur) + driver UiAutomator2
- Android SDK command-line tools + émulateur AVD
- Python + Appium-Python-Client + pytest
- GitHub Actions avec `reactivecircus/android-emulator-runner` pour le CI
- Allure pour le reporting

## L'app testée

[My Demo App Android](https://github.com/saucelabs/my-demo-app-android) de Sauce Labs, une app native pensée pour l'automatisation, avec un vrai flow e-commerce (login, catalogue, panier, checkout) et une fonctionnalité caméra (scanner QR) qui déclenche une permission runtime.

**Point de transparence** : le repo est public mais ne porte aucune licence open source explicite. Le code est consultable et l'app est utilisée ici uniquement comme cible d'automatisation, pas redistribuée. Une alternative strictement licenciée (Wikipedia Android, Apache 2.0) a été évaluée mais écartée : moins adaptée à l'automatisation, sans scénarios de permission ou de flow métier prêts à l'emploi.

## Structure

```
tests/
├── pages/                  Page Object Model (locators + actions)
├── test_functional/        login, panier, checkout
├── test_mobile_specific/   permissions, rotation, background/foreground, interruptions
└── conftest.py             fixture driver partagée
```

## Ce que ce projet démontre

**Setup environnement Linux sans Android Studio**

Appium et émulateur configurés en ligne de commande, avec de vrais obstacles rencontrés et résolus : GPU AMD blacklisté par l'émulateur, crash de snapshot incompatible avec le mode GPU, faux positifs GNOME sur la fenêtre émulateur.

**Rigueur sur les assertions**

Un premier test d'ajout au panier ne vérifiait qu'un clic, pas le résultat réel. Corrigé pour valider le badge panier, le titre produit et le compteur : la différence entre "le code s'exécute" et "le comportement est validé".

**Spécificités mobiles couvertes**, avec à chaque fois la question posée avant d'écrire le test :

→ *Permissions runtime* : que se passe-t-il en cas de refus (deux refus nécessaires, comportement Android depuis l'API 23) ? Et en cas d'acceptation ?

→ *Background/foreground* : l'état d'un formulaire et d'un panier survit-il à une mise en arrière-plan ? Et à plusieurs cycles consécutifs ?

→ *Interruption système* : un appel entrant fait-il perdre une saisie en cours ?

→ *Rotation d'écran* : fonctionne en manuel via l'UI de l'émulateur, mais échoue en programmatique sur cette configuration (rendu logiciel SwiftShader/AMD). Documenté comme limitation d'environnement plutôt que masqué : le test existe, marqué `skip`, avec l'explication du diagnostic.

## Lancer les tests

```bash
# Terminal 1
emulator -avd pixel_test -gpu host

# Terminal 2
appium

# Terminal 3
pytest tests/ -v
```

## Prochaine étape

Industrialisation : CI/CD via GitHub Actions, reporting Allure, et checks d'accessibilité automatisés sur l'arbre `content-desc`.
