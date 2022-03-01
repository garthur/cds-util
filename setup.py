
from setuptools import setup, find_packages
  
with open('requirements.txt') as f:
    requirements = f.readlines()

  
setup(
        name ='cds_util',
        version ='1.0.0',
        author ='Graham Arthur',
        author_email ='graham.d.arthur18@gmail.com',
        description ='Climate Data Science util package.',
        license ='MIT',
        packages = find_packages(),
        entry_points ={
            'console_scripts': [
                'cds-era5 = cds_util.era5:main',
                'cds-ncep = cds_util.ncep:main'
            ]
        },
        classifiers =(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ),
        keywords="cds",
        install_requires = requirements,
        zip_safe = False
)