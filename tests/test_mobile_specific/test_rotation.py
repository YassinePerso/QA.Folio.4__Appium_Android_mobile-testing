import pytest

#Test de rotation exécuter manuellement via l'UI de l'émulateur. La rotation programmatique n'est pas supportée par cet émulateur (rendu logiciel AMD/SwiftShader). Voir documentation.
@pytest.mark.skip(reason="Rotation programmatique non supportée par cet émulateur (rendu logiciel AMD/SwiftShader). Fonctionne en rotation manuelle via l'UI de l'émulateur. Voir documentation.")
def test_orientation_basic(driver):
    ...