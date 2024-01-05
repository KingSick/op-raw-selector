import setuptools

setuptools.setup(
    name="op_raw_selector",
    version="0.0.1",
    author="MINT",
    author_email="pb1123love@gmail.com",
    description="Ophilia Picture RAW-Selector CLI",
    long_description_content_type="text/markdown",
    url="<https://github.com/KingSick/op-raw-selector>",
    packages=setuptools.find_packages(
        where=".", exclude=("tests", "*.tests", "scripts", "docs")
    ),
    zip_safe=False,
    python_requires=">=3.9",
    install_requires=[
        "rich-click >= 1.7.2",
    ],
    entry_points={
        "console_scripts": [
            "op-raw-select=raw_selector:cli",
        ],
    },
)
