from setuptools import setup
import json

with open("metadata.json", encoding="utf-8") as fp:
    metadata = json.load(fp)


setup(
    name="lexibank_saenkoromance",
    description=metadata["title"],
    license=metadata.get("license", ""),
    url=metadata.get("url", ""),
    py_modules=["lexibank_saenkoromance"],
    include_package_data=True,
    zip_safe=False,
    entry_points={"lexibank.dataset": ["saenkoromance=lexibank_saenkoromance:Dataset"]},
    extras_require={"test": ["pytest-cldf"]},
    install_requires=["pylexibank>=3.0"],
)
