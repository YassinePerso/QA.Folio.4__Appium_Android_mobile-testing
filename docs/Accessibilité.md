# Audit accessibilité

Ce document synthétise les vérifications d'accessibilité automatisées menées sur l'application. Les critères RGAA (Référentiel Général d'Amélioration de l'Accessibilité) sont un référentiel conçu pour le web, sans portée légale sur une application Android native. Ils sont utilisés ici comme grille de lecture transposée au mobile, parce que les principes qu'ils portent (étiquettes, contraste, structure, taille des zones interactives) sont universels à l'accessibilité numérique, pas parce que l'app est soumise à une obligation RGAA.

## Résultats

| Critère RGAA (équivalent web) | Principe | Élément testé | Test | Résultat |
|---|---|---|---|---|
| 11.1 | Chaque champ de formulaire a une étiquette | Champs username / password (écran Login) | `test_login_accessibility.py` | Non conforme |
| 1.1 / 1.3 | Chaque élément porteur d'information a une alternative textuelle | Image produit, icône panier (catalogue) | `test_catalog_accessibility.py` | Conforme |
| 1.1 / 1.3 | Chaque élément porteur d'information a une alternative textuelle | Boutons quantité et suppression (panier) | `test_cart_accessibility.py` | Conforme |
| 1.1 / 1.3 | Chaque élément porteur d'information a une alternative textuelle | Items du menu latéral (Catalog, QR Code Scanner) | `test_menu_accessibility.py` | Non conforme |
| 12.x (principe transposé) | Zones interactives suffisamment grandes | Boutons quantité (panier), icônes (header) | `test_touch_targets.py` | Conforme (66 à 79px, seuil 48px) |
| 3.2 | Contraste suffisant entre texte et fond | Titre produit (catalogue) | `test_contrast.py` | Conforme (21:1, seuil AA 4.5:1) |
| 9.1 | Structuration de l'information par des titres | Titres d'écran Products, Login | `test_headings.py` | Non conforme |

## Synthèse

4 vérifications sur 7 sont conformes, 3 documentent un manquement réel. Chaque résultat, positif ou négatif, a été confirmé par une preuve technique directe (attribut d'accessibilité lu dans l'arbre UiAutomator2, mesure de pixels, calcul de contraste WCAG), jamais supposé.

Points de vigilance identifiés :

- Les champs de saisie de l'écran de connexion ne sont identifiables par aucun lecteur d'écran (ni `content-desc`, ni `text`).
- Le menu de navigation ne distingue ses items que par leur texte visible ; l'item "Login" fait exception, probablement pour des besoins d'automatisation du fournisseur de l'app plutôt que pour l'accessibilité.
- Aucun titre d'écran n'est structurellement marqué comme tel, ce qui empêche une navigation rapide entre sections pour un utilisateur de lecteur d'écran.

## Méthode

Chaque test interroge directement l'arbre d'accessibilité exposé par UiAutomator2 (via `page_source` ou les attributs d'élément), à l'exception du contraste, calculé à partir d'une capture d'écran réelle et de la formule de luminance relative WCAG 2.x. Aucun résultat n'a été affirmé sans preuve technique vérifiable dans le code du test correspondant.

Point méthodologique notable : lors de l'écriture du test sur les labels du login, une première version de l'assertion (`get_attribute("content-desc") not in (None, "")`) a laissé passer un faux positif - UiAutomator2 renvoie la chaîne littérale `'null'`, pas `None`, quand l'attribut est absent. Le résultat "trop propre" a été questionné plutôt qu'accepté tel quel, ce qui a permis de corriger la détection et d'obtenir un résultat fiable.