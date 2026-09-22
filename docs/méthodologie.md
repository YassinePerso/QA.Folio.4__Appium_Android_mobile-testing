# Méthodologie

Ce document explique la démarche derrière ce projet, pas seulement le résultat. Trois principes reviennent régulièrement au fil du développement.

## 1. Diagnostiquer par la preuve, jamais par supposition

Chaque bug rencontré a été résolu en observant l'état réel de l'application avant d'agir, jamais en devinant une solution.

**Exemple concret : le bouton de refus de permission introuvable**

Un test cliquait sur `permission_deny_button`, fonctionnel une première fois puis introuvable une seconde. Plutôt que de supposer un problème de timing ou de driver, l'écran a été dumpé (`uiautomator dump`) immédiatement après chaque clic. La comparaison des XML a révélé que l'identifiant du bouton change selon l'historique des refus sur la session : `permission_deny_button` au premier refus, `permission_deny_and_dont_ask_again_button` au second. Ce n'était pas un bug, mais un comportement Android natif depuis l'API 23. Le test a été corrigé pour cibler le texte visible plutôt qu'un identifiant instable, et gère maintenant les deux refus successifs qu'Android impose.

Cette méthode (observer avant de corriger) s'applique à chaque anomalie du projet : le diagnostic du GPU AMD blacklisté par l'émulateur, le crash de snapshot, ou la redirection du checkout vers le login ont tous été confirmés par preuve (logs, dumps XML, captures d'écran) avant toute correction.

## 2. Savoir arrêter, et documenter plutôt que masquer

Le scénario de rotation d'écran programmatique a été tenté selon quatre approches différentes : réglage système `accelerometer_rotation` dans les deux sens, capability Appium `autoGrantPermissions`, version minimale isolée du test. Chacune a échoué avec la même erreur (`Screen rotation cannot be changed... Is it locked programmatically?`).

La rotation fonctionne pourtant manuellement, via l'icône de l'interface de l'émulateur. Ça a permis d'isoler la cause réelle : deux mécanismes de rotation distincts existent sur l'émulateur (interface Qt vs commande système UiAutomator2), et seul le second échoue sur cette configuration, très probablement à cause du rendu logiciel (SwiftShader) utilisé faute d'accélération GPU native sur ce matériel AMD.

Plutôt que de masquer ce scénario ou de s'acharner indéfiniment, le test est conservé dans le code avec un marqueur `@pytest.mark.skip` et une raison explicite. Un projet où tout passe sans qu'aucune limite ne soit jamais rencontrée est moins crédible qu'un projet qui documente honnêtement ce qui ne fonctionne pas, et pourquoi.

## 3. Vérifier avant de s'engager, pas après

Avant de choisir l'application cible (Sauce Labs My Demo App Android), sa licence a été vérifiée directement dans le repository plutôt que supposée à partir de sa popularité ou de son usage répandu dans d'autres projets similaires. Aucun fichier `LICENSE` n'y est présent, contrairement à d'autres repositories Sauce Labs comparables. Ce point est documenté dans le README plutôt que passé sous silence, avec la justification du choix malgré cette limite.

## Questions posées avant chaque scénario mobile-spécifique

Un scénario mobile n'a de valeur que s'il répond à une vraie question de comportement, pas seulement s'il "clique quelque part". Voici les questions posées avant l'écriture de chaque test :

**Permissions runtime (caméra, scanner QR)**
Que se passe-t-il en cas de refus ? L'application redemande-t-elle, combien de fois, avec quel comportement ? Et en cas d'acceptation, l'accès à la fonctionnalité est-il immédiat ?

**Background / foreground**
L'état d'un formulaire en cours de saisie survit-il à une mise en arrière-plan ? Le contenu du panier, qui représente un état métier plus riche qu'un simple champ texte, est-il conservé de la même façon ? Un retour rapide (quasi accidentel) se comporte-t-il différemment d'un retour après plusieurs cycles consécutifs ?

**Interruption système (appel entrant)**
Une saisie en cours est-elle perdue si un appel interrompt l'utilisateur ? L'application reprend-elle normalement une fois l'appel terminé ?

**Rotation d'écran**
L'interface reste-t-elle utilisable après un changement d'orientation, pas seulement l'attribut technique change-t-il ? Un champ rempli avant rotation est-il toujours accessible après ?

Ces questions, plus que le code lui-même, définissent ce qui distingue un test mobile pertinent d'un test qui se contente d'exécuter des actions sans rien valider de réel.