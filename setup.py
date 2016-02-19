from setuptools import setup, find_packages

install_requires = [
	'scikit-learn',
	'numpy',
	'nibabel',
	'nilearn',
        'joblib'
]

def readme():
	with open('README.rst') as f:
		return f.read()

setup(
	name='scikit-bold',
	version='0.1.3',
    description='Tools to convert and transform first-level fMRI data to scikit-learn compatible data-structures',
    long_description=readme(),
    classifiers=[
    	'Development Status :: 1 - Planning',
    	'Intended Audience :: Science/Research',
    	'Operating System :: POSIX :: Linux',
    	'Programming Language :: Python :: 2.7',
    	'Topic :: Scientific/Engineering :: Bio-Informatics'],
    keywords = "fMRI scikit-learn RSA representational simililarity analysis",
    url='https://github.com/lukassnoek/scikit-bold',
    author='Lukas Snoek',
    author_email='lukassnoek@gmail.com',
    license='MIT',
    platforms='Linux',
    packages=find_packages(),
    zip_safe=False)