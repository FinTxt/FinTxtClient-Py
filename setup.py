from setuptools import setup, find_packages
import FinTxtClient

setup(
    name='FinTxtClient',
    version=FinTxtClient.__version__,
    description="Client library for accessing FinTxt.io's News Intensity API.",
    keywords='finance investing commodities text processing machine intelligence',
    url='https://github.com/FinTxt/FinTxtClient-Py',
    author='Jasper Ginn',
    author_email='jasperginn@gmail.com',
    license='GPL3',
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=['requests', 'datetime', 'warnings'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Finance :: Investing',
        'License :: OSI Approved :: OpenGPL3 License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
      ],
)
