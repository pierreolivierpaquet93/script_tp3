import unittest
from Enonce_02_Compte import CompteBancaire

class TestCompteBancaire(unittest.TestCase):

    def test_creation_compte_positif(self):
        # TODO: Vérifier qu'un compte avec solde initial positif est bien créé
        compte = CompteBancaire( "Pierre Olivier", 1000.00 )
        self.assertGreater( compte.solde, 0 )

    def test_creation_compte_solde_zero(self):
        # TODO: Vérifier qu'un compte créé sans solde initial a bien solde = 0
        compte = CompteBancaire( "Pierre Olivier" )
        self.assertEqual( compte.solde, 0 )

    def test_creation_compte_negatif(self):
        # TODO: Vérifier qu'une exception est levée si solde initial < 0
		# https://stackoverflow.com/questions/129507/how-do-you-test-that-a-python-function-throws-an-exception
        self.assertRaises(
            Exception,
            CompteBancaire,
            "Pierre Olivier",
            -1000
        )

    def test_depot_valide(self):
        # TODO: Vérifier qu'un dépôt augmente bien le solde
        solde_initial = 1000
        compte = CompteBancaire( "Pierre Olivier", solde_initial)
        compte.deposer( 0.01 )
        self.assertGreater( compte.solde, solde_initial )

    def test_depot_zero(self):
        # TODO: Vérifier qu'un dépôt de 0 déclenche une exception "ValueError"
        compte = CompteBancaire( "Pierre Olivier", 1000 )
        self.assertRaises(
            ValueError,
            compte.deposer,
            0
        )

    def test_depot_negatif(self):
        # TODO: Vérifier qu'un dépôt négatif déclenche une exception "ValueError"
        compte = CompteBancaire( "Pierre Olivier", 1000 )
        self.assertRaises(
            ValueError,
            compte.deposer,
            -100
        )

    def test_retrait_valide(self):
        # TODO: Vérifier qu'un retrait valide diminue le solde
        solde_initial = 1000
        compte = CompteBancaire( "Pierre Olivier", solde_initial )
        compte.retirer( 0.01 )
        self.assertLess(
            compte.solde,
            solde_initial
        )

    def test_retrait_trop_eleve(self):
        # TODO: Vérifier qu'on ne peut pas retirer plus que le solde disponible (déclenche une exception "ValueError")
        solde_initial = 1000
        compte = CompteBancaire( "Pierre Olivier", solde_initial )
        self.assertRaises(
            ValueError,
            compte.retirer,
            solde_initial+0.01
        )

    def test_retrait_zero(self):
        # TODO: Vérifier qu'un retrait de 0 déclenche une exception "ValueError"
        compte = CompteBancaire( "Pierre Olivier", 1000 )
        self.assertRaises(
            ValueError,
            compte.retirer,
            0
        )

    def test_retrait_negatif(self):
        # TODO: Vérifier qu'un retrait négatif déclenche une exception "ValueError"
        compte = CompteBancaire( "Pierre Oliver", 1000 )
        self.assertRaises(
            ValueError,
            compte.retirer,
            -0.01
        )

    def test_transfert_valide(self):
        # TODO: Vérifier qu'un transfert valide fonctionne sur les deux comptes
        valeur_transfert = 200
        solde_initial_compte1 = 1000
        solde_initial_compte2 = 2000
        compte1 = CompteBancaire( "Pierre Olivier", solde_initial_compte1 )
        compte2 = CompteBancaire( "Andrée Anne", solde_initial_compte2 )
        compte1.transfert( compte2, valeur_transfert )
        self.assertTrue(
            compte1.solde == solde_initial_compte1 - valeur_transfert and
            compte2.solde == solde_initial_compte2 + valeur_transfert
        )

    def test_transfert_insuffisant(self):
        # TODO: Vérifier qu'on ne peut pas transférer plus que le solde disponible (déclenche une exception "ValueError")
        compte1 = CompteBancaire( "Pierre Olivier", 1000 )
        compte2 = CompteBancaire( "Andrée Anne", 1000 )
        self.assertRaises( 
            ValueError,
            compte1.transfert,
            compte2,
            1001    
		)

    def test_transfert_vers_objet_invalide(self):
        # TODO: Vérifier qu'on ne peut pas transférer vers un objet non CompteBancaire (déclenche une exception "TypeError")
        compte1 = CompteBancaire( "Pierre Olivier", 1000 )
        compte2 = ["Andrée Anne", 1000]
        self.assertRaises(
            TypeError,
            compte1.transfert,
            compte2,
            200
        )

    def test_transfert_vers_soi_meme_impossible(self):
        # TODO: Vérifier qu'on ne peut pas transférer vers son propre compte (déclenche une exception "ValueError")
        compte = CompteBancaire( "Pierre Olivier", 1000 )
        self.assertRaises(
            ValueError,
            compte.transfert,
            compte,
            42
        )

    def test_est_vide_false(self):
        # TODO: Vérifier que est_vide retourne False quand solde > 0
        compte = CompteBancaire( "Pierre Olivier", 1000 )
        self.assertFalse( compte.est_vide() )

    def test_est_a_decouvert_true(self):
        # TODO: Vérifier que est_vide retourne True quand solde == 0
        compte = CompteBancaire( "Pierre Olivier" )
        self.assertTrue( compte.est_vide() )

    def test_str_contient_titulaire_et_solde(self):
        # TODO: Vérifier que __str__ contient bien le nom et le solde
        nom = "Pierre Olivier"
        solde = 1000
        compte = CompteBancaire( nom, solde )
        to_check = compte.__str__()
        i_nom = to_check.find( nom )
        i_solde = to_check.find( str(solde) )
        self.assertTrue(
            i_nom >= 0 and
            i_solde >= 0
		)
 
    def test_depots_consecutifs(self):
        # TODO: Vérifier que plusieurs dépôts consécutifs s'accumulent correctement
        depots = [
            22.87,
            40.00,
            67.22,
            101.89,
            266.83,
            65.01,
            42.42
        ]
        solde_initial = 4657.89
        total_depots = 0
        for montant in depots:
            total_depots += montant
        compte = CompteBancaire( "Pierre Olivier", solde_initial )
        for montant in depots:
            compte.deposer( montant )
        verification = compte.solde - total_depots
        self.assertAlmostEqual( solde_initial, verification )

    def test_retraits_consecutifs(self):
        # TODO: Vérifier que plusieurs retraits consécutifs s'accumulent correctement
        retraits = [
            132.87,
            46.12,
            150.00,
            576.27,
            21.44,
            456.29,
            63.97
		]
        solde_initial = 9653.42
        total_retraits = 0
        for montant in retraits:
            total_retraits += montant
        compte = CompteBancaire( "Pierre Olivier", solde_initial )
        for montant in retraits:
            compte.retirer( montant )
        verification = compte.solde + total_retraits
        self.assertAlmostEqual( solde_initial, verification )

    def test_depot_et_retrait_combines(self):
        # TODO: Vérifier qu'une suite de dépôt puis retrait donne le solde attendu
        depots = [
            98.87,
            102.56,
            39.55,
            78.99,
            909.03,
            62.12,
            10.98,
            43.09,
            11981.31
		]
        total_depots = 0
        for montant in depots:
            total_depots += montant
        retraits = [
            56.22,
            21.96,
            189.09,
            505.44,
            19.68,
            397.53,
            709.92
		]
        total_retraits = 0
        for montant in retraits:
            total_retraits += montant
        solde_initial = 5449.93
        compte = CompteBancaire( "Pierre Olivier", solde_initial )
        for montant in depots:
            compte.deposer( montant )
        for montant in retraits:
            compte.retirer( montant )
        verification = solde_initial + total_depots - total_retraits
        self.assertAlmostEqual( compte.solde, verification )

def main():
    unittest.main()

if __name__ == "__main__":
    main()