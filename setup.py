from setuptools import find_packages, setup

setup(
    name="viz_embeds",
    version="0.1",
    description="Embeddings projections using TensorFlow Projector and HuggingFace Transformers.",
    package_dir={'': "src"},
    packages=find_packages("src"),
    install_requires=[
        'boto3==1.12.43',
        'botocore==1.15.43',
        'certifi==2020.4.5.1',
        'chardet==3.0.4',
        'click==7.1.1',
        'docutils==0.15.2',
        'filelock==3.0.12'
        'idna==2.9',
        'jmespath==0.9.5',
        'joblib==0.14.1',
        'nltk==3.5',
        'numpy==1.18.3',
        'python-dateutil==2.8.1',
        'regex==2020.4.4',
        'requests==2.23.0',
        's3transfer==0.3.3',
        'sacremoses==0.0.41',
        'sentencepiece==0.1.85',
        'six==1.14.0',
        'tokenizers==0.5.2',
        'tqdm==4.45.0',
        'transformers==2.8.0',
        'urllib3==1.25.9',
    ],
    entry_points={
        "console_scripts": [
            "vizembeds=viz_embeddings.main:main",
        ],
    },
    zip_safe=False,
)