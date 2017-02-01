from setuptools import setup

try:
    import pypandoc
    description=pypandoc.convert('readme.md','rst')
except:
    description=''
setup(name='Offdownloader',
      version="1.0.2",
      description='Downloads Documentation from ReadTheDocs in multiple formats',
      long_description=description,
      url='https://github.com/gkdeveloper/Off-documention',
      author='Gaurav Kumar Verma',
      author_email='gkverma1094@gmail.com',
      packages=['Off    Downloader'],
      install_requires=[
          'beautifulsoup4',
          'requests'  ,'wget' ],
      scripts=['bin/offdownloader'],
      classifiers=[
          "Development Status :: 1 - Beta",
          "Topic :: Utilities",
          "Operating System :: OS Independent",
          "Programming Language :: Python"
      ],
      zip_safe=False)
