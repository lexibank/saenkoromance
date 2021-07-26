def test_valid(cldf_dataset, cldf_logger):
    assert cldf_dataset.validate(log=cldf_logger)


def test_forms(cldf_dataset):
    assert len(list(cldf_dataset["FormTable"])) == 4853
    assert any(f["Form"] == "n.ˈe.ɡ.r.+.u" for f in cldf_dataset["FormTable"])


def test_parameters(cldf_dataset):
    assert len(list(cldf_dataset["ParameterTable"])) == 110


def test_languages(cldf_dataset):
    assert len(list(cldf_dataset["LanguageTable"])) == 43
