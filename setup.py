import setuptools

setuptools.setup(
    name="ophilia_picture_row_selector",
    version="0.0.1",
    author="MINT",
    author_email="pb1123love@gmail.com",
    description="Ophilia Picture Row-Selector CLI",
    long_description_content_type="text/markdown",
    url="<https://github.com/KingSick/ophilia-row-selector>",
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
            "op-row-select=row_selector:cli",
        ],
    },
)
