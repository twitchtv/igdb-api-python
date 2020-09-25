from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
  name="igdb-api-v4",
  version="0.0.3",
  author="Felix Nordén",
  author_email="felixnorden@gmail.com",
  description="An API wrapper for IGDB API v4",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/twitchtv/igdb-api-python/",
  classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
  ],
  python_requires='>=3',
  packages=['igdb'],
  package_dir={'igdb': 'src/igdb'},
  install_requires=['requests', 'protobuf']
)
