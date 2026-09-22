# Cas de test

Matrice des scénarios couverts par la suite automatisée. Statut DONE signifie testé et validé par un pipeline d'exécution réel (pas seulement rédigé).

## Fonctionnel classique

| ID | Titre | Préconditions | Étapes | Résultat attendu | Statut |
|----|-------|----------------|--------|-------------------|--------|
| TC-01 | Connexion avec identifiants valides | Application lancée, aucun utilisateur connecté | 1. Ouvrir le menu 2. Sélectionner "Log In" 3. Saisir email et mot de passe valides 4. Valider | L'utilisateur est connecté, retour à l'écran catalogue | DONE |
| TC-02 | Ajout d'un produit au panier | Utilisateur sur le catalogue | 1. Ouvrir un produit 2. Cliquer "Add to cart" | Le badge panier affiche 1, le produit apparaît dans le panier avec le bon titre | DONE |
| TC-03 | Le checkout redirige vers le login si non connecté | Produit dans le panier, utilisateur non connecté | 1. Ouvrir le panier 2. Cliquer "Proceed To Checkout" | Redirection vers l'écran de connexion | DONE |
| TC-04 | Flow complet jusqu'à l'écran de paiement | Utilisateur connecté | 1. Ajouter un produit 2. Ouvrir le panier 3. Lancer le checkout | Arrivée sur l'écran "Checkout" avec formulaire d'adresse pré-rempli | DONE |

## Mobile spécifique : permissions runtime

| ID | Titre | Préconditions | Étapes | Résultat attendu | Statut |
|----|-------|----------------|--------|-------------------|--------|
| TC-05 | Refus de la permission caméra | Permission caméra non encore accordée | 1. Ouvrir le scanner QR 2. Refuser la popup deux fois (comportement Android natif) | L'application ne plante pas, reste sur son propre package | DONE |
| TC-06 | Acceptation de la permission caméra | Permission caméra non encore accordée | 1. Ouvrir le scanner QR 2. Accepter "While using the app" | L'application reste active, accès à la fonctionnalité caméra | DONE |

## Mobile spécifique : cycle de vie de l'application

| ID | Titre | Préconditions | Étapes | Résultat attendu | Statut |
|----|-------|----------------|--------|-------------------|--------|
| TC-07 | Un formulaire survit à une mise en arrière-plan | Champ username en cours de saisie | 1. Saisir du texte 2. Mettre l'app en arrière-plan 5s 3. Revenir | Le texte saisi est toujours présent | DONE |
| TC-08 | Le panier survit à une mise en arrière-plan | Produit ajouté au panier | 1. Ajouter un produit 2. Mettre l'app en arrière-plan 5s 3. Revenir | Le badge panier affiche toujours 1 | DONE |
| TC-09 | Retour rapide après mise en arrière-plan | Champ username en cours de saisie | 1. Saisir du texte 2. Mettre l'app en arrière-plan 1s 3. Revenir | Le texte saisi est toujours présent | DONE |
| TC-10 | Cycles multiples de mise en arrière-plan | Produit ajouté au panier | 1. Ajouter un produit 2. Répéter trois fois : mise en arrière-plan 2s puis retour | Le badge panier reste correct après chaque cycle | DONE |

## Mobile spécifique : interruptions système

| ID | Titre | Préconditions | Étapes | Résultat attendu | Statut |
|----|-------|----------------|--------|-------------------|--------|
| TC-11 | Un appel entrant ne fait pas perdre une saisie | Champ username en cours de saisie | 1. Saisir du texte 2. Simuler un appel entrant 3. Terminer l'appel | Le texte saisi est toujours présent au retour sur l'application | DONE |

## Mobile spécifique : orientation

| ID | Titre | Préconditions | Étapes | Résultat attendu | Statut |
|----|-------|----------------|--------|-------------------|--------|
| TC-12 | L'interface reste utilisable après rotation | Écran de connexion affiché | 1. Passer en paysage 2. Saisir du texte 3. Repasser en portrait 4. Saisir un second champ | Les deux champs restent accessibles et utilisables dans les deux orientations | SKIP (voir methodology.md) |

Le TC-12 échoue systématiquement en exécution programmatique sur cet émulateur (rendu logiciel, GPU non supporté), alors que le même geste fonctionne manuellement via l'interface de l'émulateur. Il est conservé dans le code avec un marqueur `skip` explicite plutôt que supprimé. Le détail du diagnostic est dans `methodology.md`.