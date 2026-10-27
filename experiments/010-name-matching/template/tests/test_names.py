from crmsync.names import find_existing, same_customer


def test_identical_names():
    assert same_customer("Brandt Söhne KG", "Brandt Söhne KG")


def test_surrounding_spaces():
    assert same_customer("  Kieler Werft GmbH ", "Kieler Werft GmbH")


def test_nordwind_duplicate():
    # Reported by sales: Contactly already has this customer, and our sync created a second record.
    existing = ["Nordlicht Reisen AG", "Nordwind Logistik GmbH"]
    assert find_existing("NORDWIND Logistik GmbH", existing) == "Nordwind Logistik GmbH"
